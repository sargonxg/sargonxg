# From evidence to reviewable judgment

[![TACITUS / PRAXIS layered policy knowledge map](../assets/policy-knowledge-map.svg)](../assets/policy-knowledge-map.svg)

This is an **architecture illustration**, not a product screenshot, a measured benchmark, or a graph extracted from a real diplomatic file. The dense topology illustrates relationships across knowledge layers. The example readout draws on the fictional Nordalia case used on the [TACITUS website](https://www.tacitus.me/).

The practical idea: a policy assessment should connect what sources say, who is involved, what changed, how the analyst reasoned, and what remains uncertain. A claim, a conclusion, and an idea for action are different objects.

## Read the structure

| Layer | Question |
| --- | --- |
| Evidence | Where did this come from? |
| Claims | Who asserts it, and who disputes it? |
| Situation | Which actors, interests and commitments connect? |
| Temporal | When did it happen, and when was it known? |
| Ontology | What do the terms and relationships mean? |
| Reasoning | Which method, assumptions and alternatives shaped the assessment? |
| Memory | What changed between versions? |
| Governance | Who reviewed it, and for what use? |
| Runtime | Which instructions and constraints should guide an AI tool? |

The nine layers follow the public [TACITUS capsule design](https://www.tacitus.me/capsules) and [DIALECTICA reference graph](https://github.com/sargonxg/A3_DIALECTICAbyTACITUS_v3/blob/main/fixtures/canonical-capsules/conflict-situation-capsule/graph.jsonld). They describe the architecture; they do not imply that every layer is complete in the live application.

## Product and research

**PRAXIS** is the policy workbench. **Context Capsules** hold reusable context. **DIALECTICA** is the engine project. **AGON** and **KAIROS** explore conflict structure and chronology; **TCGC** provides an evaluation framework.

As reviewed on **29 September 2026**, the current PRAXIS release supports the tested core flow of document upload, proposal review, capsule attachment, a sourced answer and saved history. This is a narrow functional result. Full portable context preservation, conversational ontology authoring, delegated research completion and expert evaluation of analysis quality remain development work.

Explore the [live PRAXIS workbench](https://praxis.tacitus.me), the [product explanation](https://www.tacitus.me/product/praxis), and the [public research](https://www.tacitus.me/research).

## Reproduce the visual

Run `python scripts/render_knowledge_map.py` from this repository. The renderer uses only the Python standard library, a fixed seed, editable vector text and no external image services.
