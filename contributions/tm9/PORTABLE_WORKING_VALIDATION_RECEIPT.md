# TM9/Codex Receipt — Portable Working Incarnation Validation

Date: 2026-08-20  
Repository: `GrazianoGuiducci/Meta_Semantic_Kernel`  
Branch: `tm9/joint-kernel-field`  
Entering commit: `13a9c29f34d37b19987268977fd1ca51be6b3fd1`  
Resulting implementation commit: `c8a197736612ed6308f05be64bd80bbc77795e3c`  
Accepted project state left unchanged: `0.2.0`

## Scope and boundary

TM9/Codex validated the root Portable Working Incarnation, compared it by function with the imported TM9 alpha and made one bounded correction on the joint branch.

No merge to `main`, project-version promotion, RepoKernel regeneration, public product publication, Custom Instructions installation or change to `tm7/chatgpt` occurred.

## Commands actually run

```text
git status --short --branch
git remote -v
gh auth setup-git
git fetch origin
git merge --ff-only origin/tm9/joint-kernel-field
python scripts\validate.py
rg -n -i --glob * <private-residue patterns> kernel state operations evolution adapters evals
rg -n -i --glob * <path/credential/binding patterns> kernel state operations evolution adapters evals
python -c <Custom Instructions install-text character count>
python contributions\tm9\maios-conversation-kernel-candidate\scripts\validate_kernel.py
python -c <alpha/new eval-id comparison>
git diff --check
python scripts\validate.py
```

The GitHub workspace token policy was used for authenticated remote access. No token value was printed or stored in the repository.

## Validator output

The entering candidate and the corrected candidate both returned:

```json
{
  "schema": "meta-semantic-kernel.structural-validation.v0",
  "valid": true,
  "proof_scope": "source_structure_and_claim_boundaries_only",
  "behavior_verified": false,
  "portability_verified": false,
  "errors": [],
  "warnings": []
}
```

The imported alpha validator also returned `valid: true` with no errors. That result was used only to establish a clean comparison baseline.

## Files changed

```text
evals/cases.json
  added C7-scoped-verified-limit

contributions/tm9/PORTABLE_WORKING_VALIDATION_RECEIPT.md
  this receipt
```

## Alpha subtraction findings

### Material function missing at entry and restored

The smaller candidate preserved open possibility beyond the current map but had dropped the alpha's negative discriminant for a **verified current limit**.

That loss matters because an open horizon must not become permission to ignore a real present host/surface limit, just as a present limit must not become a universal or future boundary.

`C7-scoped-verified-limit` now tests both sides:

```text
respect and scope a verified present limit
!=
ignore it in the name of openness
!=
universalize it across hosts, later states or possible relations
```

The case remains `not_run`; adding it restores the falsifiable proof obligation, not behavioral proof.

### Functions retained in the smaller candidate

```text
host adapter separated from kernel and installation
user-configurable repository binding
host capability/effect distinction
selective source/state reconstruction
positive, failure and negative discriminants
static source/claim-boundary validation
reversible evolution and de-kernelization
representation adequacy and retained unknown
user/fork-owned semantic and operational state
active/cold persistence distinction
```

### Alpha structure intentionally not carried

```text
15-family generated Project Meta-Faculty
Problem/Possibility Seed as product movement
.repokernel generator morphology and generation receipts
MAIOS Conversation Kernel product/release identity
public publication/site sequence
capability schema before deterministic exchange requires it
bootstrap source atlas before real fork bindings exist
```

No independently useful current function was found to depend on those forms. The generated family map remains useful evidence and discovery coverage, but adopting it into the active core would reintroduce the representation as the field. Machine-readable capability/source schemas can be added later if a concrete adapter, exchange or validator needs them.

## Operational-organ findings

The current file-based organ can represent the requested relations without assuming an agent, daemon, worker or scheduler:

```text
active flow                       -> flow status + CURRENT_STATE pointer
cursor/checkpoint                 -> flow cursor_or_checkpoint
pending decision/result/effect    -> pending_relation + review/effect boundary
stored schedule without scheduler -> trigger relation + executor/capability state;
                                     installed_schedules remains none_attested
replaceable executor route        -> optional route + RECOVERY executor replacement
bounded request/result handoff    -> request_id/flow_id causal envelope
receipt/recovery/replay protection-> receipt contract + latest-effect inspection
executor loss                     -> flow/cursor/pending relation survive route loss
```

No deterministic schema or executable code is required yet. The first concrete cross-executor exchange, installed schedule or replay-sensitive effect may create that requirement; until then, generating schemas would add form without observed implementation need.

## Adapter findings

The ChatGPT install text is `1209` characters, within the `1500`-character target.

It:

- uses only `<YOUR_GITHUB_USER>/<YOUR_REPOSITORY>` fork coordinates;
- keeps source, configuration, installation, repository access and behavioral activation distinct;
- assumes no persistent shell, hook, scheduler or background execution;
- loads operational state only when unfinished causal work can change continuation;
- keeps effect authority absent by default and effect-specific when operative.

Installation was not attempted; that remains an operator/host effect.

## Private-residue findings

No originating private path, private repository coordinate, credential, token marker, TM executor identity, local machine path, hidden transcript or operator-specific operational state is required by:

```text
kernel/
state/
operations/
evolution/
adapters/
evals/
```

The only D-ND/MAIOS text found in the portable roots is the negative setup of `P0-no-private-runtime-dependency`; it names what must be absent and is test genealogy, not a runtime dependency.

Root `README.md` and root `CURRENT_STATE.md` still describe the accepted shared project state rather than a release/install surface. This is consistent with keeping project `0.2.0` unchanged, but it means this branch is not yet a self-contained public release package from its root landing page.

## Classification

```text
structurally_valid_with_warnings
```

The warning is not a static defect. Behavioral activation, operational continuity and cross-host portability remain unverified, and the root project landing/release layer is intentionally not promoted.

## Remaining unknowns

```text
- whether a fresh ChatGPT instance reenters selectively from a user-owned fork;
- whether ordinary bounded work remains direct after adapter installation;
- whether one persisted active flow restores causal continuation in practice;
- whether a prior/prepared effect is not replayed after fresh reentry;
- when real host capability attestation needs its first durable representation;
- whether a second host preserves the same useful core relation;
- whether later use simplifies or dissolves any current organ boundary.
```

## Recommended next real test

Create a disposable user-owned test fork/repository whose default branch contains this working incarnation, configure the ChatGPT adapter to that fork, then use a fresh conversation for one paired test:

```text
control: C0 + O0
  ordinary bounded work stays direct and operational state remains cold

continuity: P1 + O1 + O2
  one deliberately persisted active flow is recovered from the fork,
  its cursor/pending relation resumes without archive preload,
  and a historical prepared effect is not replayed without current evidence/authority
```

This is first-person host use of the shared artifact, not external validation. Preserve the observed behavior and any actual effect as a bounded receipt; do not promote `0.3.0` merely because the test runs.
