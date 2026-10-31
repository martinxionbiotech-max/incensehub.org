import { readFile } from 'node:fs/promises';

// Sample 5 ingredient pages + 5 blog pages from dist.
const INGREDIENTS = ['agarwood', 'frankincense', 'myrrh', 'sandalwood', 'ambergris'];
const BLOG = ['agarwood-grading-guide', 'frankincense-incense', 'citrus-incense', 'incense-safety-guide', 'what-is-chinese-incense'];

const WHITELIST = ['efloras.org', 'gbif.org', 'checklist.cites.org', 'wikisource.org', 'ctext.org'];

function hostAllowed(url) {
  try {
    const h = new URL(url).hostname;
    return WHITELIST.some((host) => h === host || h.endsWith('.' + host));
  } catch {
    return false;
  }
}

function collectExternalUrls(node, out) {
  if (Array.isArray(node)) {
    for (const v of node) collectExternalUrls(v, out);
    return;
  }
  if (node && typeof node === 'object') {
    // sameAs and citation arrays hold external URLs
    for (const key of ['sameAs', 'citation']) {
      const val = node[key];
      if (Array.isArray(val)) {
        for (const u of val) {
          if (typeof u === 'string' && /^https?:\/\//.test(u)) out.add(u);
        }
      }
    }
    for (const v of Object.values(node)) collectExternalUrls(v, out);
  }
}

let parsed = 0;
let failed = 0;
const failures = [];
const externalUrls = new Set();

for (const slug of INGREDIENTS) {
  const html = await readFile(`dist/ingredients/${slug}/index.html`, 'utf8');
  const blocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  for (const b of blocks) {
    try {
      const obj = JSON.parse(b[1]);
      parsed++;
      collectExternalUrls(obj, externalUrls);
    } catch (e) {
      failed++;
      failures.push(`ingredients/${slug}: ${e.message}`);
    }
  }
}

for (const slug of BLOG) {
  const html = await readFile(`dist/blog/${slug}/index.html`, 'utf8');
  const blocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  for (const b of blocks) {
    try {
      const obj = JSON.parse(b[1]);
      parsed++;
      collectExternalUrls(obj, externalUrls);
    } catch (e) {
      failed++;
      failures.push(`blog/${slug}: ${e.message}`);
    }
  }
}

const whitelistViolations = [...externalUrls].filter((u) => !hostAllowed(u));

console.log(`Parsed JSON-LD blocks: ${parsed}`);
console.log(`Parse failures: ${failed}`);
if (failures.length) console.log(failures.join('\n'));
console.log(`External URLs collected (sameAs/citation): ${externalUrls.size}`);
console.log(`Whitelist violations: ${whitelistViolations.length}`);
if (whitelistViolations.length) {
  for (const u of whitelistViolations) console.log(`  VIOLATION: ${u}`);
}

if (failed === 0 && whitelistViolations.length === 0) {
  console.log('PASS');
  process.exit(0);
} else {
  console.log('FAIL');
  process.exit(1);
}
