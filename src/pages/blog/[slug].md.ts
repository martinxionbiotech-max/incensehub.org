// Blog guide markdown variant — data-driven from the blog content collection.
// Mirrors src/pages/blog/[slug].astro (same slug + meta-description derivation).
import { getCollection } from 'astro:content';
import { SITE_URL, frontmatter, cell, mdTable, mdResponse } from '../../lib/markdown';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map((post) => {
    // Same meta-description derivation as the HTML page (unique, from body).
    const description =
      (post.body || '')
        .replace(/<[^>]+>/g, ' ')
        .replace(/[#*_>`\[\]()!-]/g, ' ')
        .replace(/\s+/g, ' ')
        .trim()
        .slice(0, 155) || post.data.title;
    return {
      params: { slug: post.data.slug },
      props: { data: post.data, description },
    };
  });
}

export function GET({ props }: { props: { data: any; description: string } }) {
  const { data, description } = props;
  const { title, primary_keyword, search_intent, pillar, content_type, last_reviewed, author, brand } = data;
  const canonical = `${SITE_URL}/blog/${data.slug}/`;

  const clean = (v: unknown) => String(v ?? '').replace(/^"+|"+$/g, '');

  const rows: unknown[][] = [
    ['Primary keyword', primary_keyword],
    ['Search intent', search_intent],
    ['Pillar', pillar],
    ['Content type', content_type],
    ...(author ? [['Author', clean(author)]] : []),
    ...(brand ? [['Brand', clean(brand)]] : []),
  ];

  const md = [
    frontmatter({ title, description, canonical, updated: last_reviewed }),
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
    `[View the full guide](${canonical})`,
    '',
  ].join('\n');

  return mdResponse(md);
}
