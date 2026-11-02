import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Remove HTML comment nodes that are AUTO:* injection markers (used by
// scripts/sync-datasets.mjs in the knowledge-map page) so they never leak
// into the rendered HTML.
function stripAutoMarkers() {
  return (tree) => {
    const walk = (node) => {
      if (!node || typeof node !== 'object') return;
      if (Array.isArray(node.children)) {
        node.children = node.children.filter((child) => {
          const isAutoMarker =
            child &&
            child.type === 'html' &&
            /^<!--\s*\/?AUTO:/.test(child.value || '');
          if (!isAutoMarker) walk(child);
          return !isAutoMarker;
        });
      }
    };
    walk(tree);
  };
}

// TODO: replace with the production domain before launch.
export default defineConfig({
  site: 'https://incensehub.org',
  output: 'static',
  integrations: [
    sitemap({
      // Keep noindex landing pages out of the sitemap.
      filter: (page) =>
        !new Set([
          '/private-label/',
          '/oem/',
          '/wholesale/',
          '/contact/',
          '/request-a-quote/',
          '/incense-manufacturer/',
        ]).has(new URL(page).pathname),
    }),
  ],
  markdown: {
    remarkPlugins: [stripAutoMarkers],
  },
});
