# TACITUS engineering review — November 7, 2026

This review separates reproducible local behavior, source implementation and
deployed acceptance. Changes described below belong to a November 7 review
checkpoint; an open pull request is not a production release.

The portfolio inventory covered 72 owned repositories through metadata,
default-branch root paths and available READMEs. Twenty are archived and eighteen
are forks, including archived forks. The detailed private inventory stays local.
Deep code changes in this checkpoint cover the Tacitus website, Praxis context
selection and the public Knowledge Pipeline example. Other repositories have not
all been built or reviewed line by line.

## Thirty improvements and their acceptance criteria

| # | Improvement | Checkpoint status / acceptance |
| --- | --- | --- |
| 1 | Inventory the complete portfolio and distinguish archived work, forks and current products. | Local inventory completed; reusable public-only audit script added. Five verified archive candidates are blocked by the integration's missing Administration write permission. |
| 2 | Make runnable projects visible from the Tacitus homepage. | Added a catalog link in the existing Engineering section while preserving the newer working-tools lead and paused-workspace status. |
| 3 | Keep a single project catalog across website sections. | Shared eight-project catalog implemented. |
| 4 | Remove implementation claims for the empty archived ontology repository. | Removed from the active website catalog. |
| 5 | Add current Workbench, Middle East source-kit and TCGC entry points. | Catalog entries include scope and repository rights. |
| 6 | Give visitors three concrete local workflows with prerequisites. | Commands, Python virtual environments and guides implemented. |
| 7 | Replace fictional SDK calls with a real source-kit build. | Documented build ran successfully on current source. |
| 8 | Make command displays readable and keyboard accessible on narrow screens. | Focusable scrolling code displays implemented; visual browser acceptance remains open. |
| 9 | Match search metadata to the current developer page. | Website metadata updated. |
| 10 | Verify the Cloudflare database rather than infer readiness from DNS. | Authenticated read-only queries succeeded; counts matched snapshot metadata. |
| 11 | Keep the existing private dataset boundary when connecting Praxis. | Admin-only server adapter implemented; ordinary/sample users rejected. |
| 12 | Authenticate server-to-server reads through the existing Access application. | Access-header adapter implemented; deployment credentials/policy still required. |
| 13 | Bound dataset request paths, filters, response size and waiting time. | Allowlists, duplicate checks, stream byte bound and timeout implemented. |
| 14 | Refuse redirects and login HTML rather than report them as a successful connection. | Protocol validation and redirect refusal implemented. |
| 15 | Preserve snapshot identity and distinguish D1 from local/static data. | Versioned envelope checks implemented; no silent fallback. |
| 16 | Avoid leaking service credentials or upstream diagnostics. | Credentials stay in server headers; errors are sanitized and responses private/no-store. |
| 17 | Exclude retrieved graph edges when their endpoint nodes were omitted. | Retrieval correction and regression test implemented. |
| 18 | Continue looking for useful evidence after an oversized record. | All retrieval layers now consider later fitting records. |
| 19 | Select vector evidence by relevance. | Score ordering and stable tie-break implemented. |
| 20 | Avoid spending the context budget on duplicate vector chunks. | Chunk deduplication implemented. |
| 21 | Account for source metadata when budgeting retrieval. | Whole serialized rows counted using the existing token heuristic; not an exact tokenizer guarantee. |
| 22 | Fill remaining context slots after primitive coverage has been preserved. | Coverage refill and deterministic ranking implemented. |
| 23 | Make omission receipts describe the records actually omitted. | Edge eligibility and ranked-source receipts corrected. |
| 24 | Provide policy-context and real-source semantic examples anyone can run without credentials. | Standard-library Python examples added to Knowledge Pipeline open: four lenses and five recurring task recipes. |
| 25 | Require exact source quotation links in the example. | Missing sources, invented quotes and duplicate IDs rejected. |
| 26 | Preserve review state and temporal applicability before using claims. | Unreviewed, expired and future claims have explicit omission reasons. |
| 27 | Keep comparison claims together under a constrained budget. | Whole comparison groups retained or omitted; inapplicable counterparts explicitly reported. |
| 28 | Produce reproducible context receipts and enforce the complete packet's byte budget. | Input/packet digests, every omission and UTF-8 byte accounting implemented, with CI. |
| 29 | Prove a deployed, authenticated dataset-to-capsule-to-answer journey. | Remaining: mount scoped Access credentials in the existing Cloud Run service, verify the route, then integrate through reviewed capsule proposals. No live integration claim yet. |
| 30 | Measure whether capsules improve policy analysis, and reconcile linked app availability. | Remaining: matched sources/model/questions, retained generated answers, citation fidelity, analyst review, latency and cost. Access errors on linked app hosts require service-specific diagnosis before calling those apps available. |

## Reproduce the checks

```bash
# Public metadata/root review; no remote writes or model calls
python scripts/audit_portfolio.py --owner sargonxg --output /tmp/public-portfolio.md

# Separate reference repository; Python 3.10+, no dependencies or API keys
git clone https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open.git
cd TACITUS-Knowledge-Pipeline-open
python examples/context_capsule.py --budget-bytes 4000 --out /tmp/context-packet.json
python -m unittest discover -s tests -v

# Real source wording under a task-specific semantic lens
python examples/political_semantics/semantic_layer.py validate
python examples/political_semantics/semantic_layer.py query --lens mediation
python examples/political_semantics/semantic_layer.py recipes
```

The context example has its own teaching format. It is not a claim of lossless
interchange with PRAXIS or DIALECTICA capsule schemas, and deterministic source
selection does not establish analytical accuracy. Repository commands in this
review become available when their corresponding changes are merged.

The Cloudflare dataset is a historical 2000–2025 selected-country snapshot, not a
live operational feed. R2 is not enabled in the inspected account and is not
required for the read-only D1 adapter. Existing Google Cloud product hosting and
private dataset access remain unchanged by these source changes.

## Repository cleanup

Thirteen older/empty candidates received branch and open-PR checks. Five had
clear successor or empty-repository evidence and no unique work requiring
preservation. GitHub rejected both archive mechanisms because the integration
lacks repository Administration write access; no archive state changed. Eight
were preserved because of open PRs, unique unmerged commits or unclear
successors. No repository, branch or history was deleted.

The private cleanup report retains the exact candidates, original state,
evidence and reversible commands. Credential cleanup is tracked separately;
archiving never substitutes for revoking exposed credentials.

## Political semantics and recurring tasks

The [semantic-layer change](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/pull/5)
adds five source records, eight short retained excerpts and ten typed statements.
Official UN resolution, Geneva communiqué and mediation-guidance excerpts carry
locators and hashes. Short Reuters wording retains the reporting/attribution
chain. ILO material remains a candidate and is excluded from default evidence
queries. All records explicitly lack human approval.

The four lenses are policy analysis, mediation, media/narrative review and HR
policy. Five recipes cover resolution briefs, communiqué comparison, mediation
preparation, media framing and HR applicability review. Publication, occurrence,
validity and recording time remain separate. Endorsement is not implementation;
an attributed position is not proof of motive or media-wide bias. The example
exports JSON-LD 1.1 and a locally tested SQLite schema, without changing the live
D1 snapshot or asserting a measured improvement in generated reasoning.

## Reviewable changes

- [Tacitus developer paths](https://github.com/sargonxg/A2_TACITUS_WEBSITE_NEXTJS2/pull/49): stacked on the existing website redesign; 103 local unit tests and production build passed. Both existing Vercel preview deployments report success; their pages require Vercel sign-in, and visual acceptance remains open.
- [Praxis context and private data boundary](https://github.com/sargonxg/A4_PRAXIS_CLOUD_Work/pull/40): 32 focused tests and remote verify/credential checks passed. The authenticated-persona lane failed at the existing context-readiness test's conversation-create fetch, with a separate descendant-cleanup error. The underlying browser error was not retained in the bounded receipts, so its cause remains unresolved. The local full suite separately reports 3,252 passes, one skip and the reproduced zombie-process cleanup failure.
- [Political semantic layers and bounded context](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/pull/5): all 22 local tests passed; not merged or deployed.

Merging the semantic PR was rejected by automatic approval review because it
requires explicit approval for that main-branch publication/history change with
external excerpts. No merge was performed. Production rollout and archiving also
remain blocked by their separate deployment/administration access requirements.
