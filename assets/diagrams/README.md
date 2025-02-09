# Original teaching figures

[Visual guide](../../docs/visual-guide.md) · [All questions](../../README.md)

The 32 SVG files are static images with local relative links, accessible titles and descriptions, and no scripts, external resources, or remote fonts. They are original illustrations for this repository and follow its license.

Seven figures use explicit illustrative numbers: critical path, forecast distribution, capacity, earned value, burnup/burndown, cumulative flow, and an error budget. These are worked examples, not industry results or benchmark targets. The forecast uses a deterministic random seed and states its input history in the generator.

Regenerate with `python scripts/generate_visuals.py` from the repository root. Use [requirements-visuals.txt](../../scripts/requirements-visuals.txt). Add `--preview-dir <directory>` to produce PNG previews outside the source assets. The renderer uses Segoe UI on Windows or DejaVu Sans elsewhere; text bounds are checked during generation.

[manifest.json](manifest.json) records titles, descriptions, dimensions, and the answer associated with every figure. Each answer supplies conceptual references and explains applicability.
