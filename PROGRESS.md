# Dataset v1.1 revision — October 29, 2026

The disclosure audit now separates access coverage from original coding, uses clearer negative labels, and generates the public version/counts/dates from data. Original collection and codes are preserved. See [revision record](docs/revision-and-verification.md) and [prospective v2 collection protocol](docs/protocol-v2.md). Independent coding, municipal eligibility and recollection remain pending. Earlier milestone notes below describe v1.

# Progress — October 29, 2026

Author: Parsa Ara. Stage: protocol-led, five-hotel website-information pilot. The initial local research milestone is built and tested. Published at https://parsaara01-stack.github.io/sleep-is-the-product/ with a separate public source repository and a verified successful first build/deployment.

## Completed

- Fixed the question, five-domain rubric, access states, bounded search and non-ranking analysis before coding. Initial discovery was already underway; no preregistration claim.
- Committed the protocol and 30-name purposive candidate panel before the coded table (`570a88c`). The first five alphabetically named candidates form the pilot. Kept inaccessible properties rather than replacing them.
- Reviewed official pages for five hotel records and documented 13 URL attempts, with source locators, short excerpts, access depth, a retrieval session window and per-cell rationale.
- Created 25 actual coded information/access observations: 1 specific, 2 vague, 12 not stated, 10 not accessible. These are not amenity-presence codes or hotel-quality scores.
- Verified three primary research records. One publisher full text was read; two records have abstract/index/metadata limits. No causal or revenue inference.
- Saved curated source notes and SHA-256 checksums. Ran a supplementary ordinary HTTPS access check with exact timestamps and response hashes on success, without changing coding.
- Built a responsive, dependency-free static site with a question-focused matrix, evidence inspector, full static property records, methods, literature and CSV/JSON downloads.
- Prepared a GitHub Pages Actions workflow using current official GitHub documentation. Confirmed the connected account as parsaara01-stack after the human selected GitHub hosting.

## Validation performed

- `python3 scripts/build.py` and `python3 scripts/validate.py`: pass. Checks include the 30/5 sample, first-five selection rule, unique keys, five domains per hotel, positive-claim provenance, access-state safeguards, short-quote limits, note checksums, CSV/JSON parity, denominator counts and generated-site parity.
- `python3 scripts/check_site.py --base-url http://127.0.0.1:8783`: pass. All 15 linked local routes/assets/downloads returned HTTP 200; one h1, unique IDs and all fragment targets present.
- JavaScript syntax check with the bundled Node runtime: pass.
- Browser checks: desktop rendering inspected; all four evidence states open the matching inspector. Domain focus correctly updates counts. Keyboard Space activates a focus button; Enter opens evidence and transfers focus to the inspector.
- 390 × 844 viewport: no page-wide horizontal overflow; the wide table scrolls within its region and alternative full records are available. Viewport override reset after testing.
- Browser warning/error log empty during the observed tests. This is functional and visual QA, not a full assistive-technology accessibility audit.

## Material limits

- Only five properties; fixed purposive sample; no population inference. Twenty-five target candidates remain uncollected. Postal addresses do not independently verify municipal boundaries; eligibility and operating-status confirmation remain work for expansion.
- Aloft room-detail cards/answers were incompletely exposed. Cambria pages failed direct access, including browser/Python TLS failures. Ten cells are inaccessible, not negative findings. Some text is potentially cached.
- Not stated means no qualifying statement in reviewed text, not “the hotel lacks it.” Specific means concrete wording, not verified implementation. No guest slept in a studied room for this project.
- Single AI-assisted initial coder; no independent adjudication/reliability estimate. Initial web timestamps are honestly recorded as a session interval, with logging time separate.
- Primary paper access limits prevent claiming a full-text literature review. The guest-choice domain is investigator-defined.

## Publication verified

- Public source: https://github.com/parsaara01-stack/sleep-is-the-product
- Live pilot: https://parsaara01-stack.github.io/sleep-is-the-product/
- First successful build/deployment: https://github.com/parsaara01-stack/sleep-is-the-product/actions/runs/40939597426
- Public homepage, data/pilot.json and observations CSV returned HTTP 200. The public JSON contains five properties and 25 observations. Live domain counts and evidence-inspector behavior were verified in the browser, with no observed warnings/errors.
- GitHub Actions is the Pages source. The permanent workflow runs build, integrity and static-route checks before deployment. A one-time archive expansion was used because connector writes were denied; the repository now has readable source files and the normal workflow.
- Original local research commits are preserved on local-pilot-history. The initial protocol patch is public. Local main follows the remote history; no public preregistration claim.

## Next actions

1. Retry inaccessible room detail under the same documented scope and record any revision as a new review, rather than silently overwriting access history.
2. Obtain independent double-coding of the 25 cells, adjudicate with source text, then verify current operation and municipal eligibility for the 30 candidates before expansion.
3. Prepare a separate protocol for any partner/guest comprehension or room-condition validation. No recruitment, partner contact, payments or guest outcome data collection has begun.
