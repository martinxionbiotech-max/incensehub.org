// 自动更新 llms.txt：blog 指南全量列表 + Machine-readable data 段。
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';

const llms = readFileSync('public/llms.txt', 'utf8');

function parseTitle(text, fallback) {
  const m = text.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!m) return fallback;
  const t = m[1].match(/^title:\s*"?(.*?)"?\s*$/m);
  return t ? t[1].replace(/\\"/g, '"').trim() : fallback;
}

// 全量 blog 指南列表（此前 llms.txt 只有 blog 索引，115 篇正文不可发现）。
const blogDir = 'src/content/blog';
const blogLines = readdirSync(blogDir)
  .filter((f) => f.endsWith('.md'))
  .map((f) => {
    const slug = f.replace(/\.md$/, '');
    const title = parseTitle(readFileSync(`${blogDir}/${f}`, 'utf8'), slug);
    return `- [${title}](/blog/${slug}/)`;
  })
  .sort((a, b) => a.localeCompare(b, 'en'));

const blogSection = `## Blog & Guides\n\n${blogLines.join('\n')}`;

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

const dataLines = datasets.map(({ file, label, noun }) => {
  const { n, edges } = count(file);
  const num = edges !== undefined ? `${n} / ${edges}` : `${n}`;
  return `- [${label}](https://data.incensehub.org/datasets/${file}): ${num} ${noun} (Schema.org Dataset / DefinedTerm).`;
});
const dataSection = `## Machine-readable data\n\n${dataLines.join('\n')}`;

let out = llms;

// 替换已有 Blog & Guides 段，或在 Machine-readable data 前插入。
const BLOG_RE = /## Blog & Guides[\s\S]*?(?=\n## |$)/;
if (BLOG_RE.test(out)) {
  out = out.replace(BLOG_RE, () => blogSection + '\n');
} else {
  out = out.replace('## Machine-readable data', () => blogSection + '\n\n## Machine-readable data');
}

// 替换 Machine-readable data 段（保留后续小节）。
const DATA_RE = /## Machine-readable data[\s\S]*?(?=\n## |$)/;
if (!DATA_RE.test(out)) {
  console.error('未找到 Machine-readable data 段，跳过');
  process.exit(1);
}
out = out.replace(DATA_RE, () => dataSection + '\n');

writeFileSync('public/llms.txt', out);
console.log(`llms.txt 自动更新: ${blogLines.length} blog guides, ${dataLines.length} datasets`);
