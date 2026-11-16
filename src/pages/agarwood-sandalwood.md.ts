// Agarwood & Sandalwood pillar markdown variant — rendered at /agarwood-sandalwood/.
import { getEntry } from 'astro:content';
import { SITE_URL, frontmatter, mdTable, mdResponse } from '../lib/markdown';

export async function GET() {
  const concept = await getEntry('concepts', 'agarwood-sandalwood');
  const { title, type, primary_keyword, search_intent } = concept.data;
  const description =
    "A buyer's field guide to agarwood and sandalwood: species, resin formation, grading, authentication, CITES rules, and the four components of price.";
  const canonical = `${SITE_URL}/agarwood-sandalwood/`;
  const updated = '2026-11-17';

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
