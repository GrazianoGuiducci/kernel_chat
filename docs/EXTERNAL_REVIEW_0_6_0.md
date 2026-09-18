# kernel_chat 0.6.0 — External Review Brief

```text
source_version: 0.6.0
review_state: external_rereview_pending
canonical_repository: GrazianoGuiducci/kernel_chat
review_target: exact current main commit checked out by the reviewer
latest_tagged_distribution: v0.5.0
v0.6.0_release: intentionally not created before review
```

## Purpose

Re-review the current canonical source of `kernel_chat 0.6.0` after reconciliation
of the first external-review findings and before a numbered release is selected. Pin the exact revision you inspect with `git rev-parse HEAD`.
Do not treat a later moving `main`, a development commit, or a future tag as
equivalent to the revision actually reviewed.

This brief is a navigation/evidence surface. Product truth remains in the
living owners and executable source.

## Product relation

`kernel_chat` is a user-owned continuity kernel for cloud chats and small
conversational systems that do not own a durable workspace.

Keep these states distinct:

```text
canonical package
!= user-owned instance
!= configured bridge
!= operator-confirmed installed bridge
!= repository reachability
!= exercised conversation behavior
!= later behavioral assimilation
```

A project is optional: it can become a current context/source without becoming
the identity of the kernel.

## Recommended review path

1. `README.md` — product claim and user-facing contract.
2. `CURRENT_STATE.md` — current source/evidence boundary.
3. `docs/ARCHITECTURE.md` — ownership and incarnation model.
4. `docs/ADOPTION_GUIDE.md` — adoption and installation states.
5. `AGENTS.md` — host entry, source contact and operating discovery.
6. `kernel/KERNEL.md` — portable Core.
7. `kernel/COMPETENCE.md` — competence formation/circulation.
8. `kernel/EVOLUTION.md` — evolution, proof and closure convergence.
9. `kernel/FDLA.md` — interpretation-closure correction.
10. `scripts/configure.py`, `scripts/validate.py` and `tests/` — mechanics and evidence.

`docs/EVOLUTION_GUIDE.md` is genealogy after the current form is understood;
it is not a substitute for current owners.

## Reproduce repository proof

Supported Python lines are **3.11–3.14**.

The runtime validator remains dependency-free:

```bash
python scripts/validate.py
```

For the complete regression suite, install the test-only consumer oracle:

```bash
python -m pip install -r requirements-test.txt
python -B -m unittest discover -s tests -v
```

For a clean checkout the expected repository-level relation is:

```text
validator: valid=true, errors=[], warnings=[]
tests: 38 configurator + 17 structural/receipt/drift/provenance/delivery + 3 CommonMark oracle = 58
CI: Python 3.11 / 3.12 / 3.13 / 3.14 x Ubuntu / Windows = 8 jobs
```

Confirm that CI is green on the exact review revision. Do not inherit green
status from another commit.

The workflow pins `actions/checkout` v7.0.1 and `actions/setup-python` v7.0.0
by immutable SHA. If dependency provenance matters, resolve owner-native tags
independently rather than trusting version comments.

## High-value review relations

### State ownership

Verify that `INSTANCE`, `CURRENT`, `SOURCES` and optional `operations/` retain
distinct functions and that generated/current views do not become semantic
authority by proximity.

### Legacy migration and provenance

Check that 0.5.3 migration preserves user state and a legacy configured bridge
without inventing template provenance. `unknown` provenance is valid; a known
bridge/instance repository mismatch should fail before owned-file mutation.

### Configurator effect boundaries

Verify:

```text
--refresh-instance != accept local bridge drift
--confirm-host-installation != repair configured state
--replace-adapter != migrate existing instance_repository
requested replacement != material host drift by assumption
missing local bridge != permission to regenerate during unrelated work
```

A no-write preview may inspect another target without rebinding the instance.

### Artifact identity

Configured and installed bridge digests claim raw-byte SHA-256 identity.
LF/CRLF-only changes must remain distinguishable, and byte identity must not be
confused with repository target or provenance identity.

### Host evidence

`--confirm-host-installation` records an operator report about an exact configured
bridge. It must not become direct ChatGPT UI inspection, connector reachability,
conversation behavior or assimilation evidence.

### Evolutionary integrity

Review mobile observation, pre-closure claim/proof sensing, common-mode evidence
limits, closure convergence, consumer-surface fit and capability discovery.
They should remain distributed faculties, not a standing reviewer, central
chooser, score or mandatory multi-pass pipeline.

```text
material correction
-> new resultant
-> only causally dependent surfaces converge
-> proof belongs to resulting identity
-> another pertinent observation can still disagree
-> material delta | no_change
```

### Discovery and delivery

The ChatGPT bridge should remain small and route missing method knowledge through
`AGENTS.md`. `AGENTS.md` must preserve discoverable routes to Core mobile
observation and Evolution closure convergence.

### Validation-frame fit

The dependency-free runtime validator intentionally does **not** parse arbitrary
Markdown. It protects explicit structural discovery-route declarations and their
living owner headings.

Full Markdown consumer semantics belong to the test suite. The independent
CommonMark oracle must:
- find active package-local links and reject missing destinations;
- confirm the constitutive AGENTS discovery links are active for the consumer;
- reproduce the five R1/F06 counterexamples with the expected active/non-active
  link relation.

A future change that makes runtime regexes appear more complete is not a
substitute for this independent consumer oracle.

### Capability-relative onboarding and product fit

Review the adoption surface from the position of an ordinary user who may have
different host capabilities.

The product should preserve:

```text
durable project filesystem + capable coder/terminal
-> MAIOS Project Kernel is normally the more native carrier

turn-reactive cloud chat without its own durable workspace
-> kernel_chat + user-owned repository persistence
```

For `kernel_chat`, setup mechanics are receiver-relative:

```text
required adoption effect
+ actually available tool / permission
-> perform effect directly when authorized
-> otherwise surface the smallest missing operator action
```

Verify that Python/Git commands remain the supported reference implementation
without becoming a claim that the human must personally execute every command.
Repository access, repository-write authority, filesystem/terminal access,
Python execution and ChatGPT account-setting authority must remain distinct.

A local or remote filesystem (including a VPS) is usable only when the current
host exposes an authorized execution route. If no execution surface can run the
reference configurator, the assistant must not fabricate configured state or
receipts.

Custom Instructions installation remains an operator-owned host effect unless a
future host explicitly exposes that authority.

### Support contract

The public support claim is Python 3.11–3.14. Documentation, workflow matrix and
source should not imply a broader or narrower contract than the evidence.

### Canonical/release boundary

At review time:

```text
canonical source = 0.6.0
latest tagged distribution = v0.5.0
v0.6.0 tag/release = intentionally pending external review
```

Source publication must remain distinct from release, user-instance migration,
bridge replacement, host update and announcement.

## Evidence limits / non-claims

Repository tests and CI do not establish installation in a specific ChatGPT
account, connector availability in a turn, real conversational behavior, later
assimilation, background autonomy, autonomous self-evolution, AGI or subjective
awareness.

## Useful finding format

```text
finding
affected path / owner
exact reviewed revision
condition / reproduction
expected relation
observed relation
evidence
first likely losing seam
downstream consequence
suggested direction (optional)
```

Separate product defect, documentation/claim drift, missing evidence,
release-readiness concern, and unresolved question. A different possible design
is not itself a defect; show the material relation it changes.

## Reconciliation of the 2c816975 review findings

The first external review fixed its observations to
`2c81697595baf4a330f99f6a9e96d799dac4370e` and reported F01–F10.
The current canonical source reconciles each finding in its owning seam:

| Finding | Reconciliation | Native discriminant |
| --- | --- | --- |
| F01 | Owned text files are prepared separately and atomically replaced per file; recovery docs explicitly keep multi-file commands non-transactional. | replacement failure preserves prior INSTANCE |
| F02 | Existing INSTANCE must be `kernel_chat.instance.v1` with `host_adapter=chatgpt` before mutation. | unsupported schema refresh fails without writes |
| F03 | Confirmed receipts require confirmation time; equal configured/installed digest with conflicting known repositories is invalid even without a local bridge. | persisted contradiction + missing bridge |
| F04 | Host-confirmed state is re-derived from the resulting configured identity and surviving confirmed receipt. | A→B→A restores confirmed state |
| F05 | `--preview-adapter` returns the candidate before old-bridge decode/preservation checks. | mismatched and non-UTF8 old bridge do not block preview |
| F06 | Navigation surface masks HTML comments, fenced/indented code and multiline code spans with fence-length semantics. | active/non-active Markdown pairs |
| F07 | Required AGENTS routes must be active and their destination anchors must exist. | renamed heading and HTML-comment-only route fail |
| F08 | GitHub `owner/repo` identity comparison is case-insensitive; artifact bytes remain exact. | mixed-case refresh/confirm + validator receipt case |
| F09 | Host confirmation docs require selected commit/push and remote readback before reentry. | documentation delivery contract test |
| F10 | Existing instances preserve absent CURRENT/SOURCES until explicit state replacement/restoration. | refresh keeps missing state absent |

The first rereview target `1a0720fa...` carried 54 native tests. The current canonical source carries **53 tests**: 33 configurator, 17
structural/receipt/drift/provenance/delivery validator, and 3 independent
CommonMark consumer-oracle cases. The count changed because Markdown parser
behavior moved out of the dependency-free runtime validator into stronger
consumer-relative tests; removed runtime-parser tests are not silently counted
as preserved proof.

For re-review, repeat the original probes where applicable and use the same
finding discipline: a changed implementation is not proof until the external
counterexample no longer reproduces on the reviewed revision.

## Reconciliation of the 1a0720 rereview findings

The rereview of `1a0720fad51c0e5057020b71dbc0ab4711f4d8ff` reported three
remaining relations:

| Rereview finding | Reconciliation | New discriminant |
| --- | --- | --- |
| R1 / F06 | Removed arbitrary Markdown parsing from the dependency-free runtime validator. Constitutive discovery routes are explicit structural owner paths; a test-only `markdown-it-py` CommonMark oracle now validates active package-local links, active discovery links and the five rereview counterexamples. | independent consumer parser, not another runtime regex layer |
| N1 | `--preview-adapter` renders and returns before loading/interpreting `state/INSTANCE.json`. Mutation paths still reject unsupported schema/host owners. | future/foreign INSTANCE + preview another target succeeds with no writes |
| N2 | Delivery regression now checks strict ordering of confirmation, add, commit, push, remote readback and reentry markers on README, INSTALL and adapter README. | causal order rather than substring presence |

The runtime validator remains dependency-free. The full suite installs
`requirements-test.txt` and uses the CommonMark dependency only as an
independent test oracle.

The current canonical proof target carries **53 tests** across all 8 Python 3.11–3.14 ×
Ubuntu/Windows jobs. Validator, suite and CI must belong to the exact canonical
SHA being rereviewed; proof from the reconciliation branch remains genealogy.


## Reconciliation of the 82078ed rereview findings

The rereview of `82078ed26cb3b6bacee74951fb727e31adba0d16` confirmed the
previous runtime/product seams remained closed, but exposed three proof
relations in the new consumer oracle:

| Rereview finding | Reconciliation | Discriminant |
| --- | --- | --- |
| A / consumer-link coverage | The CommonMark oracle now observes the rendered HTML surface rather than only `link_open` Markdown tokens, so active raw-HTML anchors and Markdown links share the same consumer check while fenced examples remain non-active. | rendered `<a href>` active + fenced raw HTML inactive |
| B / discovery evidence composition | Constitutive discovery proof now composes active AGENTS link, actual Markdown owner heading, uniqueness, and the explicit simple-ASCII fragment contract. A matching heading string inside fenced code cannot satisfy the proof. | real Markdown heading + fenced/raw-HTML-heading decoy |
| C / oracle reproducibility | The test environment pins both `markdown-it-py==4.2.0` and the resolved `mdurl==0.1.2` dependency. | exact parser dependency pair |

These changes strengthen existing oracle cases, so the suite remains **53
tests** rather than increasing its count. The important delta is proof depth:
individually true observations no longer stand in for the composed relation
they are meant to establish.

The next reviewer should falsify the composed consumer/discovery relation
directly, not infer closure from the unchanged test count.


## Reconciliation of the 0d1fa97 whole-system review findings

The deep review of
`0d1fa97f5c09a3794a4aa748d7ebfa2caff53e0a` returned
`changes_required` while preserving the product architecture. The current
source reconciles the reported mechanical/proof seams without adding a
supervisory controller:

| Finding | Reconciliation | Discriminant |
| --- | --- | --- |
| F01 / concurrent INSTANCE writers | Mutating configurator commands acquire `state/.INSTANCE.write.lock` before reading INSTANCE and hold ownership through publication. A competing/stale lock fails visibly; uncertain stale ownership is reconciled explicitly rather than auto-deleted. | second cooperative writer cannot complete a stale read-modify-write; explicit stale-lock removal + reread recovers |
| F02 / historical receipt validity | Automatic return to `installed_operator_confirmed` is allowed only from a still-applicable confirmed/local-drift state. Explicit `unknown` is not overwritten by historical byte equality. | A→B→A without invalidation still restores; A→unknown→A does not |
| F03 / bridge target attribution | Repository identity is extracted only from the recognized constitutive bridge header. Unrecognized/custom forms degrade to `unknown`; later examples/comments are non-authoritative. | custom body + fake recognized comment does not create known target |
| F04 / anchor collision proof | Constitutive routes use explicit prefixed custom anchors adjacent to the intended owner headings. The CommonMark oracle verifies the active route and explicit rendered anchor rather than automatic heading-slug uniqueness. | prior colliding heading cannot steal the constitutive route |
| F05 / remote readback | Documentation requires push → fresh fetch of the selected branch → fetched commit identity comparison → readback from `FETCH_HEAD`. | local remote-tracking cache is no longer called fresh remote observation |
| M01 / template-like user data | Template fields are substituted in one pass over the original template. Inserted values are never reinterpreted as placeholders. | literal `{{DATE}}` in user data survives |
| P01 / delayed operator confirmation | Confirmation requires the digest of the bridge incarnation that was actually delivered. If the current bridge differs, the late response is rejected and the current bridge must be delivered again. | delivered A + current B cannot confirm B with A's response |

The suite now contains **58 tests**: 38 configurator, 17
structural/receipt/drift/provenance/delivery validator and 3 CommonMark
consumer-oracle cases. The writer lock is intentionally narrow: it serializes
cooperating filesystem configurators around the single INSTANCE owner; it is
not narrated as a universal database transaction or as coordination for every
possible external API writer.

The reviewer should rerun the original counterexamples on the exact resulting
canonical SHA. In particular, F01 must produce either preserved state or an
explicit writer conflict, F02 must preserve the positive A→B→A control, and
F05 should distinguish a fresh fetched remote ref from remembered tracking
state.

## Reconciliation of the c7d2d9c rereview residuals

The rereview of
`c7d2d9c5e95fab61fea6323c0218d9947f991652` confirmed that the prior
architecture and primary fixes hold, but returned four local
`changes_required` residuals. The current source reconciles them at their first
losing seams:

| Residual | Reconciliation | Discriminant |
| --- | --- | --- |
| N01 / generated next action | `scripts/configure.py` emits the complete confirmation command including the exact delivery digest it just authorized. | generated command contains `--confirm-host-installation` plus `--expected-bridge-sha256 <current configured digest>` |
| N02 / AGENTS delivery discovery | `AGENTS.md` routes confirmation to the stable `INSTALL.md#receipt-publication-and-fresh-readback` owner before suggesting remote reachability. | confirmation -> active owner route -> remote reentry; INSTALL retains commit/push/fetch/commit-identity/readback contract |
| N03 / anchor-owner proof composition | The CommonMark consumer records ordered active anchor/heading events and proves the intended pair on one rendered surface. | wrong active anchor + fenced raw-source decoy cannot satisfy anchor->owner proof |
| N04 / drift promoted to host delivery | `confirmation_bridge_sha256` is emitted only when local bytes equal `INSTANCE.configured_bridge_sha256`; drifted bytes are reported as `observed_local_bridge_sha256` and host delivery is explicitly blocked. | refresh preserves recorded configured digest while drifted local artifact cannot acquire delivery authority |

These changes deliberately **do not** add a controller, transaction manager,
host taxonomy or new state machine. They carry existing semantic relations into
the consumer that needs them and leave visible conflicts to the present
LLM/operator for situated reconciliation.

The native suite remains **58 tests**. Rereview should rerun N01–N04 against
the exact canonical SHA produced from this reconciliation and should continue
to preserve the already-closed F01–F05, M01 and P01 controls.

## Reconciliation of the affbc66b rereview residuals

The rereview of
`affbc66b039739f1c9f7fb5f7261b2c8e2ff32c2` confirmed N01–N04 and all earlier
mechanical relations, but exposed one remaining proof seam plus minor current
wording drift:

| Residual | Reconciliation | Discriminant |
| --- | --- | --- |
| N05 / anchor-owner projection dropped intervening rendered content | The CommonMark consumer now records non-whitespace rendered content as an owner event. An anchor satisfies the owner relation only when the next relevant rendered event is the intended heading. | active anchor + intervening rendered paragraph + expected later heading must not form the constitutive pair |
| D01 / abbreviated confirmation wording | Current README, INSTALL and adapter summaries name the generated confirmation command as `--confirm-host-installation` plus the delivered digest required by `--expected-bridge-sha256`. | no current operational shorthand presents the bare flag as the complete executable confirmation effect |

This reconciliation changes proof fidelity and current delivery wording only.
The reviewer should preserve the closed F01–F05, M01, P01 and N01–N04 controls,
rerun the N05 counterexample on the exact resulting SHA, and move observation
once more to a materially independent surface before returning `no_change`.

## Intentionally deferred effects
External review is selected before:

```text
v0.6.0 tag / GitHub Release
existing user-instance migration
configured bridge replacement
ChatGPT host bridge update
website / announcement
behavioral-assimilation claim
```

After review, reconcile only findings that materially change the source, run
proof on the resulting canonical revision, and only then decide the immutable
`v0.6.0` release.
