// Ingredient entity markdown variant — data-driven from the ingredients
// content collection + the ingredients dataset (data/ingredients.json).
// Mirrors src/pages/ingredients/[slug].astro (same data source, same slug).
import { getCollection } from 'astro:content';
import ingredientsDataset from '../../../data/ingredients.json';
import { SITE_URL, frontmatter, cell, mdTable, mdResponse } from '../../lib/markdown';

interface DatasetEntity {
  termCode?: string;
  additionalProperty?: { name?: string; value?: unknown }[];
  sources?: { title?: string; url?: string; evidenceLevel?: string }[];
}

export async function getStaticPaths() {
  const ingredients = await getCollection('ingredients');
  return ingredients.map((ingredient) => ({
    params: { slug: ingredient.id },
    props: { id: ingredient.id, data: ingredient.data },
  }));
}

export function GET({ props }: { props: { id: string; data: any } }) {
  const { id, data } = props;
  const { title, chinese, pinyin, scientificName, type, aroma } = data;
  const aromaText = (aroma || []).join(', ');
  const description = `${chinese} (${pinyin}) is an ${type} from ${scientificName}, with an aroma profile of ${aromaText}.`;
  const canonical = `${SITE_URL}/ingredients/${id}/`;
  // Dataset-level last-modified date — the entity record is derived from this
  // dataset, so its dateModified is the honest "updated" signal.
  const updated = ingredientsDataset.dateModified;

  const entity: DatasetEntity | undefined = (ingredientsDataset.mainEntity || []).find(
    (e) => e.termCode === id,
  );
  const category = entity?.additionalProperty?.find((p) => p.name === 'Category')?.value;
  const sources = entity?.sources || [];

  const rows: unknown[][] = [
    ['Chinese', chinese],
    ['Pinyin', pinyin],
    ['Scientific name', scientificName],
    ['Type', type],
    ['Aroma', aromaText],
    ...(category ? [['Category', category]] : []),
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
    ...(sources.length > 0
      ? [
          '## Sources',
          '',
          ...sources.map(
            (s) =>
              `- [${cell(s.title)}](${s.url}) — ${cell(s.evidenceLevel)}`,
          ),
          '',
        ]
      : []),
    '## Human-readable page',
    '',
    `[View the full ingredient page](${canonical})`,
    '',
  ].join('\n');

  return mdResponse(md);
}
