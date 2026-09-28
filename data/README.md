# data/

Storage location for speech datasets used in this research. No dataset is
downloaded or committed yet.

- `raw/` — original, unmodified audio/transcript files as obtained from a
  source dataset. Never edited in place.
- `processed/` — derived artifacts (resampled audio, cleaned transcripts,
  extracted feature tables) produced deterministically from `raw/`.
- `external/` — third-party reference data that isn't a primary dataset
  (e.g. lexical norm lists, pretrained embedding vocabularies).

All contents of these folders (except `.gitkeep`) are gitignored. Datasets
involving human subjects (e.g. Parkinson's speech corpora) typically carry
usage/licensing restrictions, so raw data must never be committed to
version control. When a dataset is added, document its source, license,
and access conditions here.
