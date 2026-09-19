# Adoption guide

Adoption makes the kernel's operating relation reachable in a conversational
environment and keeps useful context and learning available for later work.

## Recognize the receiving relation

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
do not.

When the relation is `kernel_chat`, continue with the
[chat setup guide](CHAT_SETUP.md).

## What complete adoption makes true

A persistent conversational adoption establishes:

```text
one reachable kernel source
+ one installed conversational entry pointing to that source
+ a place for current context and source relations when they are needed
+ a way for reusable competence learning to remain reachable later
```

The source can be a repository, project/knowledge space, filesystem, connector
or another durable receiver-native mechanism.

An attachment-only conversation can use the kernel now but does not provide
cross-conversation persistence by itself.

## Use the receiver's actual means

The assisting AI performs authorized effects through capabilities it actually
has. Account settings, credentials and other operator-owned actions remain with
the operator.

Keep distinct:

```text
source read
!= source write
!= filesystem / terminal / code execution
!= account-setting authority
!= installed instructions
!= observed behavior
```

If a required capability is absent, expose the smallest missing action rather
than simulating it.

## Private and public continuity

Use a private persistent source for private work. Use a public source only for
content deliberately public.

Keep the upstream/source revision distinguishable from the user's evolving
context and local competence learning.

A project may be present at adoption or added later. It is context in which the
kernel works, not the identity of the kernel.

## Host-specific mechanics

The portable adoption contract does not require one provider's installation
procedure.

For the current ChatGPT Git/Python implementation use
[INSTALL.md](../INSTALL.md) and the
[ChatGPT adapter guide](../adapters/chatgpt/README.md). Those documents own
configured-entry provenance, host confirmation, receipt publication, update and
recovery mechanics.

Another conversational host uses its own persistent-instruction and source
mechanisms while preserving the same kernel owners and effect distinctions.

## Package source and installed entry evolve separately

A newer upstream source can change kernel knowledge without requiring an
instruction replacement. An instruction contract can change without changing a
user's current context.

Therefore keep separate:

```text
upstream/source revision
available conversational-entry version
configured entry
installed host instructions
reachable user state
observed conversational behavior
```

Inspect or update only the relation that can materially change the present
result.

## Continue normally

Bring the real topic, question or activity. Pertinent competences participate
where they change the movement, and each final response exposes a compact
competence trace.

The trace is continuity and observation, not a permanent activation list. A
later turn can preserve, drop or add competences as the field changes.

See the [User guide](USER_GUIDE.md) for ordinary use and evolution.
