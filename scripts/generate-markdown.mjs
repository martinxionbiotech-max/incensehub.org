// md-negotiation: build-time Markdown generation from final dist HTML.
// Canonical Markdown variant: /<public-path>.md (flat), with YAML frontmatter.
// One file per eligible HTML page; old/duplicate .md files are removed first.
import { readdir, readFile, writeFile, mkdir, unlink } from 'node:fs/promises';
import path from 'node:path';
import { NodeHtmlMarkdown } from 'node-html-markdown';

const DIST = 'dist';
const SKIP_DIRS = new Set(['_astro', 'images', '_md']);

async function* walk(dir) {
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return;
  }
  for (const e of entries) {
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      yield* walk(path.join(dir, e.name));
    } else if (e.name.endsWith('.html')) {
      yield path.join(dir, e.name);
    }
  }
}

async function cleanOldMarkdown(dir) {
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return 0;
  }
  let removed = 0;
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      removed += await cleanOldMarkdown(p);
    } else if (e.name.endsWith('.md')) {
      await unlink(p);
      removed++;
    }
  }
  return removed;
}

function isEligible(html) {
  if (/<meta\s+http-equiv=["']refresh/i.test(html)) return { ok: false, reason: 'redirect' };
  if (/<meta\s+name=["']robots["'][^>]*noindex/i.test(html)) return { ok: false, reason: 'noindex' };
  return { ok: true };
}

function extractMain(html) {
  const m = html.match(/<main\b[^>]*>([\s\S]*?)<\/main>/i);
  if (!m) return null;
  return m[1]
    .replace(/<script\b[\s\S]*?<\/script>/gi, '')
    .replace(/<style\b[\s\S]*?<\/style>/gi, '');
}

function decodeEntities(s) {
  return String(s)
    .replace(/&#38;/g, '&')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>');
}

function pick(html, re) {
  const m = html.match(re);
  return m ? decodeEntities(m[1].trim()) : '';
}

function findDate(html) {
  const blocks = [...html.matchAll(/<script\s+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
  for (const b of blocks) {
    try {
      const data = JSON.parse(b[1]);
      const stack = Array.isArray(data) ? [...data] : [data];
      while (stack.length) {
        const node = stack.pop();
        if (!node || typeof node !== 'object') continue;
        if (typeof node.dateModified === 'string') return node.dateModified;
        if (typeof node.datePublished === 'string') return node.datePublished;
        for (const v of Object.values(node)) {
          if (v && typeof v === 'object') stack.push(v);
        }
      }
    } catch {
      /* ignore malformed ld+json */
    }
  }
  return '';
}

function publicPathFor(file) {
  let rel = '/' + path.relative(DIST, file).split(path.sep).join('/');
  rel = rel.replace(/index\.html$/, '');
  return rel === '' ? '/' : rel;
}

function markdownPathFor(pub) {
  if (pub === '/') return '/index.md';
  return pub.replace(/\/$/, '') + '.md';
}

const manifest = {};
let generated = 0;
const skipped = [];
const warnings = [];

// Remove legacy flat/index .md files so the deployed corpus can never drift.
const removed = await cleanOldMarkdown(DIST);

for await (const file of walk(DIST)) {
  const rel = path.relative(DIST, file).split(path.sep);
  if (rel.join('/') === '404.html' || rel[0] === '404.html') {
    skipped.push(['404.html', 'error-page']);
    continue;
  }
  const html = await readFile(file, 'utf8');
  const elig = isEligible(html);
  if (!elig.ok) {
    skipped.push([rel.join('/'), elig.reason]);
    continue;
  }
  const mainHtml = extractMain(html);
  if (!mainHtml || mainHtml.trim().length < 80) {
    skipped.push([rel.join('/'), 'no-main-content']);
    continue;
  }

  let md = NodeHtmlMarkdown.translate(mainHtml, { keepDataImages: false }).trim();
  if (md.length < 40) {
    skipped.push([rel.join('/'), 'empty-after-conversion']);
    continue;
  }

  // Drop the visual breadcrumb / eyebrow line before the article H1.
  const h1 = md.search(/^#\s+/m);
  if (h1 > 0) md = md.slice(h1).trim();

  const title = pick(html, /<title>([\s\S]*?)<\/title>/i);
  const description = pick(html, /<meta\s+name=["']description["']\s+content=["']([^"']*)["']/i);
  const canonical = pick(html, /<link\s+rel=["']canonical["']\s+href=["']([^"']*)["']/i);
  const updated = findDate(html);

  const pub = publicPathFor(file);
  const mdPath = markdownPathFor(pub);
  const section = pub === '/' ? 'home' : pub.split('/')[1] || 'home';

  const fm = [
    '---',
    `title: ${JSON.stringify(title)}`,
    `description: ${JSON.stringify(description)}`,
    `canonical: ${JSON.stringify(canonical)}`,
    `section: ${JSON.stringify(section)}`,
    ...(updated ? [`updated: ${JSON.stringify(updated)}`] : []),
    '---',
    '',
  ].join('\n');

  const outFile = path.join(DIST, mdPath.replace(/^\//, ''));
  await mkdir(path.dirname(outFile), { recursive: true });
  await writeFile(outFile, fm + md + '\n', 'utf8');

  manifest[pub] = mdPath;
  generated++;
}

let missing = 0;
for (const [k, v] of Object.entries(manifest)) {
  const f = path.join(DIST, v.replace(/^\//, ''));
  try {
    await readFile(f, 'utf8');
  } catch {
    missing++;
    delete manifest[k];
    warnings.push(`missing md for ${k}`);
  }
}

await mkdir(path.join(DIST, '_md'), { recursive: true });
await writeFile(path.join(DIST, '_md', 'manifest.json'), JSON.stringify(manifest, null, 2), 'utf8');

console.log(`[md-negotiation] cleaned=${removed} generated=${generated} skipped=${skipped.length} missing=${missing}`);
for (const [p, why] of skipped.slice(0, 20)) console.log(`  skip ${p} (${why})`);
for (const w of warnings) console.log(`  warn: ${w}`);
if (generated === 0 || Object.keys(manifest).length === 0 || missing > 0) {
  console.error('[md-negotiation] critical integrity error — build fails');
  process.exit(1);
}
