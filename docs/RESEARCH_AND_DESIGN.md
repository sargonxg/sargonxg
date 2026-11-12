# Why TACITUS keeps the evidence attached

TACITUS is an independent effort to make policy research easier to inspect and reuse: preserve sources, express the question, retain important conditions, and keep the analyst's judgment distinct from the record. The practical hypothesis is that better prepared context can help people and models produce better work. That benefit must be measured, not inferred from an attractive graph.

Reviewed on 11 November 2026, America/New_York. The notes below draw on the papers' methods and evaluation sections as well as their abstracts. They are a reading guide, not a reproduction of the authors' experiments.

## Retrieval is an external knowledge path

Lewis et al. (2020), [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), §2–4.

> “providing provenance for their decisions and updating their world knowledge remain open research problems”

The paper combines a dense passage retriever with a sequence generator. RAG-Sequence marginalizes a document choice over the output; RAG-Token can use a different document for each token. The experiments address question answering, generation and fact verification. It does not establish a general policy-research review process.

TACITUS's local reference compiler instead starts from explicitly supplied passages and annotations. Its contribution is inspectable context assembly: editions, quotations, qualifications, omissions and review state travel together. This is an engineering choice, not a new trained retriever or a demonstrated improvement over the paper. Measure quotation fidelity, omitted conditions and whole-task effort independently from answer fluency.

## A large context window does not guarantee use

Liu et al. (2023), [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), §2–5.

The authors move relevant evidence within multi-document QA inputs and separately test exact key/value retrieval. Many tested readers perform worse when the needed information is in the middle. Their setups also distinguish retriever recall from reader performance: finding another relevant document does not guarantee a useful answer. These are measurements of particular models/tasks, not a universal law about current models.

For TACITUS, this motivates testing where qualifications are placed and what selection omits. A shorter capsule can discard essential context. A fair study should keep the source set and model settings fixed, vary ordering and context treatment, and record unsupported assertions, retained conditions, tokens, latency and reviewer effort. Counts of assembled nodes or bytes do not answer that question.

## GraphRAG addresses a different question class

Edge et al. (2024; revised 2025), [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130), §3–5.

Their pipeline extracts entities/relations, builds hierarchical communities, summarizes communities, and combines question-specific partial responses. The experiments compare community levels with text map/reduce and vector retrieval on large podcast/news collections, using criteria suited to global sensemaking. A claim about corpus-wide themes is different from checking one exact quotation.

TACITUS's source-linked graphs are not automatically implementations of GraphRAG. An authored attribution edge can help inspect a statement; it does not reproduce hierarchical community summarization. A future comparison should separate local evidence lookup from global synthesis and include indexing/model costs, not just final-answer tokens. No comparative quality or cost advantage is claimed in this portfolio pass.

## Provenance is a foundation, not a truth oracle

Groth and Moreau, eds. (2013), [W3C PROV overview](https://www.w3.org/TR/prov-overview/).

The PROV family offers a vocabulary for entities, activities and agents involved in producing data. TACITUS uses this distinction to explain why a source record, an extraction proposal and a review decision need different identities. The teaching export and small evidence validator are not PROV-conformance implementations. A SHA-256 digest binds bytes; it does not authenticate the publisher, establish rights or prove a claim.

## What is borrowed and what this work adds

| Source | Credit and role | TACITUS boundary |
| --- | --- | --- |
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | Original graph-index/community-summary implementation and research | A research comparison, not an undeclared dependency of every TACITUS graph |
| [EdgeQuake](https://github.com/raphaelmansuy/edgequake) | Rust graph/RAG application stack underlying the Policy Workbench integration lab | Retain Apache-2.0 and the lab's `UPSTREAM.md`; distinguish inherited stack from policy-layer changes |
| [Graphify](https://github.com/Graphify-Labs/graphify) | Code/document graph navigation | Fork retained for evaluation; inferred edges need source verification |
| [LEANN](https://github.com/StarTrail-org/LEANN) | Retrieval research and implementation | Its reported retrieval/storage results belong to upstream until reproduced |
| [Memvid](https://github.com/memvid/memvid) | Portable memory-storage implementation | Storage candidates need independent persistence and exact-locator checks |
| [Open Ontologies](https://github.com/fabio-rovai/open-ontologies) | Ontology engine/tooling | Ontology reuse preserves original licenses and does not establish domain applicability |
| [Parameter Golf](https://github.com/openai/parameter-golf) | Training challenge, code and rules | Historical experiment; no new TACITUS model or training result is claimed |

Each repository's own license, upstream notice and source rights remain authoritative. Do not relabel an upstream result as a TACITUS achievement. If code is adapted, retain the license and name the changed files and behavior. If an idea is an inspiration rather than copied code, say so.

## The contribution to test

The useful unit is a complete research job: a question, a dated source set, a selected context, a draft, and a reviewable output. Start with the [public reference pipeline](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open), inspect exports in the [local Workbench](https://github.com/sargonxg/tacitus-workbench), and use the [historical source toolkit](https://github.com/sargonxg/Syria-political-analysis) when its dataset scope fits the question. These tools have distinct formats and acceptance gates; their existence is not proof of an automatic integration.

A valuable improvement should reduce a concrete failure—lost attribution, stale evidence, an omitted exception, an untraceable draft, or repeated preparation effort. Evaluate that failure on held-out work with matched baselines and domain review before claiming better policy judgment or improved lives.
