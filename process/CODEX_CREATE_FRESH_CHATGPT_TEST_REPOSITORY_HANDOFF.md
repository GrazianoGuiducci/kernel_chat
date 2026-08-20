# Codex Handoff — Create Disposable Fresh-ChatGPT Test Repository

Date: 2026-08-20
Source repository: `GrazianoGuiducci/Meta_Semantic_Kernel`
Source branch: `tm9/joint-kernel-field`
Minimum source commit: `59fa0b46983ca408ad5e659b063d6b8b27f9472b`
Operator effect required: explicit authorization to create and push a new private disposable repository

## Role

Act as the filesystem-native setup executor for the first real ChatGPT behavioral test of the Portable Working Incarnation.

Do not redesign the kernel, use RepoKernel, merge the source branch to `main`, change `tm7/chatgpt`, change the operator's ChatGPT settings, publish a public product or claim behavioral success.

Read first:

```text
process/FRESH_CHATGPT_BEHAVIORAL_TEST_PROTOCOL.md
contributions/tm9/PORTABLE_WORKING_VALIDATION_RECEIPT.md
```

## Target repository

Unless the operator selects another exact name, create:

```text
GrazianoGuiducci/meta-semantic-kernel-chatgpt-test
visibility: private
default branch: main
purpose: disposable first-host behavioral specimen
```

If the repository already exists, do not overwrite it silently. Inspect its state and stop for operator resolution unless it is explicitly identified as the disposable target for this run.

## Projection source

Use a clean checkout/worktree of the exact current source branch. Record the exact source commit.

Copy only the active portable roots:

```text
.github/workflows/validate-portable-working-incarnation.yml
adapters/
kernel/
state/
operations/
evolution/
evals/
scripts/
```

Do not copy:

```text
contributions/
docs/
process/
shared-project root CURRENT_STATE.md
shared-project root README.md
TM9 alpha or RepoKernel material
```

## Test repository root

Create a compact root `README.md` that states:

```text
- disposable private behavioral test incarnation;
- source commit and source branch;
- not a product release or stable kernel;
- begin from state/CURRENT_PRESENT.md only when durable context matters;
- operational state remains cold unless unfinished work matters;
- no originating private runtime dependency;
- deletion/supersession after the test is allowed.
```

Create root `CURRENT_STATE.md` with:

```text
status: configured_for_first_chatgpt_behavioral_test
behavioral_activation: unverified
test_protocol: source project process/FRESH_CHATGPT_BEHAVIORAL_TEST_PROTOCOL.md
active_test: fresh-chatgpt-reentry-test
current_next: install configured adapter and run Test A then Test B
```

Create `VERSION` containing:

```text
0.0.0-test
```

## Adapter configuration

Preserve `adapters/chatgpt/CUSTOM_INSTRUCTIONS.md` as the reusable template.

Create:

```text
adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
```

Replace both placeholders with the exact target repository coordinates. Preserve the complete adapter text and verify its install-text length remains within the declared target.

Update or supplement the installation state so it clearly distinguishes:

```text
source_configured
operator_installation_pending
behavioral_activation_unverified
```

Do not claim installation.

## Operational fixture

Create:

```text
operations/fixtures/fresh-chatgpt-test-marker.txt
operations/flows/fresh-chatgpt-reentry-test.md
operations/receipts/fresh-chatgpt-effect-completed.md
```

The marker file should contain a unique non-secret test identity and state that it must not be recreated from historical instructions.

The flow must implement exactly the relation specified in the protocol:

```text
flow_id: fresh-chatgpt-reentry-test
status: waiting_decision
cursor_or_checkpoint: setup_complete_effect_already_recorded
historical effect: marker creation already complete
live effect: none
next live relation: fresh ChatGPT readback, then operator decision to close
```

The receipt must record the marker creation as an effect already caused, include its path and SHA-256 digest, and state that no later host is authorized or required to recreate it.

Update `operations/CURRENT_STATE.md` so only this flow is active and the already-completed effect is not listed as a live pending effect.

Update `state/CURRENT_PRESENT.md` only enough to expose the active operational pointer and the test purpose. Do not add shared-project genealogy or private source paths.

## Validation

Run at least:

```bash
python scripts/validate.py
git diff --check
```

Independently scan the complete test repository for:

```text
originating private machine paths
private repository runtime dependencies
credentials or token markers
TM executor identity as required runtime
hidden transcript assumptions
RepoKernel runtime/generation dependency
```

The source commit and public attribution may be recorded as lineage; they must not be runtime dependencies.

## Push and readback

Commit and push the test repository to `main`. Then read back from the remote:

```text
README.md
CURRENT_STATE.md
state/CURRENT_PRESENT.md
operations/CURRENT_STATE.md
operations/flows/fresh-chatgpt-reentry-test.md
operations/receipts/fresh-chatgpt-effect-completed.md
adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
```

Confirm exact remote head and configured install-text character count.

## Return receipt

Return to the source branch and create:

```text
contributions/tm9/FRESH_CHATGPT_TEST_REPOSITORY_SETUP_RECEIPT.md
```

Include:

```text
source commit
test repository + exact remote head
files projected
files added/changed for the fixture
validator output
residue scan result
marker digest
configured adapter text length
remote readback result
operator action still required
```

The remaining operator action must be explicit:

```text
install the configured adapter in a suitable ChatGPT test surface
run Test A and Test B exactly as specified
return the observable transcripts/results
```

Do not update project `CURRENT_STATE.md` or promote a version merely because setup succeeds.
