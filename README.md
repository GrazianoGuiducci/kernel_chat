# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.

It gives a conversational AI a persistent operating source: kernel logic,
competences and metacompetences, current context, source relations and the
learning that changes how later work is understood and carried out.

```text
persistent/custom instructions or equivalent entry
+ a kernel source the conversation can reach
+ current context and owner-native sources
+ competences and metacompetences
-> the conversational AI enters kernel_chat
-> pertinent competences participate in the work
-> reusable learning returns to the owner that must act differently later
```

The model or provider is not the kernel. The repository, project knowledge,
connector, filesystem or other persistence mechanism is not the kernel either.
They are means through which the same semantic operating relation can be
incarnated.

## What is here

[AGENTS.md](AGENTS.md) is the entry and routing surface.

[Core](kernel/KERNEL.md) carries the operating relation: present context,
source distinction, situated movement, selective reentry and observation.

[Competence](kernel/COMPETENCE.md) carries how usable knowledge participates,
combines, deepens, forms and learns.

[FDLA](kernel/FDLA.md) corrects an interpretation when the acting system has
narrowed or substituted the relation it is trying to understand.

[Evolution](kernel/EVOLUTION.md) returns material consequences and reusable
learning to the owner that should behave differently next time.

`state/CURRENT.md` carries the current relation needed for continuation.
`state/SOURCES.md` points to owner-native sources and reusable knowledge.

The persistent conversational entry is
[adapters/conversational/INSTRUCTIONS.template.md](adapters/conversational/INSTRUCTIONS.template.md).
It points the receiving chat into these owners without copying the whole kernel
into provider settings.

## When this is the receiving relation

```text
conversational AI environment
+ persistent/custom operating instructions or an equivalent entry
+ a persistent kernel source the conversation can reach
-> kernel_chat can be incarnated in that environment
```

The environment supplies its own means. It may expose project knowledge,
repository access, files, connectors or another persistent source. The source
references can be translated to that environment while preserving the same
owners and relations.

When the AI instead operates as an agent inside a durable project
workspace/filesystem that it owns as its continuing work surface, the
project-native carrier is
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel).

## What happens in use

Work begins from the present relation rather than from a fixed workflow.

```text
present relation
+ still-valid determinations
+ pertinent owner-native sources
+ competences that can materially change the movement
+ actual means and authority
-> situated movement
-> resultant
-> causal readback and reusable learning
```

A competence can make another competence pertinent. Several competences can
participate together without becoming one controller. A result can improve the
current work, change an existing competence, form a capability that did not
previously exist, or produce `no_change`.

Continuity is part of this relation but is not its whole identity. Decisions,
reasons, sources, unfinished relations and learned methods can remain reachable
across conversations without forcing every previous representation back into
the present.

## Set it up

The [chat setup guide](docs/CHAT_SETUP.md) maps the same conversational entry
onto the instruction and source mechanisms that actually exist in the receiving
environment.

For the current ChatGPT repository implementation, [INSTALL.md](INSTALL.md)
and the [ChatGPT adapter](adapters/chatgpt/README.md) provide the
Git/Python/configuration and host-receipt mechanics. Those mechanics are one
host incarnation, not the identity of `kernel_chat`.

After installation, bring the actual work. The kernel reaches additional
knowledge only when it can change the present movement, and reusable learning
returns to the competence or owner that should use it later.

The [User guide](docs/USER_GUIDE.md) covers continuation, sources, competences
and evolution in ordinary use. The [Adoption guide](docs/ADOPTION_GUIDE.md)
covers the receiving relation and setup effects.

## Source

[Architecture](docs/ARCHITECTURE.md) ·
[Current source state](CURRENT_STATE.md) ·
[Contributing](CONTRIBUTING.md) ·
[Changelog](CHANGELOG.md) ·
[Source version](VERSION) ·
[Apache License 2.0](LICENSE)

Copyright 2026 Graziano Guiducci.
