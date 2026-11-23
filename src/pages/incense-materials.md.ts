// Incense Materials pillar markdown variant — rendered at /incense-materials/.
import { getEntry } from 'astro:content';
import { SITE_URL, frontmatter, mdTable, mdResponse } from '../lib/markdown';

export async function GET() {
  const concept = await getEntry('concepts', 'incense-materials');
  const { title, type, primary_keyword, search_intent } = concept.data;
  const description =
    'A field guide to incense materials: identity, form, grade, treatment, and the tests that separate a real material claim from a label.';
  const canonical = `${SITE_URL}/incense-materials/`;
  const updated = '2026-11-24';

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
