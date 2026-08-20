# Codex Handoff — Portable Working Incarnation Validation

Date: 2026-08-20
Target repository: `GrazianoGuiducci/Meta_Semantic_Kernel`
Target branch: `tm9/joint-kernel-field`
Accepted main state: `0.2.0` at merge base `ca797b0b79952832e6a488da52230210f9798cf4`

## Role

Act as TM9/Codex filesystem-native implementation/verifier for the current shared project field.

Do **not** redesign the kernel from scratch, regenerate the package through RepoKernel, merge to `main`, publish a product, change `tm7/chatgpt`, or treat passing static checks as behavioral proof.

The current branch contains:

```text
TM9 independent/non-coincident field contribution
TM9 imported alpha package under contributions/tm9/
ChatGPT first-person contribution
portable function matrix
portable operational-continuity regression
first implementation convergence
first portable working skeleton at repository root
```

## Read order

1. `CURRENT_STATE.md` on branch — accepted project state remains 0.2.0.
2. `docs/FIRST_IMPLEMENTATION_CONVERGENCE.md`
3. `docs/PORTABLE_FUNCTION_MATRIX.md`
4. `contributions/chatgpt/CHATGPT_FIRST_PERSON_KERNEL_CONTRIBUTION.md`
5. `docs/PORTABLE_OPERATIONAL_CONTINUITY.md`
6. root working candidate:
   - `kernel/`
   - `state/`
   - `operations/`
   - `evolution/`
   - `adapters/chatgpt/`
   - `evals/cases.json`
   - `scripts/validate.py`
7. only then compare with `contributions/tm9/maios-conversation-kernel-candidate/` where needed.

## Task A — deterministic structural validation

From a clean checkout/worktree of the exact branch, run:

```bash
python scripts/validate.py
```

Preserve the exact JSON output.

If it fails because of a deterministic defect in the new working candidate, fix the **smallest owner-local defect on this branch only**, rerun, and record before/after.

Do not weaken a validator merely to make it pass. If a check is wrong, explain the semantic reason before changing it.

## Task B — private-residue check

Independently inspect the portable roots:

```text
kernel/
state/
operations/
evolution/
adapters/
evals/
```

Confirm whether runtime use requires any originating private path, private repository, hidden transcript, private permission, TM1/TM9 executor identity, MAIOS/D-ND project state or local machine path.

Source attribution or genealogy is different from a runtime dependency; distinguish them.

## Task C — alpha subtraction comparison

Compare the new smaller working candidate with:

```text
contributions/tm9/maios-conversation-kernel-candidate/
```

Do not ask which has more files. Ask:

```text
which material function present in the alpha is absent from the smaller working candidate?
would that absence change a real result, reentry, operation, recovery, evolution or proof?
is the missing item a function, implementation convenience, RepoKernel morphology, product residue or still-unknown?
```

Pay particular attention to:

```text
host adapter contract
capability attestation
source/state reconstruction
positive/negative evals
static validation
reversible evolution
representation adequacy / retained unknown
user-owned state
```

Also test the inverse: identify alpha structure that the smaller candidate removes without losing an independently useful function.

## Task D — operational-organ sanity review

Review:

```text
operations/CURRENT_STATE.md
operations/flows/README.md
operations/requests/README.md
operations/receipts/README.md
operations/RECOVERY.md
```

Check that they can represent, without assuming a daemon/agent:

```text
active flow
cursor/checkpoint
pending decision/result/effect
stored schedule without installed scheduler
replaceable executor route
bounded request/result handoff
receipt/recovery/replay protection
executor loss without continuity loss
```

Flag any relation that requires deterministic schema/code now. Do not generate schema merely for completeness.

## Task E — adapter/host boundary

Check that the ChatGPT Custom Instructions source:

```text
- remains <= 1500 characters for the install text;
- points only to user-configurable fork coordinates;
- does not claim source presence == installation/activation;
- does not imply persistent shell/background execution;
- makes operational reentry conditional rather than always-on.
```

Do not install it in ChatGPT; installation is an operator/host effect later.

## Task F — result classification

Return one bounded classification for the working candidate:

```text
structurally_valid
structurally_valid_with_warnings
needs_small_fix
material_function_missing
architecture_regression
inconclusive
```

This classification is not a project-version promotion and not portability/behavioral validation.

## Receipt

Write the result on the same branch as:

```text
contributions/tm9/PORTABLE_WORKING_VALIDATION_RECEIPT.md
```

Include:

```text
repository + branch
exact entering commit
exact resulting commit if you changed anything
commands actually run
validator output
files changed, if any
alpha functions found missing or intentionally removed
operational-organ findings
adapter findings
residue findings
classification
remaining unknowns
recommended next real test
```

Commit/push only to `tm9/joint-kernel-field`.

Do not update root project `CURRENT_STATE.md` or create 0.3.0. ChatGPT will read the receipt as the next non-coincident contribution and decide whether it changes the shared project resultant.
