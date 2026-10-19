# TACITUS public project map

This page distinguishes the active product surface from research modules, reference implementations, and completed experiments. It is intended to prevent repository names or retained prototypes from being mistaken for current production services.

_Last reviewed: 15 October 2026._

## Active product and platform work

| Project | Role | Public status |
| --- | --- | --- |
| [PRAXIS](https://praxis.tacitus.me) | Analyst-facing workbench for evidence, context capsules, agentic workflows, and inspectable outputs | Invitation-only; AI generation and paid upgrades paused |
| [TACITUS Workbench](https://github.com/sargonxg/tacitus-workbench) | Standalone local evidence inspector with recorded examples and an opt-in pinned Rust core | Local developer tool; hosted multiuser operation unsupported |
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

- **Active product development:** part of the intended user-facing TACITUS or PRAXIS surface.
- **Active prototype:** implementation work is current, but the stated release gate has not passed.
- **Active experimental:** maintained research or engineering work whose interfaces may change.
- **Alpha benchmark:** evaluation infrastructure exists, but definitive measured results are not yet published.
- **Reference implementation:** a smaller educational or reproducible example, not the production system.
- **Completed prototype:** retained as a portfolio case study, without a maintenance or service commitment.
- **Superseded:** an architectural path that informed later work but is no longer the current direction.

Repository READMEs and licenses control the exact terms, limitations, and reuse conditions for each project.
