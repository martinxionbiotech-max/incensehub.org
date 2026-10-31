import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const ingredients = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/ingredients' }),
  schema: z.object({
    title: z.string(),
    entity: z.string(),
    chinese: z.string(),
    pinyin: z.string(),
    scientificName: z.string(),
    type: z.string(),
    aroma: z.array(z.string()),
    status: z.string(),
    related: z.array(z.string()).optional(),
    primary_keyword: z.string().optional(),
    search_intent: z.string().optional(),
    last_reviewed: z.string().optional(),
  }),
});

const concepts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/concepts' }),
  schema: z.object({
    title: z.string(),
    entity: z.string(),
    type: z.string(),
    status: z.string(),
    primary_keyword: z.string().optional(),
    search_intent: z.string().optional(),
    last_reviewed: z.string().optional(),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    primary_keyword: z.string(),
    search_intent: z.string(),
    pillar: z.string(),
    content_type: z.string(),
    cluster_role: z.string().optional(),
    last_reviewed: z.string(),
    brand: z.string().optional(),
    author: z.string().optional(),
  }),
});

export const collections = { ingredients, concepts, blog };
