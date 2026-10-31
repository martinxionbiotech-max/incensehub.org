# Internal Link Map — Hub → Spoke → Cross-Link Status

> Audit-only. Built from `scripts/orphan_inbound.json` (252 mapped URLs: 97 blog + 151 ingredient entries + 4 core pages) and the nav/footer templates.

## Global topology

| Metric | Value |
|---|---|
| URLs mapped | 252 |
| ≥ 2 inbound links | 176 (69.8%) |
| = 1 inbound link | 39 |
| = 0 inbound links (orphans) | 37 |
| Ingredient pages mapped | 151 (150 files + 1 empty-slug artifact) |
| Blog pages mapped | 97 |

## Hub → spoke structure (actual)

**Site-wide nav** (header, `BaseLayout.astro`): Home · Ingredients · Wholesale · OEM · Contact.

**Footer:** adds Chinese Incense, Ingredients, Wholesale, OEM, Contact + "Machine-readable resources" (Knowledge map, Ingredient dataset link).

**Pillar hubs** (13, one per cluster — see `topic-map.md`): each hub links out to its spokes and back; spokes link to hub via contextual anchors + breadcrumbs.

**Entity hub:** `/ingredients/` (CollectionPage + ItemList schema) links to all 150 entity pages.

## Entity ↔ Entity cross-links (current state)

The `related[]` frontmatter field exists on 150/150 entities and is rendered as contextual links on entity pages. The data-site `relationships.json` holds a richer typed layer (450 edges across 150 entities: category/aroma/…).

**Top cross-linked entities (inbound internal links):**

| Entity | Inbound | Entity | Inbound |
|---|---|---|---|
| sandalwood | 12 | cedar | 9 |
| jasmine | 12 | rose | 9 |
| osmanthus | 12 | benzoin | 8 |
| cinnamon | 11 | plum-blossom | 8 |
| mugwort | 11 | agarwood | 7 |
| frankincense | 10 | orange-peel | 7 |
| agastache-rugosa | 10 | borneol | 7 |
| clove | 10 | pine-resin / galangal / fennel | 7 each |

## Orphan pages (0 inbound links) — 37 total

**1 blog orphan:** `/blog/incense-export-considerations/`

**36 ingredient orphans:**

`aglaia, amber, apricot-kernel, asarum, banksia-rose, beeswax, bletilla, castoreum, copaiba, cyperus, daphne, dill, elsholtzia, eucalyptus, fenugreek, galbanum, ginkgo, grapefruit, lily-of-the-valley, mastic, mustard, nutmeg, onycha, orchid, oxyphylla, paicao, prickly-ash, quince, rue, schisandra, shellac, silk-tree, tree-peony-bark, valerian, violet, ylang-ylang`

### Orphan severity flags

- **Classical-core orphans (high priority for repair):** `amber` (琥珀), `onycha` (甲香), `castoreum` (海狸香), `shellac` (紫草茸), `civet` (灵猫香, 1 inbound) — the animal/mineral fixative family is nearly un-linked despite classical importance.
- **False-friend / name-drift entities (need disambiguation links):** `quince` (木瓜), `oxphylla` (益智仁), `katsumadai` (草豆蔻) — these carry naming-trap content that should cross-link to their "true" counterpart entities.

## Link-map integrity notes

1. **Empty-slug artifact:** the map contains one ingredient entry with an empty slug (trailing-slash link bug) → 151 entries for 150 files. Fix in the linking phase.
2. **No reciprocal-link enforcement:** `related[]` is directional and not guaranteed symmetric; the 450-edge dataset layer is more complete than the frontmatter layer.
3. **Comparison cross-links:** present (agarwood↔sandalwood, stick↔cone, incense↔candles) but sparse — comparison intent is concentrated in P7, not yet cross-linked into entity pages systematically.

## Anchor-text observations

- Contextual, entity-name anchors dominate (no "click here", no "Related Posts" keyword-stuffing).
- Breadcrumb + hub + spoke + comparison pattern is followed; the main deficit is **coverage** (36 entities + 1 blog with no inbound path), not anchor quality.
