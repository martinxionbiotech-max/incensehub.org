// Chinese incense pillar markdown variant — the single concepts-collection entry
// rendered at /chinese-incense/. Mirrors src/pages/chinese-incense/index.astro.
import { getEntry } from 'astro:content';
import { SITE_URL, frontmatter, mdTable, mdResponse } from '../lib/markdown';

export async function GET() {
  const concept = await getEntry('concepts', 'chinese-incense');
  const { title, type, primary_keyword, search_intent } = concept.data;
  // Same meta description as the HTML page.
  const description =
    'What Chinese incense is, its history, the Four Leisure Arts, and the way of incense (香道).';
  const canonical = `${SITE_URL}/chinese-incense/`;
  // Last content edit (no date field on the concepts schema — sourced from git history).
  const updated = '2026-09-28';

  const rows: unknown[][] = [
    ['Type', type],
    ['Primary keyword', primary_keyword],
    ['Search intent', search_intent],
  ];

  const md = [
    frontmatter({ title, description, canonical, updated }),
    `# ${title}`,
    '',
    description,
    '',
    '## Key facts',
    '',
    mdTable(['Field', 'Value'], rows),
    '',
    '## Human-readable page',
    '',
    `[View the full page](${canonical})`,
    '',
  ].join('\n');

  return mdResponse(md);
}
