# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.

It gives a conversation a user-owned operating layer made of sources,
competences, current context and reusable learning. That layer can change
through real work, so later work can begin from what the system has learned
instead of reconstructing the same understanding from scratch. A persistent
source keeps that changed layer reachable across conversations.

A **competence** is reusable operating knowledge: a way of understanding,
deciding or doing something that becomes relevant when the present work calls
for it. Several competences can participate in the same task, one can make
another relevant, an existing competence can deepen, and a genuinely missing
capability can form.

## What changes through use

The kernel keeps the present work, its sources and the competences acting on it
in one causal relation:

```text
current work
+ relevant sources
+ relevant competences
-> useful result
-> observe what changed
-> preserve the reusable difference where it should act again
-> later, different work can begin differently
```

Learning in `kernel_chat` happens at the **system level**: the user-owned
operating layer changes through use. The persistent representation carries that
change between conversations; the observable result is that a later situation
can be understood or handled differently.

For example:

```text
task A:
a user corrects the system for mixing a source fact with its own inference
-> the distinction changes the source-discrimination competence
-> that changed competence is preserved in the user-owned kernel source

task B, later and materially different:
the same distinction becomes relevant
-> the AI keeps source fact and its own inference separate
-> the user does not have to reconstruct the earlier correction
-> the changed handling of task B is the observable result
```

The same mechanism can operate at a deeper level. If real work exposes that
the system is forming the wrong question or selecting the wrong things as
relevant, the reusable change can belong to the competence that forms the
question itself. What matters is not merely that a file changed, but that later
work begins from a changed operating relation.

Files, state objects and instructions are persistent forms of this relation.
They make the kernel reachable again across conversations and environments;
they are the carrier through which the user-owned operating layer continues.

Each final user-facing response closes with a compact
[competence trace](kernel/KERNEL.md#kernel-chat-competence-trace): the
competence owners that materially formed the response and any possibilities
that materially emerged. The trace makes recent competence participation
visible to the next conversational turn without turning it into a fixed stack.

## Where it can operate

```text
conversational AI environment
+ persistent/custom operating instructions or an equivalent entry
+ a persistent kernel source the conversation can reach
-> kernel_chat can operate in that environment
```

The receiving environment supplies its own means. A persistent source may be a
repository, a project or knowledge surface, files, or another durable source
the conversation can reach. The kernel keeps the operating knowledge and its
sources connected; the host supplies the mechanism through which they become
reachable.

When the AI instead operates as an agent inside a durable project
workspace/filesystem that it owns as its continuing work surface, the
project-native carrier is
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel).

## Follow the operating sources

The README is the first public surface. The deeper owners are here:

- [AGENTS.md](AGENTS.md) — portable entry and routing;
- [Core](kernel/KERNEL.md) — present context, source distinction, situated
  movement, selective reentry, observation and competence trace;
- [Competence](kernel/COMPETENCE.md) — how reusable capabilities participate,
  combine, deepen, form and evolve;
- [Evolution](kernel/EVOLUTION.md) — how consequences from real use can change
  later work while remaining attributable and revisable;
- [FDLA](kernel/FDLA.md) — how the acting system can revise an interpretation
  that has narrowed the field it is trying to understand.

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
-> place the kernel sources there and preserve their relations

attachments only
-> use the kernel in the current conversation; persistence is not established yet
```

Install the conversational entry through the host's available instruction
mechanism, then begin real work. The kernel reaches deeper state and knowledge
only when the present work makes them relevant.

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
