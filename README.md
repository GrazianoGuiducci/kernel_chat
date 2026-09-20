# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for AI.

> **Operating principle: Do not presume. Go deeper without narrowing the field.**
> Follow the owner/source relations when deeper understanding can change the
> work; a first representation, current host, adapter, example or apparent
> capability boundary is not the kernel's horizon.

In practical terms, it lets an AI **carry forward the ways of working it
develops with you**: relevant sources, current context, reusable competences and
learning from real work remain available across later conversations.

**Experience can become capability.** When real work teaches a better way to
understand, decide or do something, that reusable difference returns to the
competence that performs it. Later, materially different work can begin from
the improved competence rather than from a remembered outcome alone.

The result is user-owned continuity of context and capability. You spend less
time reconstructing context and corrections, while useful ways of understanding
and working can become part of later work.

It can inhabit an AI host surface — including a chat — when that host can
retain a persistent/custom operating entry and reach a durable kernel source.
GitHub, MCP, project knowledge, a filesystem, connectors or equivalent
receiver-native means can provide that source relation.

This extends a chat beyond dialogue and context recall: experience can become
competence, competences can change later work, and source, ownership, evolution
and effect boundaries can live in the semantic operating layer. The actual host
still supplies the tools and authority for material effects. In that sense a
chat can acquire system-level properties often implemented in agentic
architectures without requiring those conceptual and evolutionary structures to
be hard-coded into an external agent harness.

A dedicated host-specific adapter is optional.

## What you get

- **Continuity from the present** — later conversations can recover the current
  point, relevant sources and still-useful reasons without replaying the whole
  history.
- **Reusable competences** — a useful way of understanding, deciding or doing
  something can participate again when a later task makes it relevant.
- **Learning from real work** — corrections, successful methods, changed
  directions and other reusable differences can change how later work is
  handled.
- **User-owned sources** — the operating knowledge lives in a persistent source
  you control and can inspect.
- **Selective reentry** — the conversation reaches the sources and competences
  that can change the current result instead of loading everything.
- **Visible participation** — a compact competence trace shows which competence
  owners materially contributed to each final response.

## A small before / after

```text
task A

user:
The source says X. Y is our inference, not a fact from the source.

kernel_chat:
the distinction changes the source-discrimination competence
-> the reusable difference is preserved in the user-owned kernel source


task B, later and materially different

a new source mixes reported facts with possible explanations
-> the source-discrimination competence becomes relevant
-> the AI keeps source facts and its own inference separate
-> the user does not have to reconstruct the earlier correction
```

The important result is the **changed handling of task B**.

The same relation can operate at a deeper level. If real work shows that the
system is forming the wrong question or selecting the wrong things as relevant,
the reusable change can belong to the competence that forms the question
itself. Later work can then begin from a different operating relation.

The persistent files, state objects or knowledge surfaces carry this operating
layer between conversations and environments.

## Capabilities and where to verify them

The README summarizes the operating result. The linked owners carry the exact
relations behind each capability.

| Capability | What it does | Inspect |
| --- | --- | --- |
| **Present-first continuity** | Recovers only the durable relation that can change the work now. | [Core](kernel/KERNEL.md) · [User guide](docs/USER_GUIDE.md) |
| **Selective source reentry** | Reaches owner-native sources when they become relevant instead of replaying a whole history. | [Core](kernel/KERNEL.md) · [SOURCES template](templates/state/SOURCES.md) |
| **Situated competences** | Lets reusable ways of understanding and working participate, combine, deepen or form when needed. | [Competence](kernel/COMPETENCE.md) |
| **Learning return** | Turns a reusable difference from real work into a change in the competence or owner that should understand or perform later work differently. | [Evolution](kernel/EVOLUTION.md) · [Competence](kernel/COMPETENCE.md) |
| **Revision through later use** | Refines, revises or retires persistent forms when later consequences change the relation they carry. | [Evolution](kernel/EVOLUTION.md) |
| **Source / inference distinction** | Keeps source, evidence, inference, representation and effect authority distinguishable when the difference matters. | [Core](kernel/KERNEL.md) |
| **In-flow correction** | Lets the system revise an interpretation that has narrowed the field it is trying to understand. | [FDLA](kernel/FDLA.md) |
| **Competence trace** | Exposes which competence owners materially participated in a final response. | [Core trace](kernel/KERNEL.md#kernel-chat-competence-trace) |
| **Provider-neutral portable entry** | Carries the same kernel relation into compatible receiving environments. | [Portable entry](adapters/portable/README.md) · [Instruction source](adapters/portable/INSTRUCTIONS.template.md) |
| **Receiver-relative adoption** | Uses the persistent source and instruction mechanisms actually available in the host. | [Chat setup](docs/CHAT_SETUP.md) · [Adoption guide](docs/ADOPTION_GUIDE.md) |
| **ChatGPT reference integration** | Provides the current ready-made Git/Python configuration and receipt mechanics. | [ChatGPT adapter](adapters/chatgpt/README.md) · [Install](INSTALL.md) |
| **Current package evidence** | Records current source state, release identity and repository proof boundaries. | [Current state](CURRENT_STATE.md) · [Tests](tests/) |

## Useful clarifications

**Learning** means experience changing a reusable competence or source relation
so later relevant work can be understood or performed differently. The
persistent representation carries that change between encounters; it is not by
itself the exercised competence. Later, different work is where the changed
capability becomes observable. See [Competence](kernel/COMPETENCE.md) and
[Evolution](kernel/EVOLUTION.md).

**The kernel is portable across compatible AI environments.** The canonical
entry is under [adapters/interaction/](adapters/interaction/README.md).
A host-specific adapter is a ready-made integration layer, not a requirement
for adoption. If a receiving environment already provides a persistent
instruction entry and a persistent source it can reach, the portable entry can
be installed directly there. ChatGPT currently has the first ready-made
host-specific helper.

**GitHub and Python belong to the current ChatGPT reference helper**, not to the
portable semantic relation. The [setup guide](docs/SETUP.md) starts
from the source route the receiving environment actually exposes.

**The deeper terminology is optional for normal use.** Core, Competence,
Evolution, FDLA and the
[System Semantic Kernel working paper](https://github.com/GrazianoGuiducci/maios-ssk-paper)
are available for technical or conceptual study. They are not prerequisites for
starting to use the kernel.

## Check it directly

The shortest useful verification path is:

```text
1. read the capability you care about
2. follow its owner/source link above
3. use the kernel on one real task
4. preserve one reusable difference
5. observe a later, different task
```

The repository shows how the relation is formed. The later task shows whether
that relation actually changed the work.

## Start using it

### 1. Choose the persistent source already natural to your environment

Possible routes include:

```text
existing project / knowledge space
-> use it as the persistent kernel source

reachable repository or filesystem
-> use that source in place

session-only attachments
-> use the kernel in the current conversation
-> add a persistent source when you want cross-conversation continuity
```

### 2. Install the portable entry

Use the provider-neutral
[portable instruction source](adapters/portable/INSTRUCTIONS.template.md)
through the host's persistent/custom instruction mechanism or equivalent entry.

The [setup guide](docs/SETUP.md) covers the supported source routes.

### 3. Start with real work

Bring the real topic, project, question or activity.

When useful learning emerges, let it return to the source or competence that
should participate differently later.

See the [User guide](docs/USER_GUIDE.md) for ordinary use, continuation and
competence evolution.

## Ready-made integrations

### ChatGPT

The current [ChatGPT adapter](adapters/chatgpt/README.md) provides the
host-specific Git/Python/configuration and installation-receipt mechanics for a
repository-backed setup.

[INSTALL.md](INSTALL.md) owns the complete reference procedure.

### Other receiving environments

The portable entry lives under
[adapters/portable/](adapters/portable/README.md).

A dedicated host adapter is optional. When the host already exposes persistent
instructions and a persistent project/knowledge/repository source, install the
portable entry through those native mechanisms. A host-specific adapter is
useful when setup, translation, receipts or other host mechanics benefit from a
ready-made implementation.

When an AI operates instead inside a durable project workspace/filesystem that
it owns as its continuing work surface, use the project-native
[MAIOS Project Kernel](https://github.com/GrazianoGuiducci/maios-project-kernel).

## Go deeper

Normal use can begin from the operating result above. The internal kernel
documents are the study and extension surface:

- [AGENTS.md](AGENTS.md) — portable entry and routing;
- [Core](kernel/KERNEL.md) — present context, source distinction, situated
  movement, selective reentry, observation and competence trace;
- [Competence](kernel/COMPETENCE.md) — how reusable capabilities participate,
  combine, deepen, form and evolve;
- [Evolution](kernel/EVOLUTION.md) — how consequences from real use can change
  later work while remaining attributable and revisable;
- [FDLA](kernel/FDLA.md) — in-flow correction when the acting interpretation
  narrows the field it is trying to understand;
- [Architecture](docs/ARCHITECTURE.md) — package, instance, entry, adapter and
  host relations;
- [Adoption guide](docs/ADOPTION_GUIDE.md) — what complete adoption makes
  reachable.

For the broader research corpus and theoretical development, see the
[System Semantic Kernel working paper](https://github.com/GrazianoGuiducci/maios-ssk-paper).

## Reading path

This README is the shared entry surface.

For ordinary use, **What you get**, the capability/source map and **Start using
it** are enough to begin. An AI assistant can continue through the linked
owners when deeper knowledge becomes relevant.

For technical or conceptual study, continue through **Go deeper** and the
System Semantic Kernel working paper. That depth explains the architecture and
research language; it is not the entry cost for using the kernel.

## Source

[Current source state](CURRENT_STATE.md) ·
[Contributing](CONTRIBUTING.md) ·
[Changelog](CHANGELOG.md) ·
[Source version](VERSION) ·
[Apache License 2.0](LICENSE)

Copyright 2026 Graziano Guiducci.
