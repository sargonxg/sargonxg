# Portfolio execution and usability review — November 8, 2026

This record covers public repositories and public service behavior. The account's
private inventory, cleanup decisions and operational diagnostics are kept out of
this repository. The [public project map](PUBLIC_PROJECT_MAP.md) contains 44
verified public repositories across `sargonxg` and `TACITUS-me`, including archived
references and forks. A fork's age does not make it disposable.

## Start with a working result

| Starting point | Reproducible result | Boundary |
| --- | --- | --- |
| [Political task workflows](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/docs/POLITICAL_TASK_WORKFLOWS.md) | Five attributed preparation packets, Markdown worksheets and independent receipt verification | Standard-library Python; no paid API, inference or production database |
| [Historical research atlas](https://github.com/sargonxg/Syria-political-analysis/blob/main/docs/historical-atlas.md) | Local browser atlas of retained UCDP and World Bank records | Historical observations and provider uncertainty; not a live conflict forecast |
| [TACITUS Workbench](https://github.com/sargonxg/tacitus-workbench) | Recorded-mode workbench and static evidence readers | Native helper and Linux-only evaluation acceptance are separate |
| [DIALECTICA v3](https://github.com/sargonxg/A3_DIALECTICAbyTACITUS_v3) | Rust capsule contracts and fixture development | Engine development; not certified as an integrated hosted PRAXIS ingestion service |
| [PRAXIS](https://praxis.tacitus.me) | Public product pages and invited workspace entry | Invitation-only; AI generation and paid operations remain paused |

PRAXIS is the visible workbench; DIALECTICA v3 is the current capsule-engine
development line. Earlier DIALECTICA repositories remain prototypes and historical
references. AGON and KAIROS explore conflict/evidence and temporal primitives;
their presence does not establish a deployed integration. The EdgeQuake-based
core and Workbench's native Context JSON are distinct from DIALECTICA capsule
bundles. The public pipeline's teaching packet is also a separate format.

## Twenty-eight implemented improvements

The priority order starts with production integrity, then public starting points
and the inspectable political-data examples. Source changes are on main. Existing
unrelated PRs and unique branches were preserved.

| # | Change | Implementation / evidence |
| --- | --- | --- |
| 1 | Route the public TACITUS site to its verified release with explicit rollback information | Public health returned 200; revision/image/traffic receipts retained privately |
| 2 | Release reviewed PRAXIS frontend while preserving invitation-only access, paid pauses and existing compute limits | Public health returned 200 with invited-only/paused; anonymous detailed health remained 403 |
| 3 | Refresh the complete public project map, including organization repositories | [44-entry catalog](../data/public-projects.json) |
| 4 | Refuse private, internal and unclassified rows in the public catalog renderer | [Renderer and three regression checks](../scripts/test_project_catalog.py) |
| 5 | Disambiguate repository identities by showing owner and repository together | [Generated map](PUBLIC_PROJECT_MAP.md) |
| 6 | Replace a stale review-branch starting point with a maintained main-branch guide | [Profile](../README.md) |
| 7 | Explain PRAXIS's actual availability in its previously empty About field | [PRAXIS repository](https://github.com/sargonxg/A4_PRAXIS_CLOUD_Work) |
| 8 | Identify the graph generator as a retained experiment | [NEXUS reference](https://github.com/sargonxg/cc-graph-TACITUS-upgrade) |
| 9 | Attribute LEANN performance claims to upstream and state the fork's evaluation limit | [LEANN fork](https://github.com/sargonxg/LEANN) |
| 10 | State Memvid's retained-fork scope without an unmeasured production claim | [Memvid fork](https://github.com/sargonxg/memvid) |
| 11 | Make ontology-source licensing and applicability limits explicit | [Ontology reference fork](https://github.com/sargonxg/open-ontologies) |
| 12 | Identify Parameter Golf as an upstream training experiment without a claimed TACITUS benchmark | [Training reference](https://github.com/sargonxg/parameter-golf-Giulio-train) |
| 13 | Execute a resolution-brief preparation recipe | [Worked resolution packet](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/resolution_brief.md) |
| 14 | Execute a communiqué-comparison preparation recipe | [Worked comparison](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/communique_comparison.md) |
| 15 | Execute a consent/inclusion mediation-preparation recipe | [Worked mediation packet](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/mediation_preparation.md) |
| 16 | Execute a bounded media-framing review recipe with sample limits | [Worked media packet](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/media_framing_review.md) |
| 17 | Execute an HR convention-applicability preparation recipe | [Worked HR packet](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/hr_policy_application.md) |
| 18 | Reconstruct saved packets against the retained corpus so rewritten hashes cannot conceal altered passages | [Independent verifier](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/verify_packet.py) |
| 19 | Carry quotations, attribution, locators, dates and original evidence metadata into readable worksheets | [Task exporter](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/task_workflows.py) |
| 20 | Leave analyst interpretation, hypotheses and applicability checks explicitly unresolved | [Workflow contract](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/docs/POLITICAL_TASK_WORKFLOWS.md) |
| 21 | Package exact payload variants and integrity manifests, preserving bytes on Windows checkouts | [Retained manifest](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/manifest.json) |
| 22 | Compare exact byte budgets with omitted IDs, reasons and retained primitive coverage | [Budget comparison](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/worked_tasks/budget-comparison.json) |
| 23 | Verify package contents, worksheets, omissions and comparisons against reconstruction | [Adversarial checks](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/tests/test_task_workflows.py) |
| 24 | Refuse existing output paths and validate all task options before writing | [Exporter](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/examples/political_semantics/task_workflows.py) |
| 25 | Add CI commands for task generation, verification and retained artifacts | [Workflow](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/.github/workflows/context-example.yml); remote execution is disabled at repository level and is not claimed as passed |
| 26 | Read the evidence explorer's Unicode fixtures explicitly as UTF-8 on Windows | [Explorer tests](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/blob/main/tests/test_evidence_explorer.py) |
| 27 | Resolve Workbench React components explicitly rather than similarly named model modules on case-insensitive filesystems | [Fix](https://github.com/sargonxg/tacitus-workbench/commit/ff613456fd458ced5aa1802faee3d4cd4a42cf74) and [integrity update](https://github.com/sargonxg/tacitus-workbench/commit/364f0358cfa71a2b6eb3311fd02f2d72303bea72) |
| 28 | Add a concrete Windows PowerShell startup path and correct npm working-directory/build prerequisites | [Workbench setup](https://github.com/sargonxg/tacitus-workbench#inspect-a-context-in-the-browser) |

The pipeline changes are retained in commits
[`9783ceb`](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/commit/9783cebdefe904bd424c01561f9e1edb33228f71),
[`d3ca169`](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/commit/d3ca16935fa22bc60775fcfe67351e52bf51359a),
[`5aac9cb`](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/commit/5aac9cba46e044e8feae2bdc48059692c02d675f) and
[`018e69e`](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open/commit/018e69e).
These commits implement local examples, not a claimed hosted deployment.

## Checks actually executed

- Political task examples: **45 tests passed** on Windows/Python 3.12. Five
  packages and 21 payload files verified. A fresh checkout with Windows line-ending
  settings also verified. CI configuration was reviewed and extended; repository
  Actions execution is disabled, so no remote CI pass is claimed.
- Workbench: Windows typecheck, application build, static-viewer build and
  305-file inventory verification passed. The Windows full test run had 76 passes,
  3 failures and 5 native skips; the failures concern Linux-only Python/file-mode
  assumptions. The original remote run passed builds/tests and failed the stale
  integrity manifest; that manifest was corrected in the subsequent commit.
  The subsequent [exact-source Linux run](https://github.com/sargonxg/tacitus-workbench/actions/runs/42446776810)
  passed: 79 tests, 5 explicit native skips, both builds, typecheck and all 305
  inventory identities. This does not turn the three Windows platform failures
  into passes.
- Research atlas: initial standard-library run had 121 passing tests, one loader
  error for missing optional PyLD and one Windows symlink skip. With PyLD installed
  into an isolated test directory, the affected 13 ontology tests passed. The
  public snapshot built with 120,576 historical event records and 15,272 annual
  country values. No source-kit code was changed in this checkpoint.
- Public sites: 38 desktop/mobile page visits and 103 internal links returned
  successfully, with no page exceptions or horizontal overflow. Earlier network-idle
  timeouts are retained separately from the successful document-readiness repeat.
  Protected-resource 403 console entries were observed and are not called a
  zero-console-error result. No inference, checkout or invitation creation ran.

The remaining public repositories received metadata, README, source-structure,
manifest, license, workflow, branch, PR and deployment-metadata inspection. That
does **not** mean every source line, build or integration was executed. All
licenses and upstream attribution were preserved. Exact bytes, hashes and test
counts establish reproducibility; they establish neither political truth nor
improved reasoning, lower inference costs or media-bias detection.

## Retained-fork attribution notices

The original upstream README bodies were preserved byte-for-byte; only a bounded
fork-status notice was prepended and read back from GitHub. No library build,
model evaluation or training job was run for these documentation changes.

- [sargonxg/LEANN](https://github.com/sargonxg/LEANN/commit/4dedfc6ed04c7dde6c77ea47509e4c26581467a7)
- [sargonxg/memvid](https://github.com/sargonxg/memvid/commit/45e10d9fd6454beab4fe8dffc9052f2b661b9093)
- [sargonxg/open-ontologies](https://github.com/sargonxg/open-ontologies/commit/95adce75a89b2467a3018f751433478b60fdbdf2)
- [sargonxg/parameter-golf-Giulio-train](https://github.com/sargonxg/parameter-golf-Giulio-train/commit/63f48cdea9101134ab51db2b59fdf2f7593f6dc8)
