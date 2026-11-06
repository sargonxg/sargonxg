# TACITUS public project map

TACITUS is an independent project building AI data infrastructure for policy and political analysis. This map distinguishes runnable tools, paused workspace access, experimental engines and retained prototypes. Repository names and screenshots do not establish a production service.

_Latest research-tool review: 6 November 2026. Earlier dated verification records below retain their original scope; other experimental-project boundaries follow the 15 October review._

## Three independent projects

| Project | Focus |
| --- | --- |
| [TACITUS](https://www.tacitus.me) | AI data infrastructure and research tools for policy and political analysis. The Middle East kit and Workbench belong here. |
| [Concordia Discors Magazine](https://concordiadiscors.org/) | Political ideas, polarization, pluralism and civic virtue. |
| [Next Diplomacy](https://nextdiplomacy.substack.com/) | A publication in development on AI policy, governance and diplomacy. |

## Independent infrastructure and workspace

| Project | Role | Public status |
| --- | --- | --- |
| [PRAXIS](https://praxis.tacitus.me) | Agentic workspace for policy research | Paused; public recorded examples and local tooling remain available |
| [TACITUS Workbench](https://github.com/sargonxg/tacitus-workbench) | Static native Context viewer, a separate [research-selection reader](https://github.com/sargonxg/tacitus-workbench/blob/main/apps/workbench/docs/research-selection-reader.md), and a local evidence inspector | Browser readers retain imported bytes and keep their formats separate. Native query/authoring are implemented opt-in paths, but full native acceptance was not rerun: Cargo is absent. Hosted multiuser backend unsupported. See the [dated quickstart receipt](https://github.com/sargonxg/tacitus-workbench/blob/main/docs/READINESS_2026-11-05.md). |
| [Middle East public-source research kit](https://github.com/sargonxg/Syria-political-analysis) | Historical event and country-indicator atlas, bounded query/export workflow, curated source/ontology desk and optional private notebook | [Clone/run/query guide](https://github.com/sargonxg/Syria-political-analysis/blob/main/docs/historical-atlas.md) and [actual source selections](https://github.com/sargonxg/Syria-political-analysis/tree/main/examples/historical-research) are available. Historical provider records and the curated political collection remain separate; private cases require the single-operator notebook. |
| [DIALECTICA](https://github.com/sargonxg/A3_DIALECTICAbyTACITUS_v3) | Rust-first compiler, review, graph, storage, and export engine for PRAXIS Capsules | Active experimental engine; local contracts and fixture paths exist, full production integration is incomplete |
| [Policy capsule core / integration lab](https://github.com/sargonxg/tacitus-political-policy-second-brain) | EdgeQuake-based local-first integration environment for policy research | Bounded capsule-only developer workflow; full application end-to-end verification remains a release gate |

## Active research modules

| Project | Research question | Public status |
| --- | --- | --- |
| [TCGC](https://github.com/sargonxg/TCGC_TACITUS-Conflict-Grammar-Corpus_BENCHMARK) | How should systems be evaluated on typed conflict and policy structure, chronology, contradiction, and provenance? | Alpha benchmark and corpus; measured public leaderboard remains pending |
| [AGON](https://github.com/sargonxg/AGON) | How can difficult human text be converted into reviewable actors, claims, commitments, contradictions, and friction signals? | Experimental research software; licensing is not yet finalized |
| [KAIROS](https://github.com/sargonxg/KAIROS-temporal-vision-TACITUS) | How can policy and institutional text retain sequence, overlap, delay, episodes, and changing commitment status? | Experimental Rust library and demonstration surface |

## Public reference implementation

| Project | Purpose | Public status |
| --- | --- | --- |
| [TACITUS Knowledge Pipeline](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open) | Accessible notebooks and graph queries showing an evidence-linked extraction-to-graph workflow | Reference implementation, not the production TACITUS stack |

## Completed or superseded experiments

These repositories are retained for provenance, attribution, and portfolio evidence. They are not current TACITUS product commitments.

| Repository | Historical purpose | Status |
| --- | --- | --- |
| [CONCORDIA](https://github.com/sargonxg/H2_CONCORDIA_GHACK_SUBMISSION) | Voice-AI mediation hackathon prototype | Completed prototype |
| [NEXUS](https://github.com/sargonxg/cc-graph-TACITUS-upgrade) | Neo4j application-generator experiment | Superseded |
| [Graphify for TACITUS](https://github.com/sargonxg/graphify_4TACITUS) | Evaluation of an upstream code/document graph tool | Completed integration experiment |
| [Parameter Golf experiment](https://github.com/sargonxg/parameter-golf-Giulio-train) | Small-model training and conflict-domain evaluation exploration | Historical fork; no longer maintained |

Other archived public repositories may preserve earlier integrations, forks, hackathon drafts, storage experiments, or superseded architectural paths. They should not be interpreted as supported components unless this page identifies them as active.

## Status vocabulary

- **Paused workspace:** PRAXIS service work is paused; a recorded demonstration does not establish generation availability.
- **Runnable static or recorded tool:** the documented build and browser flow pass within the stated verification scope.
- **Active prototype:** implementation work is current, but the stated release gate has not passed.
- **Active experimental:** maintained research or engineering work whose interfaces may change.
- **Alpha benchmark:** evaluation infrastructure exists, but definitive measured results are not yet published.
- **Reference implementation:** a smaller educational or reproducible example, not the production system.
- **Completed prototype:** retained as a portfolio case study, without a maintenance or service commitment.
- **Superseded:** an architectural path that informed later work but is no longer the current direction.

Repository READMEs and licenses control the exact terms, limitations, and reuse conditions for each project.

## Semantic exploration and working database · 6 November 2026

The expanded atlas contains 120,576 retained GED records for 2000–2025 and 15,272 annual World Bank values. Five scoped vocabulary lenses expose actual provenance, concepts, time, geography and annual observations. A 2,048-record navigation slice is explicitly nonrepresentative. Workbench adds a separate semantic preparation mode; its downloads remain research selections rather than native capsules or a verified PRAXIS attachment.

The source kit now builds a local SQLite database and a read-only Cloudflare D1 API. The owner-account database was remotely verified with all event/annual/profile/lens counts and 49 original fields per event. Public instructions cover local use, bounded queries and checkpointed cloud imports; there is no public shared analysis service. Source-kit CI passes on Linux and Windows, including 135 Python tests and eight Worker API tests. Workbench passes 79 tests, with five native-acceptance checks explicitly skipped. [Database workflow](https://github.com/sargonxg/Syria-political-analysis/tree/main/cloudflare) · [Semantic preparation](https://github.com/sargonxg/tacitus-workbench/blob/main/apps/workbench/docs/semantic-exploration.md).

## Historical atlas and research handoff · 5 November 2026

The atlas contains 113,656 UCDP GED 26.1 event records for 2011–2025 across nine provider country categories. A separate World Bank snapshot contains 15,272 non-null annual values, 32 indicators and ten economies; 5,848 returned null cells are documented rather than counted as data values. These dataset categories, periods and units retain their original source meaning. They do not determine borders or establish a causal relationship between events and national indicators.

The working path is clone → build the static atlas → filter or run `research-query` → validate/export a bounded selection → reopen it in [Workbench’s research-selection reader](https://github.com/sargonxg/tacitus-workbench/blob/main/apps/workbench/docs/research-selection-reader.md). The [worked examples](https://github.com/sargonxg/Syria-political-analysis/tree/main/examples/historical-research) contain real provider rows and explicit matched/exported counts, with no generated analyst conclusion. Reopening a selection does not create a native capsule, run a model or attach records to paused PRAXIS.

The source directory and political-ontology desk remain a separate curated collection: 55 source profiles and 228 context records. The large historical datasets do not expand that count or imply human review of every event. [Data, scope and reproduction](https://github.com/sargonxg/Syria-political-analysis/blob/main/docs/historical-atlas.md).

## Workbench quickstart verification · 5 November 2026

A clean npm install, TypeScript check, static viewer build and recorded local build passed. The documented Node-only preview loaded the recorded context and layer inspector. The default interface suite passed 40 tests and explicitly skipped five native/prepared-collection acceptance checks. Both example-preparation suites passed 11 tests, and onboarding source/download hashes matched the shipped archives. The [dated readiness receipt](https://github.com/sargonxg/tacitus-workbench/blob/main/docs/READINESS_2026-11-05.md) lists commands, skips and limits.

Cargo is absent in this environment. The pinned build script correctly refuses before creating an output directory; that check is not a Rust build. No native integration, model evaluation, deployment or current PRAXIS availability was certified by this pass.

## Working-tool verification · 4 November 2026

The Middle East kit passed 66 Python tests. The new media worksheet passed 19 browser assertions, including publisher-attribution and asynchronous-export checks; four new desktop/mobile accessibility audits returned no violations. Eight data/research resources are typed separately from the 55 publisher and institutional profiles. The Workbench interface suite ran 45 tests: 40 passed and five native/collection acceptance checks were skipped. Both static builds passed Cloudflare configuration dry runs. Desktop/mobile automated accessibility scans returned no violations for the new views.

This is scoped verification of those two tools. Rust engines, model-answer evaluation and full hosted integrations were not rerun. See each repository's context verification document for commands, source scope and limitations.

## Entered evidence trail · 5 November 2026

The Middle East source desk now draws only relationships supplied in a report comparison: publisher attribution, entered quotations and named upstream references. Analyst interpretation stays separate. The toolkit passed 67 Python tests and 54 browser assertions; four light/dark desktop/mobile accessibility scans reported zero violations or incomplete checks. Source counts and the saved news snapshot were not refreshed. The static public snapshot and separately authenticated private notebook remain different deployment choices.
