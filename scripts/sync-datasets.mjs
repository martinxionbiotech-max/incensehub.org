#!/usr/bin/env node
// 同步权威数据集（../data-landeng/datasets/*.json，唯一源）到主仓 data/ 与
// public/data/，并把数据集计数注入 knowledge-map 页（标记区块内改写）。
//
// 流程：
//   1) 拷贝 8 个 datasets/*.json → data/ + public/data/（md5 校验，输出同步报告）
//   2) 读主仓 data/*.json，注入 knowledge-map 页的 Dataset Map 表（条数 + version）
//      与正文/FAQ 的 terminology 计数（<!-- AUTO:dataset-counts:... --> 标记区内）
//
// 幂等：重复运行得到相同结果。数据站 data-landeng 是唯一权威源。
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const SRC_DIR = join(__dirname, '..', '..', 'data-landeng', 'datasets');

const DATASETS = [
  { file: 'ingredients.json',   label: 'Ingredient database' },
  { file: 'terminology.json',   label: 'Terminology database' },
  { file: 'aroma.json',         label: 'Aroma database' },
  { file: 'materials.json',     label: 'Material database' },
  { file: 'comparisons.json',   label: 'Comparison database' },
  { file: 'techniques.json',    label: 'Technique database' },
  { file: 'forms.json',         label: 'Form database' },
  { file: 'relationships.json', label: 'Relationships database' },
];

function md5(buf) {
  return createHash('md5').update(buf).digest('hex');
}

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function loadCounts() {
  const counts = {};
  for (const { file } of DATASETS) {
    const data = JSON.parse(readFileSync(join(ROOT, 'data', file), 'utf8'));
    counts[file] = {
      n: Array.isArray(data.mainEntity) ? data.mainEntity.length : 0,
      version: data.version || '',
    };
  }
  return counts;
}

function syncJson() {
  const results = [];
  for (const { file } of DATASETS) {
    const src = join(SRC_DIR, file);
    if (!existsSync(src)) {
      throw new Error(`Missing authoritative source: ${src}`);
    }
    const buf = readFileSync(src);
    const srcHash = md5(buf);
    const statuses = [];
    for (const t of [join(ROOT, 'data', file), join(ROOT, 'public', 'data', file)]) {
      mkdirSync(dirname(t), { recursive: true });
      writeFileSync(t, buf);
      statuses.push(md5(readFileSync(t)) === srcHash ? 'OK' : 'MISMATCH');
    }
    results.push({ file, srcHash: srcHash.slice(0, 8), data: statuses[0], publicData: statuses[1] });
  }
  return results;
}

function injectKnowledgeMap() {
  const path = join(ROOT, 'src', 'content', 'blog', 'lanDeng-knowledge-map.md');
  let text = readFileSync(path, 'utf8');
  const counts = loadCounts();

  // 1) Dataset Map 表（8 行，条数 + version）
  const rows = DATASETS.map(({ file, label }) => {
    const c = counts[file];
    return `| ${label} | \`https://data.incensehub.org/datasets/${file}\` | ${c.n} | ${c.version} |`;
  });
  const table = `| Dataset | JSON path | Entities | Version |\n|---|---|---|---|\n${rows.join('\n')}`;
  const tableOpen = '<!-- AUTO:dataset-counts:table -->';
  const tableClose = '<!-- /AUTO:dataset-counts:table -->';
  const tableRe = new RegExp(escapeRegex(tableOpen) + '[\\s\\S]*?' + escapeRegex(tableClose));
  if (!tableRe.test(text)) {
    throw new Error(`knowledge-map: missing ${tableOpen} marker`);
  }
  text = text.replace(tableRe, `${tableOpen}\n${table}\n${tableClose}`);

  // 2) terminology 计数（正文 + FAQ，全局替换，可能多处）
  const term = counts['terminology.json'].n;
  const termOpen = '<!-- AUTO:dataset-counts:terminology-terms -->';
  const termClose = '<!-- /AUTO:dataset-counts:terminology-terms -->';
  const termRe = new RegExp(escapeRegex(termOpen) + '\\d+' + escapeRegex(termClose), 'g');
  const occurrences = (text.match(termRe) || []).length;
  if (occurrences === 0) {
    throw new Error(`knowledge-map: missing ${termOpen} marker`);
  }
  text = text.replace(termRe, `${termOpen}${term}${termClose}`);

  writeFileSync(path, text);
  return { termValue: term, termOccurrences: occurrences };
}

const sync = syncJson();
const km = injectKnowledgeMap();

console.log('sync-datasets.mjs — source = ../data-landeng/datasets/ (authoritative)');
for (const r of sync) {
  console.log(`  ${r.file}: src=${r.srcHash}  data=${r.data}  public/data=${r.publicData}`);
}
const ok = sync.filter((r) => r.data === 'OK' && r.publicData === 'OK').length;
console.log(`  ${ok}/8 md5 match authoritative source`);
console.log(`knowledge-map: Dataset Map table injected; terminology-terms x${km.termOccurrences} -> ${km.termValue}`);
