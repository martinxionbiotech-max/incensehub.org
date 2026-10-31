import { readFile, writeFile } from 'node:fs/promises';

const SAMEAS_HOSTS = ['efloras.org', 'gbif.org', 'checklist.cites.org'];

function hostAllowed(url, hosts) {
  try {
    const h = new URL(url).hostname;
    return hosts.some((host) => h === host || h.endsWith('.' + host));
  } catch {
    return false;
  }
}

function extractExternalUrls(body, hosts) {
  if (!body) return [];
  const m = body.match(/## Sources\s*\n([\s\S]*)$/);
  if (!m) return [];
  const out = [];
  const seen = new Set();
  const re = /\[[^\]]*\]\((https?:\/\/[^\s)]+)\)/g;
  let mm;
  while ((mm = re.exec(m[1])) !== null) {
    const url = mm[1].replace(/[.,;]+$/, '');
    if (hostAllowed(url, hosts) && !seen.has(url)) {
      seen.add(url);
      out.push(url);
    }
  }
  return out;
}

const paths = ['data/ingredients.json', 'public/data/ingredients.json'];

for (const p of paths) {
  const dataset = JSON.parse(await readFile(p, 'utf8'));
  let count = 0;
  for (const entity of dataset.mainEntity || []) {
    let body = '';
    try {
      body = await readFile(`src/content/ingredients/${entity.termCode}.md`, 'utf8');
    } catch {
      body = '';
    }
    const sameAs = extractExternalUrls(body, SAMEAS_HOSTS);
    if (sameAs.length > 0) {
      entity.sameAs = sameAs;
      count++;
    }
  }
  await writeFile(p, JSON.stringify(dataset, null, 1));
  console.log(`${p}: added sameAs to ${count}/${(dataset.mainEntity || []).length} entities`);
}
