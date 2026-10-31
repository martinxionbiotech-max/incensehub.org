import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';

const SITE = 'https://incensehub.org'; // TODO: replace with production domain
const DIR = 'src/content/ingredients';

function parseFrontmatter(md) {
  const m = md.match(/^---\n([\s\S]*?)\n---/);
  if (!m) return {};
  const out = {};
  for (const line of m[1].split('\n')) {
    const kv = line.match(/^(\w+):\s*(.*)$/);
    if (!kv) continue;
    const [, key, val] = kv;
    if (key === 'aroma') {
      // aroma: ["woody", "resinous"]  -> parse array
      out.aroma = [...val.matchAll(/"([^"]*)"/g)].map((x) => x[1]);
    } else {
      out[key] = val.replace(/^"(.*)"$/, '$1');
    }
  }
  return out;
}

const files = (await readdir(DIR)).filter((f) => f.endsWith('.md')).sort();

const mainEntity = [];
for (const f of files) {
  const slug = path.basename(f, '.md');
  const md = await readFile(path.join(DIR, f), 'utf8');
  const fm = parseFrontmatter(md);
  const aroma = (fm.aroma || []).join(', ');
  const name = ((fm.title || slug).split(' — ')[0]).replace(/ \(.*\)$/, '');
  mainEntity.push({
    '@type': 'DefinedTerm',
    termCode: slug,
    name,
    alternateName: [fm.chinese, fm.pinyin, fm.scientificName].filter(Boolean),
    description: `${fm.chinese} (${fm.pinyin}) is a Chinese botanical incense ingredient — ${fm.scientificName} — with an aroma profile of ${aroma || 'n/a'}.`,
    additionalProperty: [
      { '@type': 'PropertyValue', name: 'Chinese', value: fm.chinese || '' },
      { '@type': 'PropertyValue', name: 'Pinyin', value: fm.pinyin || '' },
      { '@type': 'PropertyValue', name: 'Scientific name', value: fm.scientificName || '' },
      { '@type': 'PropertyValue', name: 'Type', value: fm.type || 'ingredient' },
      { '@type': 'PropertyValue', name: 'Aroma', value: aroma || '' },
    ],
  });
}

const dataset = {
  '@context': 'https://schema.org',
  '@type': 'Dataset',
  '@id': `${SITE}/data/ingredients.json`,
  name: 'IncenseHub Chinese Botanical Incense Ingredient Encyclopedia',
  description:
    'Machine-readable definitions of the botanical ingredients in the IncenseHub (澜灯) Chinese incense encyclopedia. Chinese terms are the source of truth; English is the agreed translation.',
  url: `${SITE}/data/ingredients.json`,
  publisher: { '@id': `${SITE}/#organization` },
  dateModified: new Date().toISOString().slice(0, 10),
  inLanguage: ['en', 'zh'],
  isAccessibleForFree: true,
  distribution: {
    '@type': 'DataDownload',
    encodingFormat: 'application/json',
    contentUrl: `${SITE}/data/ingredients.json`,
  },
  mainEntity,
};

await writeFile('data/ingredients.json', JSON.stringify(dataset, null, 2) + '\n');
console.log(`Wrote data/ingredients.json with ${mainEntity.length} ingredients.`);
