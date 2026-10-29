# Data dictionary

All JSON and CSV files use UTF-8. Missing quotations are empty strings, not zeros. Category names are non-ordinal.

## observations.json / observations.csv

One row per property × domain. Exactly 25 initial rows, no participants.

| Field | Definition |
|---|---|
| observation_id | Unique property-domain key |
| property_id | Join to properties.json and candidate_id in candidate-panel.csv |
| domain | noise, light, temperature, bedding, choice |
| status | specific, vague, not_stated, not_accessible; defined in protocol |
| evidence_excerpt | Short verbatim evidence; empty for negative search results/access failures |
| source_ids | List of reviewed source IDs (semicolon-delimited in CSV) |
| locator | Human-readable page section; generic review scope for non-positive cells |
| rationale | Why the statement meets or does not meet the rule |
| scope | Claim scope; not a guarantee for every room |
| access_caveat | Retrieval or interpretation limitation |
| observed_window_start_utc / observed_window_end_utc | Retrieval session interval; not exact per-page fetch time |
| coder | Initial coding arrangement; no independent adjudication |
| protocol | Version of prospective coding rules |

## sources.json and evidence/*.json

source_id is unique. property_id identifies the hotel. title and url identify the official page. access_depth is page_text, page_text_partial, unavailable, or unavailable_index_lead. delivery indicates a potentially cached web extractor. access_note explains limits. evidence_excerpt and locator retain the short relevant text and its section. retrieval_window fields give honest timestamp precision; logged_at_utc is record creation, not source publication or fetch time. An evidence file is an exact copy of its source record. evidence/sha256sums.txt hashes the curated records, not hotel HTML. No full copyrighted pages are redistributed.

## properties.json

property_id, name, short_name, address, source_ids, access and eligibility describe the five pilot properties. Addresses are official-page labels (Cambria index-only); municipal eligibility is explicitly pending, rather than inferred from a postal address.

## candidate-panel.csv

candidate_id is a stable panel ID. name is a candidate hotel. stage is pilot or target_uncollected. eligibility remains verification_pending until municipal and current-operation checks are complete. selection_note records the fixed purposive selection rule. The uncollected rows contain no amenity codes.

## literature.json

id, authors, year, title, doi and url identify primary research. fulltext_url is supplied where relevant. access and access_note distinguish full text from abstract/index-only readings. design, use, limitations and measurement_window summarize the verified scope without extrapolating to causal effects. Retrieval/logging fields follow sources.json.

## summary.json (generated)

pilot_properties, target_candidates, observations and source_urls are counts, not outcome measures. overall and by_domain contain four separate status counts. Denominator is five per domain, 25 overall. claim_quality_sensitivity states the single documented alternative. source/data checksums are generated at build time in site/downloads/checksums.sha256.

## evidence/http-access-recheck.json

Supplementary diagnostics, separate from the coded retrieval session. started_at_utc and completed_at_utc are exact log times; method describes normal HTTPS GET. http_status, final_url, response_bytes, content_type and sha256_response_bytes are present on success. error is present on failure. limit_bytes documents the response read cap. coding_changed is always false. HTTP success does not establish full page-content access or an amenity claim.

## v1.1 added fields

`disclosure_status` separates specific/vague/not_found_in_review/undetermined from original `status`. `access_coverage` is partial, unavailable or reviewed_text_only; the latter does not certify completed browser review. `verification_status` is not_independently_verified. `claim_type` identifies the three positive examples or no_classified_claim. `actionability` is not_evaluated. Original v1 status is retained for historical comparability. `study.json` controls version, public dates, repository URL and citation.
