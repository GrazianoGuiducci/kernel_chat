# Changelog

## 0.6.0 — 2026-09-18

- **Second rereview proof reconciliation (pre-release):** strengthened the
  test-only consumer oracle after the rereview of `82078ed2...`. Link
  observation now follows rendered HTML so raw `<a href>` navigation is not
  invisible; constitutive discovery now composes an active AGENTS link with one
  real Markdown owner heading and its explicit simple-ASCII fragment contract,
  rejecting fenced-heading decoys; and the oracle environment pins both
  `markdown-it-py==4.2.0` and `mdurl==0.1.2`. These are stronger assertions
  inside the existing oracle cases, so the suite remains 53 tests.
- **External rereview reconciliation (pre-release):** after the rereview of
  `1a0720fa...`, closed the remaining Markdown consumer-surface problem by
  contracting the dependency-free runtime validator to explicit structural
  discovery contracts and moving full Markdown link semantics to an independent
  test-only CommonMark oracle (`markdown-it-py`). This avoids extending a partial
  runtime parser case by case while still falsifying the reported GFM/CommonMark
  counterexamples and active local-link delivery.
- Moved pure `--preview-adapter` ahead of INSTANCE loading so unsupported/future
  schemas or host adapters cannot block a no-write candidate observation.
- Strengthened the host-confirmation delivery regression to prove ordered
  confirmation → `git add` → `git commit` → `git push` → remote readback →
  remote reentry, rather than checking only that two strings occur later.
- Full pre-release suite now contains **53 cases**: 33 configurator, 17
  structural/receipt/drift/provenance/delivery validator, and 3 independent
  CommonMark consumer-oracle tests. CI installs the Markdown parser only as a
  test dependency; `scripts/validate.py` remains dependency-free.
- **External-review reconciliation (pre-release):** reconciled all ten findings
  from the review of `2c816975...` without adding a controller or new runtime
  subsystem. Owned text files now publish through temporary-file + atomic
  replacement at the single-file boundary; unsupported INSTANCE schemas/host
  adapters are rejected before mutation; persisted host/configured receipt
  contradictions are validated even without a local bridge; A→B→A bridge
  replacement can recover an already-confirmed host incarnation from identity;
  adapter preview no longer depends on decoding/preserving an incoherent old
  bridge; GitHub repository identity comparisons are case-insensitive while
  bridge bytes remain byte-exact; refresh preserves missing CURRENT/SOURCES;
  Markdown validation handles multiline code spans, fence length, indented code
  and HTML comments for the package navigation surface; discovery routes prove
  their destination anchors; host-confirmation docs now require commit/push and
  remote readback before a new chat relies on the receipt.
- The post-review native suite contains **54 cases** (32 configurator + 22
  validator/drift/provenance/reachability/delivery) and is exercised across all
  8 Python 3.11–3.14 × Ubuntu/Windows matrix jobs. Review findings still require
  proof on the final canonical revision before release.
- Reframed the package around a **user-owned continuity kernel** rather than a
  mandatory project-first harness. A kernel instance can now be configured
  without an active project; a project remains an optional current context.
- Added `state/INSTANCE.json` as the bounded owner of instance/package/bridge
  identity, operator-confirmed installed-bridge observation and source-contact
  observations, keeping those facts distinct from `CURRENT` user context,
  `SOURCES` owner-native knowledge and optional operational continuity.
- Added separate ChatGPT bridge-template versioning under
  `adapters/chatgpt/VERSION`. Package updates, bridge-template availability,
  configured-bridge provenance/repository/bytes, operator-confirmed installed
  bridge digest and actual host behavior are explicitly separate relations.
- Legacy pre-0.6 instances can preserve an existing configured bridge while
  creating `INSTANCE.json`. When the historical template origin of that bridge
  cannot be established, the receipt records
  `configured_bridge_template_version = unknown` instead of assigning the
  current package template retroactively.
- Standard legacy bridges are checked against `INSTANCE.instance_repository`
  before migration writes. A known bridge/instance repository mismatch is
  rejected rather than silently creating a continuity receipt whose configured
  bridge would reenter another repository.
- Added `--confirm-host-installation`: after the operator actually copies/saves
  the current configured bridge in ChatGPT, the command persists that operator
  report and binds it to the exact configured bridge SHA-256 digest. The
  repository still does not independently inspect the ChatGPT UI.
- A later local bridge replacement preserves the previous operator-confirmed
  installed digest/date while marking the local/host relation unconfirmed, so
  host drift remains reconstructible until the replacement is confirmed.
- Reduced the ChatGPT Custom Instructions template to a stable entry bridge.
  Source-contact cadence, Evolution Feedback mechanics and deeper competence /
  evolution methods remain in their repository owners and are reached only
  when pertinent.
- Extended configuration with valid no-project and project-pair modes,
  `--refresh-instance`, bounded bridge replacement and preservation of
  user-owned state / source-contact observations across reruns and updates.
  `--refresh-instance` advances package/available-template identity without
  falsifying configured-bridge provenance; `--replace-adapter` can establish
  provenance because it generates the local bridge from the current template.
- Corrected privacy/adoption guidance: non-public continuity uses a private
  standalone repository initialized from the public distribution; a normal
  fork of a public GitHub repository is treated as public.
- Deepened the portable core with situated observation-frame and transformation
  lineage, semantic determinacy without forced reopening, and explicit
  distinction among semantic relation, persistent operational incarnation,
  effect authority, actual effect and observed consequence.
- Made **situated movement** explicit across Core, Competence and AGENTS: the
  present field can resolve to use/preserve, compose, adapt/deepen, form,
  preserve unknown/defer, or `no_change` without adding a central chooser or a
  mandatory decision pipeline. Operator preference and exact effect authority
  remain outside the kernel when they own the selection.
- Added **closure convergence** to Evolution: a material correction creates a
  new resultant whose causally dependent proof, consumer, state and descriptive
  surfaces must converge before closure; prior green evidence remains evidence
  for its own revision rather than automatically proving the new one.
- Deepened evolution with first-losing-transformation diagnosis and
  owner/incarnation drift: persistent projections can be reconsidered when
  their living semantic owner or relevant conditions change, without creating
  automatic synchronization.
- Added **mobile observation without losing the point** to the portable Core:
  the object can remain stable while observation moves through another material
  source/scale/owner/representation/consumer/transformation/consequence relation
  and then returns to the same point as changed resultant or `no_change`, without
  creating a mandatory multi-view workflow.
- Deepened Evolution with **pre-closure incongruence sensing**: claim strength
  is kept distinct from proof strength; common-mode agreement between
  implementation, validator, tests or documentation is not treated as
  independent falsification.
- Let competences exercise the same mobile observation when their own method
  becomes the limiting frame, returning reusable learning to the owner that
  must behave differently in later non-identical cases.
- Refined package Markdown reachability validation so malformed prose links are visible while fenced/inline code examples remain outside the active link consumer surface.
- Added explicit AGENTS discovery routes for Core mobile observation and Evolution closure convergence; validator/tests preserve those owner-native routes without freezing explanatory wording.
- Added package-level claim/proof integrity in `AGENTS.md`: human version labels,
  owner-native tag/refs, immutable revisions, runtime artifact identity,
  discovered tests and actual CI jobs remain distinct evidence surfaces.
- Corrected `actions/setup-python` v7.0.0 provenance to the owner-native commit
  `5fda3b95a4ea91299a34e894583c3862153e4b97`; both pinned GitHub Actions now
  resolve exactly from their declared tags and use Node 24.

- Added an adoption guide and aligned README, INSTALL, architecture, user guide,
  AGENTS, adapter guidance and state documentation to the same instance-first
  product relation.
- Extended validation to make package/bridge/instance drift visible as
  reconciliation warnings rather than conflating it with structural invalidity.
- Reopened and completed the pre-canonical technical evidence closure with a
  source-bound full 0.5.3 migration fixture, raw-byte bridge SHA-256 identity,
  deterministic LF/CRLF byte discriminants, durable configured/installed
  repository-target and template-provenance receipts, and backward-compatible
  optional identity fields under `kernel_chat.instance.v1`.
- Separated configurator effects: `--refresh-instance` does not accept local
  bridge drift, `--confirm-host-installation` refuses unreconciled local bytes,
  and `--replace-adapter` does not migrate an existing instance repository.
  Missing local bridges remain visible without being regenerated implicitly.
  A requested replacement that produces the already-confirmed incarnation
  remains a legitimate `no_change` for host synchronization.
- Declared Python **3.11–3.14** support and expanded CI across every declared
  Python line (3.11, 3.12, 3.13, 3.14) on Ubuntu and Windows. GitHub Actions are
  pinned to immutable current Node-24 action revisions.
- The current regression suite contains **53 cases** (33 configurator + 17
  structural/receipt/drift/provenance/delivery + 3 CommonMark consumer-oracle), including malformed multiline Markdown-link detection, code-example exclusion, and AGENTS discovery-route preservation. CI exercises all **8 Python/OS matrix jobs**. Canonical proof belongs to the
  exact canonical revision that runs validator + full tests; repository proof
  does not claim host behavior.

Canonical source **0.6.0** does not by itself create a `v0.6.0` tag or release,
update user-owned instances, install/update ChatGPT Custom Instructions, prove
connector reachability, or establish behavioral assimilation. Those remain
separate selected effects.

## 0.5.3 — 2026-09-11

- Distinguish the user-owned fork from the canonical upstream for source contact
  and approved feedback. Include source-only changes on main and a truthful
  fallback when submission is unavailable. Existing configured/installed
  instructions are preserved until an explicit host update.

## 0.5.2 — 2026-09-10

- Added a public contribution path for testers, operators, developers and AI
  coders through `CONTRIBUTING.md` and an Evolution Feedback Issue template.
- Made first-use impressions part of the evidence field when they expose useful
  friction, clarity, unexpected success or a new possibility.
- Added a light source-contact relation to the installed ChatGPT adapter:
  roughly seven days between checks during active use, or sooner when a current
  problem may already have been corrected upstream.
- Kept source contact read-only and non-blocking: newer source is a possibility,
  not an automatic update or host mutation.
- Added coder guidance to prepare compact Evolution Feedback and require
  operator consent before any public submission; concrete changes use fork +
  Pull Request rather than implied write access to upstream `main`.
- Extended structural/configuration tests so the configured adapter must carry
  the weekly source-contact and feedback relations.

This source patch does not itself create a `v0.5.2` release, update installed
Custom Instructions, submit feedback, or schedule background work.

## 0.5.1 — 2026-09-10

- Made the ChatGPT host-activation boundary explicit during adoption: repository
  configuration no longer risks being reported as completed ChatGPT installation.
- Added an adoption rule to `AGENTS.md`: once the configured adapter exists, a
  coder or agent must immediately tell the operator that the ChatGPT UI
  copy/save step is still required.
- Added an explicit host-UI boundary message to the configurator output and
  covered that handoff in the existing configuration regression suite.
- Reworked README and installation guidance so repository configuration,
  operator-confirmed Custom Instructions installation, host reachability and
  behavioral assimilation remain distinct evidence states.
- Clarified the same operator boundary in the ChatGPT adapter documentation.

This source patch does not itself create a `v0.5.1` tag, release, account
installation or behavioral-assimilation claim. Those remain separate effects.

## 0.5.0 — 2026-09-10

- Deepened semantic comprehension: understand represented knowledge through
  its function and still-valid reasons, and regenerate methods in new contexts.
- Separated selective project reentry from kernel-method retrieval through
  the existing AGENTS entry, without introducing an automatic boot.
- Made competence circulation, formation from knowledge/success/possibility,
  owner-local learning and practical cultivation explicit in existing owners.
- Preserved causal reentry reasons while keeping reusable methods out of state.
- Clarified source-change sensing, local embodiment and recipient claim levels.
- Preserved configured adapters by default; added independent `--replace-adapter`
  and no-write `--preview-adapter`. Host installation remains separate.
- Added eight configuration regression tests, Windows/Linux CI coverage and
  package-link checks. These validate source mechanics, not model assimilation.

The version identifies the evolved source package. A tag, release and account
installation are separate actions.

## 0.4.0 — 2026-08-21

Canonical `kernel_chat` incarnation and continuation of the `0.3.0` lineage.

- Established the product as a portable harness for chat environments without
  their own durable project workspace.
- Separated the host-neutral core, user-owned state, persistence surface, and
  host adapter.
- Added present-first routing, situated competence and metacompetence,
  source-aware reentry, FDLA self-observation, and revisable evolution.
- Added a ChatGPT Custom Instructions adapter and a configurator that also
  initializes the user's first project state.
- Added dependency-free structural validation without artificial behavioral
  proof claims.
- Restored the portable operational organ for unfinished work,
  requests/results, receipts, replay protection, and recovery.
- Integrated the complete Git ancestry and historical `v0.3.0` release into
  the new owner repository.
- Replaced the former public name and surface with `kernel_chat`; the earlier
  repository is no longer an operational dependency or parallel product.

## 0.3.0 — 2026-08-20

First integrated all-in-one incarnation, originally released as Meta Semantic Kernel. It assembled the ChatGPT adapter, semantic routing, competence organs,
durable state, operational continuity, reversible evolution, documentation,
and structural validation. The original release and commits remain reachable
in this repository's Git history.

## 0.2.0 — 2026-08-20

Moved the project from a prescribed analytical workflow to present-driven,
falsifiable relations while keeping source, inference, introduced form, and
unknowns distinguishable.

## 0.1.0 — 2026-08-20

Established the initial research baseline from which the portable chat kernel
was developed.
