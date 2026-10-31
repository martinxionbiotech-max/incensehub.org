// 自动更新 llms.txt 的 Machine-readable data 段（数据来自 data/*.json 权威源）
import { readFileSync, writeFileSync } from 'node:fs';

const llms = readFileSync('public/llms.txt', 'utf8');

const datasets = [
  { file: 'ingredients.json', label: 'Ingredient dataset', noun: 'ingredient entities' },
  { file: 'terminology.json', label: 'Terminology dataset', noun: 'Chinese–English incense terms' },
  { file: 'relationships.json', label: 'Relationship dataset', noun: 'entity records (typed edges)' },
  { file: 'comparisons.json', label: 'Comparison dataset', noun: 'comparison profiles' },
  { file: 'materials.json', label: 'Material dataset', noun: 'functional materials' },
  { file: 'forms.json', label: 'Form dataset', noun: 'incense forms' },
  { file: 'techniques.json', label: 'Technique dataset', noun: 'incense techniques' },
  { file: 'aroma.json', label: 'Aroma dataset', noun: 'aroma families' },
];

function count(file) {
  const d = JSON.parse(readFileSync(`data/${file}`, 'utf8'));
  const n = Array.isArray(d.mainEntity) ? d.mainEntity.length : 0;
  if (file === 'relationships.json') {
    let edges = 0;
    if (Array.isArray(d.mainEntity)) {
      for (const rec of d.mainEntity) edges += Array.isArray(rec.relatedEntity) ? rec.relatedEntity.length : 0;
    }
    return { n, edges };
  }
  return { n };
}

const lines = datasets.map(({ file, label, noun }) => {
  const { n, edges } = count(file);
  const num = edges !== undefined ? `${n} / ${edges}` : `${n}`;
  return `- [${label}](https://data.incensehub.org/datasets/${file}): ${num} ${noun} (Schema.org Dataset / DefinedTerm).`;
});

const section = `## Machine-readable data\n\n${lines.join('\n')}`;

const SECTION_RE = /## Machine-readable data[\s\S]*?(?=\n## |\n\n## |$)/;
if (!SECTION_RE.test(llms)) {
  console.error('未找到 Machine-readable data 段，跳过');
  process.exit(1);
}
const out = llms.replace(SECTION_RE, section.trim() + '\n');
writeFileSync('public/llms.txt', out);
console.log(`llms.txt 自动更新: ${lines.length} datasets`);
