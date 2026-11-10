# Verified workflows — 10 November 2026

The account inventory covered 79 repositories across the personal account and TACITUS-me. The public map contains 44 public repositories; private project names and source are excluded. Original projects, upstream forks and archived references remain distinct. No repository visibility, license, archive status or account identity was changed.

## Run something useful

- [Policy pipeline](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open): sources → ontology → semantic layer → bounded context → cited draft. Explicit provider adapters and a finite evidence-inspection agent.
- [Workbench](https://github.com/sargonxg/tacitus-workbench): inspect the actual model result, quotations, qualifications, graph and agent steps; malformed imports clear the previous draft.
- [Syria source toolkit](https://github.com/sargonxg/Syria-political-analysis): export curated historical source records with explicit required context into the pipeline.
- [AGON](https://github.com/sargonxg/AGON): verify exact quoted evidence and reject an altered displayed quotation with a retained hash.
- [KAIROS](https://github.com/sargonxg/KAIROS-temporal-vision-TACITUS): explore temporal structures in mock mode; loopback default and explicit container ingress.
- [TCGC](https://github.com/sargonxg/TCGC_TACITUS-Conflict-Grammar-Corpus_BENCHMARK): score its own corpus separately from the new policy-workflow recording inspector.

## Exact verification scope

- pipeline reference: 33 local tests passed.
- pipeline existing: 45 local tests passed.
- syria toolkit: 137 local tests passed.
- agon: 75 local tests passed.
- kairos: 9 local tests passed.
- dialectica: 81 local tests passed.
- tcgc: 78 local tests passed.
- workbench: 91 local tests passed.

The workbench has 5 skipped native/configured acceptance tests, TCGC has 3 optional adapter/API skips, and DIALECTICA has 1 ignored test. Those paths are not claimed as verified. The workbench also passed 15 new browser checks at 320, 390, 768 and 1440 px, with screenshots from the actual interface. The checks above do not establish a fully accepted hosted PRAXIS deployment or validate every feature in every repository.

## Actual model execution

The public Syria example records flat-evidence and structured-context Cloudflare drafts plus a two-step evidence-inspection agent. Reported usage is 1,280, 1,889 and 2,427 tokens respectively. The structured draft uses fewer output tokens but more total tokens than the flat draft. This one-model, one-task smoke test does not establish quality, latency or efficiency improvements. A failed initial agent-format attempt was refused and retained, rather than silently presented as success.

Model calls were observed through the connected Cloudflare API using the code-produced request bodies. Replay/import checks bind files by checksum but do not authenticate a supplied provider recording. Direct local HTTP provider adapters are covered by loopback tests; no live Ollama model was run.

[Research index: 12 papers and implementation boundaries](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/tree/main/research). Hosted PRAXIS generation and paid upgrades remain paused. The public local workflows remain separate from native capsules and any future hosted attachment bridge.
