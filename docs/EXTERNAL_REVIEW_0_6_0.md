# kernel_chat 0.6.0 — External Review Brief

```text
source_version: 0.6.0
review_state: findings_reconciliation_candidate
canonical_repository: GrazianoGuiducci/kernel_chat
review_target: exact current main commit checked out by the reviewer
latest_tagged_distribution: v0.5.0
v0.6.0_release: intentionally not created before review
```

## Purpose

Review the current canonical source of `kernel_chat 0.6.0` before a numbered
release is selected. Pin the exact revision you inspect with `git rev-parse HEAD`.
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

```bash
python scripts/validate.py
python -B -m unittest discover -s tests -v
```

For a clean checkout the expected repository-level relation is:

```text
validator: valid=true, errors=[], warnings=[]
tests: 32 configurator + 22 validator/drift/provenance/reachability/delivery = 54
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

The validator should reject malformed multiline Markdown links in active prose
without treating the same syntax inside fenced or inline code as an active link.

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
The current reconciliation candidate addresses each finding in its owning seam:

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

The candidate suite now contains **54 native tests**: 32 configurator and 22
validator/drift/provenance/reachability/delivery cases. The branch proof is not
release proof: after canonical reconstruction, the same suite and CI must pass
on the exact new canonical SHA.

For re-review, repeat the original probes where applicable and use the same
finding discipline: a changed implementation is not proof until the external
counterexample no longer reproduces on the reviewed revision.

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
