# Sleep Is the Product

By Parsa Ara. A five-hotel Milwaukee website-information pilot, collected October 29, 2026. What do official hotel pages tell a guest about noise, light control, temperature, bedding and sleep-specific choices before booking?

This repository contains real, source-linked observations, including access failures. It does **not** measure guest sleep, amenity prevalence, clinical effectiveness, willingness to pay, purchases or revenue.

## Run locally

Python 3.9+ is the only requirement. From this repository:

```sh
python3 scripts/run.py
```

Open http://127.0.0.1:8783. This builds the static site, validates its data, and starts a loopback server. Stop with Ctrl-C. Use `--port 8784` if needed. No package installation, credentials or network request is needed to build or run it.

To build and check without a server:

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/check_site.py
```

Serve `site/` on any static host. Relative URLs support a GitHub Pages repository subpath. The committed generated site includes all records, source links and downloads; JavaScript adds domain focus and an evidence inspector. Property records remain manually expandable without JavaScript.

## What is complete

- Protocol and a fixed 30-name purposive candidate panel committed before coding (initial local protocol commit `570a88c`, preserved as [a patch](evidence/protocol-initial-commit.patch); discovery had already begun, so this is not preregistration).
- Five pilot properties: Aloft, Ambassador, Best Western Plus Milwaukee Airport, Brewhouse and Cambria. The remaining 25 candidate rows are uncollected, with eligibility checks pending.
- 25 property-domain rows; 13 official URL records, including failed attempts; short excerpts, locators, retrieval window, access depth and rationales.
- Three verified primary research records with actual reading depth: Frontiers full text, Robbins abstract/metadata plus indexed sections (direct full text unavailable), and Chen publisher abstract only (paywalled).
- Data dictionary, methods, access log, sensitivity note, curated evidence-note checksums and supplementary HTTPS response diagnostics.
- Responsive static website with accessible text labels, keyboard-operable controls, downloadable CSV/JSON and progressive enhancement.

The primary table has **1 specific**, **2 vague**, **12 not stated** and **10 not accessible** cells. These categories describe this bounded review, not hotel quality. Brewhouse's quiet-hours policy is the one specific claim under this rubric; it is not independent proof of a quiet room.

## Read the evidence

- [Prospective coding protocol](docs/protocol.md)
- [Methods, limitations and sensitivity](docs/methods.md)
- [Access log](docs/access-log.md)
- [Data dictionary](docs/data-dictionary.md)
- [25 observations, CSV](data/observations.csv)
- [Official source manifest](data/sources.json)
- [Primary literature evidence table](data/literature.json)
- [30-name candidate panel](data/candidate-panel.csv)
- [Progress and next work](PROGRESS.md)

Source notes in `evidence/*.json` are curated excerpts and access records, not whole-page snapshots. SHA-256 hashes protect saved file integrity, not the truth of hotel claims. Initial web retrieval times are retained honestly as a session interval (18:55–19:01 UTC), not invented exact timestamps. `logged_at_utc` is note logging time. Website text may be cached. A separately timestamped ordinary HTTPS diagnostic is in `evidence/http-access-recheck.json`; it neither updates coding nor validates page content.

## Reproduce and extend

Edit the authoritative JSON/CSV evidence tables, retaining source IDs and a dated protocol amendment when definitions change. Rebuild and validate. Do not automatically convert search results into claims or inaccessible cells into “not stated.” `scripts/build.py` regenerates counts and website artifacts from these tables; it does not pretend to automate judgment-based coding.

An optional ordinary public-URL access check is available:

```sh
python3 scripts/recheck_sources.py
```

It writes diagnostics under ignored `work/`, uses ordinary certificate validation, saves no credentials, and does not change observations. Do not use an HTTP 200 alone as evidence that a dynamic room panel was read.

## Publication

The human confirmed GitHub and GitHub Pages on October 29, 2026. The connected GitHub identity was freshly verified as `parsaara01-stack`. The intended new repository name is `sleep-is-the-product`. The separate public repository has been created at https://github.com/parsaara01-stack/sleep-is-the-product. Source upload and Pages activation are in progress. No successful CI run or public site URL is claimed until verified.

The checked-in `.github/workflows/pages.yml` builds and validates before deployment. Once the new public repository exists and the local commits are pushed, set Settings → Pages → Source to GitHub Actions. The workflow follows [GitHub's official Pages instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). Do not claim deployment until its workflow and public URL are verified.

No hotel/participant contact, paid access or participant recruitment occurred. No changes were made to the existing Adobe Portfolio site or sibling studies. Hotel text belongs to its respective rights holders; no license to hotel imagery or full website content is implied.
