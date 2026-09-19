# Adoption guide

Adoption makes the kernel's working knowledge usable in your environment and
keeps useful changes available for later work.

## Choose the relation you need

### Recognize the receiving relation before choosing the mechanics

```text
conversational AI
+ persistent/custom operating instructions or equivalent entry
+ reachable persistent kernel source
-> kernel_chat

AI agent / harness
+ durable project workspace/filesystem as its continuing work surface
-> MAIOS Project Kernel
```

The receiver's actual relation determines the carrier. Provider and model names
do not. A project or knowledge area can be the persistent source of a
conversation without turning that conversation into a project-native agent
harness.

When that relation is `kernel_chat`, continue with the
[chat setup guide](CHAT_SETUP.md).

### Use the app's actual means

The shared chat route uses kernel files, persistent instructions and a place
for current context and evolving methods. The setup guide includes an entry
text and Claude Projects instructions. The ChatGPT repository helper has its
own complete [installation procedure](../INSTALL.md).

The assistant performs the steps available through its tools. Where account
settings, repository access or file placement need the operator, it supplies
the exact action and complete text or file. An attachment-only session can use
the supplied methods now; persistence across sessions comes from a saved,
reachable source in the selected app scope.

### Study and adoption

A request to understand the product calls for an explanation grounded in its
methods and the operator's work. A request to install selects setup. Adoption
does not require a separate general review, and reading the README does not
itself change an account or repository.

### Private continuity instance

For non-public work, use a private project space or private standalone
repository under your control. A public GitHub repository cannot be made
private by creating a fork. Keep the source revision of the kernel distinct
from your evolving local knowledge.

### Public continuity instance

A public fork is suitable when its contents are deliberately public.

### Instance with an initial project

A project may be supplied at setup or added later. It is one context in which
the kernel works, rather than a prerequisite for the kernel.

## What configuration creates

The shared chat route makes the constitutive kernel owners reachable, saves the
portable conversational entry at the app's instruction surface, and gives
current context, source relations and evolving competences a location that later
conversations can reach.

The Git/Python ChatGPT helper additionally manages:

```text
state/INSTANCE.json
  package, repository, configured bridge and reported host-installation identity

state/CURRENT.md
  current work and the reasons needed to resume it

state/SOURCES.md
  original sources and reusable methods

adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md
  generated local ChatGPT entry text
```

A project-file setup uses its saved files and app scope. It does not manufacture
a ChatGPT `INSTANCE` receipt for another application.

## ChatGPT activation

The operator saves the configured entry in ChatGPT. The assistant retains the
`confirmation_bridge_sha256` emitted when that exact entry was delivered.
After the operator confirms saving it, the helper records the report with
`--confirm-host-installation` and `--expected-bridge-sha256` for that delivery.

The helper rejects a delayed report when a different bridge is now configured.
Complete the [receipt publication and fresh readback](../INSTALL.md#receipt-publication-and-fresh-readback)
before a new chat relies on the remote record. The
[adapter guide](../adapters/chatgpt/README.md) preserves the full command and
recovery contract.

## Package update, available bridge and configured bridge are different

An upstream source update can improve methods without changing the app's entry.
Compare the proposed change with your saved methods and preserve useful local
learning. Updating a source, replacing a bridge and saving instructions in an
account are distinct actions.

For the ChatGPT helper:

- `--preview-adapter` inspects a candidate without changing the instance.
- `--refresh-instance` refreshes package observations while preserving the
  configured bridge and reported installation. It observes local drift rather
  than accepting new bridge bytes.
- `--replace-adapter` generates a replacement; the operator subsequently saves
  the delivered text in the account and confirms that exact delivery.

Legacy configured-template provenance can remain `unknown`. Existing valid
v1 receipts remain readable when newer optional identity fields are absent.
A known repository mismatch requires deliberate reconciliation. The
[installation guide](../INSTALL.md) and [architecture](ARCHITECTURE.md) retain
these mechanics and their evidence boundaries.

## Source contact

A relevant upstream difference can improve the local kernel. Inspect the
source when it can change the work, preserve the observation when useful, and
select updates deliberately. The current source-contact method remains in
[AGENTS.md](../AGENTS.md).

## Continue normally

Bring the real topic, question or activity. The kernel's methods participate
where they help understand and carry out that work. Keep reusable learning in
the method that should use it and current context in the place used for reentry.
See the [User guide](USER_GUIDE.md).
