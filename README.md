# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.

It gives a conversation a persistent operating source: kernel logic,
competences and metacompetences, current context, source relations and reusable
learning that can change how later work is understood and carried out.

```text
persistent/custom instructions or equivalent entry
+ a kernel source the conversation can reach
+ current context and owner-native sources
+ competences and metacompetences
-> the conversational AI enters kernel_chat
-> pertinent competences participate in the work
-> reusable learning returns to the owner that must act differently later
```

The same semantic operating relation can be incarnated through different
models, providers and persistence mechanisms. The receiving environment
supplies the means; the kernel supplies the operating relation.

## When this is the receiving relation

```text
conversational AI environment
+ persistent/custom operating instructions or an equivalent entry
+ a persistent kernel source the conversation can reach
-> kernel_chat can be incarnated in that environment
```

The environment may expose project knowledge, repository access, files,
connectors or another persistent source. Source references can be translated to
that environment while preserving the same owners and relations.

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

Each final response closes with a compact
[competence trace](kernel/KERNEL.md#kernel-chat-competence-trace): the
competence owners that materially formed the response and any possibilities
that materially emerged. The next turn recomputes pertinence from the new
field; the trace is continuity and observation, not a permanent stack.

Continuity is part of this relation but is not its whole identity. Decisions,
reasons, sources, unfinished relations and learned methods can remain reachable
across conversations without forcing every previous representation back into
the present.

## What is here

[AGENTS.md](AGENTS.md) is the portable entry and routing surface.

[Core](kernel/KERNEL.md) carries the operating relation: present context,
source distinction, situated movement, selective reentry, observation and
response-closing competence trace.

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
It points the receiving conversation into these owners without copying the
whole kernel into provider settings.

## Set it up

The [chat setup guide](docs/CHAT_SETUP.md) starts from the source route the
receiving environment actually exposes:

```text
reachable persistent source already exists
-> use it in place

project / knowledge surface is the persistent source
-> place the constitutive owners there and preserve their mapping

attachments only
-> usable for the current conversation, not persistent adoption yet
```

Then install the same conversational entry and begin real work.

For the current ChatGPT repository implementation, [INSTALL.md](INSTALL.md)
and the [ChatGPT adapter](adapters/chatgpt/README.md) own the
Git/Python/configuration and host-receipt mechanics. Those mechanics are one
host incarnation.

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
