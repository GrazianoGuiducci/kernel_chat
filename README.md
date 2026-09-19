# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.

It lets a conversation work through owner-native sources, competences and
metacompetences that can change through use and participate differently in
later work.

```text
present relation
+ owner-native sources
+ pertinent competences
-> situated work
-> resultant
-> causal readback
-> reusable difference changes the competence that should act differently
-> later non-identical work can begin from that changed competence
```

A competence is reusable operating knowledge: a way of understanding or doing
work that becomes pertinent when the present situation calls for it. Several
competences can participate together, one can make another pertinent, an
existing competence can deepen, and a genuinely missing capability can form.

Files, state objects and instructions are persistent incarnations of this
operating relation. They make the kernel reachable again; they are not the
kernel reduced to storage.

## What changes when it operates

The kernel keeps the work, its sources and the competences acting on it in one
causal relation. A useful result can therefore change more than the current
answer.

For example:

```text
task A:
a user corrects the system for mixing a source fact with its own inference
-> the reusable distinction changes the source-discrimination competence
-> that changed competence is preserved in the user-owned kernel source

task B, later and materially different:
the same distinction becomes pertinent
-> the AI keeps source fact and its own inference separate
-> the user does not have to reconstruct the earlier correction
-> the changed handling of task B is the observable result
```

The persistent source carries the competence between conversations. The stored
representation is the carrier; the later changed handling is the readback that
shows the competence participated. Later use can preserve, refine or revise it
again.

Each final user-facing response closes with a compact
[competence trace](kernel/KERNEL.md#kernel-chat-competence-trace): the
competence owners that materially formed the response and any possibilities
that materially emerged. The next turn recomputes pertinence from the changed
field.

## When this is the receiving relation

```text
conversational AI environment
+ persistent/custom operating instructions or an equivalent entry
+ a persistent kernel source the conversation can reach
-> kernel_chat can be incarnated in that environment
```

The receiving environment supplies its own means. A persistent source may be a
repository, project/knowledge surface, files or another durable source the
conversation can reach. The kernel supplies the operating relation and the
owner map; the host supplies the mechanism through which those owners become
reachable.

When the AI instead operates as an agent inside a durable project
workspace/filesystem that it owns as its continuing work surface, the
project-native carrier is
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel).

## Follow the operating sources

[AGENTS.md](AGENTS.md) is the portable entry and routing surface.

[Core](kernel/KERNEL.md) carries the present relation, source distinction,
situated movement, selective reentry, mobile observation and competence trace.

[Competence](kernel/COMPETENCE.md) carries how usable knowledge participates,
combines, deepens, forms and learns.

[FDLA](kernel/FDLA.md) corrects the movement when the acting system has replaced
or narrowed the source relation through its own interpretation.

[Evolution](kernel/EVOLUTION.md) returns material consequences and reusable
learning to the owner that should behave differently in later work.

`state/CURRENT.md` carries the current relation needed for continuation.
`state/SOURCES.md` points to owner-native sources and reusable knowledge.

The persistent conversational entry is
[adapters/conversational/INSTRUCTIONS.template.md](adapters/conversational/INSTRUCTIONS.template.md).
It points a receiving conversation into these owners without copying the whole
kernel into host settings.

For the broader System Semantic Kernel research corpus and theoretical
development, see the
[System Semantic Kernel working paper](https://github.com/GrazianoGuiducci/maios-ssk-paper).

## Set it up

The [chat setup guide](docs/CHAT_SETUP.md) starts from the source route the
receiving environment actually exposes:

```text
reachable persistent source already exists
-> use it in place

project / knowledge surface is the persistent source
-> place the constitutive owners there and preserve their mapping

attachments only
-> use the kernel in the current conversation; persistence is not established yet
```

Install the same conversational entry through the host's available instruction
mechanism, then begin real work. The kernel reaches deeper state and knowledge
only when the present relation makes them pertinent.

For the current ChatGPT repository implementation, [INSTALL.md](INSTALL.md)
and the [ChatGPT adapter](adapters/chatgpt/README.md) own the
Git/Python/configuration and host-receipt mechanics. Those mechanics are one
host incarnation of the portable conversational relation.

The [User guide](docs/USER_GUIDE.md) covers continuation, sources, competences,
the competence trace and evolution in ordinary use. The
[Adoption guide](docs/ADOPTION_GUIDE.md) defines the receiving relation and the
effects a complete adoption must make true.

## Source

[Architecture](docs/ARCHITECTURE.md) ·
[Current source state](CURRENT_STATE.md) ·
[Contributing](CONTRIBUTING.md) ·
[Changelog](CHANGELOG.md) ·
[Source version](VERSION) ·
[Apache License 2.0](LICENSE)

Copyright 2026 Graziano Guiducci.
