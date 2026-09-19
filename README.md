# kernel_chat

`kernel_chat` is a user-owned semantic operating kernel for conversational AI.

In practical terms, it lets an AI **carry forward the ways of working it
develops with you**: relevant sources, current context, reusable competences and
learning from real work remain available across later conversations.

The result is continuity that belongs to the user. You spend less time
reconstructing context and corrections, while useful ways of understanding and
working can become part of later work.

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

## Questions and answers

### What does “learning” mean here?

The changing object is the **user-owned operating layer**: competences, current
relations, source distinctions and reusable ways of working can change through
use.

Learning becomes observable when a later, different situation is understood or
handled differently because that changed operating knowledge participates.

### How is this different from a memory file, native memory, AGENTS.md, CLAUDE.md or custom instructions?

Those can all be useful carriers or entry surfaces.

`kernel_chat` adds a shared operating relation around them: selective reentry,
source ownership, competence participation and composition, learning returned
to the competence that should behave differently, and evolution when later
experience changes an earlier method.

A memory can preserve information. A competence also preserves **how to
understand or work when that knowledge becomes relevant**.

### Does it work beyond ChatGPT?

Yes. The portable conversational entry is provider-neutral:

```text
conversational AI environment
+ persistent/custom operating instructions or an equivalent entry
+ a persistent kernel source the conversation can reach
-> kernel_chat can operate in that environment
```

The receiving host supplies its own mechanism. The kernel source can be a
repository, project/knowledge space, filesystem, connector or another durable
source the conversation can reach.

ChatGPT currently has the first ready-made host-specific adapter. Other
compatible conversational environments can use the same kernel relation through
their own persistent instruction and source mechanisms.

### Do I need GitHub or Python?

The portable kernel relation can use the persistent source and instruction
mechanisms already available in the receiving environment.

GitHub and Python are used by the current ChatGPT reference helper. A receiver
that already has project knowledge, persistent files, a repository connection
or another durable knowledge surface can use that route instead.

### What does the host need?

For persistent use, the conversational environment needs:

```text
a persistent instruction / entry mechanism
+ a persistent source it can reach
```

Read access lets the conversation use existing kernel knowledge. Write access
lets it preserve new learning directly. When the host cannot write the source,
the assistant can produce the complete update for the user to save.

### How does it avoid loading an ever-growing history?

The current conversation remains the starting point. It reaches deeper state,
sources and competences only when they can materially change the work.

`CURRENT` keeps a small reentry margin. `SOURCES` points to the sources that
own useful knowledge. Reusable methods stay in their own competence owners
instead of accumulating in one transcript or prompt.

### What happens when a competence becomes wrong or stale?

Later results can change the knowledge that should act next time.

Reusable differences return to the closest owner, with enough source and reason
to understand why the method changed. A persistent form can be refined, revised
or retired when later work changes the relation it was carrying.

### What is the competence trace for?

Every final user-facing response closes with two compact functions:

```text
Competences: <owners that materially formed this response | —>
Emergent possibilities: <possibilities that materially emerged | —>
```

The trace makes recent competence participation visible. The next turn
recomputes what is relevant from the changed situation; the trace is an
observation of the completed work.

### How much context does this consume?

The design is selective rather than preload-oriented. The active conversation
uses its present context first and reaches additional knowledge only when it can
change the question, method or result.

This is also why the kernel source can grow in depth without requiring every
conversation to carry the whole source in its prompt.

### How do I know whether it is actually helping?

Look at **later non-identical work**.

A useful test is:

```text
experience or correction in task A
-> reusable change is preserved
-> task B later makes that competence relevant
-> task B is handled differently without rebuilding the same correction
```

Repository validation and regression tests verify package structure, source
routes and adapter mechanics. Behavioral evidence comes from observing whether
later work actually changes in the intended way.

### What does a normal user need to understand?

Only the operating result:

```text
work with the AI normally
-> useful reusable learning is preserved
-> later work can begin from it
```

The deeper kernel documents explain how source distinction, competence
formation, evolution and in-flow correction work for people who want to study
or extend the system.

### Who is this README for?

It is a shared entry surface for **people and AI assistants**.

A person can use the Q&A and the start path to understand what changes and what
to do next. In assisted adoption, an AI can use the same README to follow the
kernel owners, inspect the relevant source and carry out the parts of setup or
use that its environment actually supports.

### Why do some terms sound more abstract than the setup itself?

The public surface has two depths.

The first depth is operational: what changes for the user, what the host needs,
how learning is carried forward and how to start.

The second depth names the deeper relations that make the kernel portable and
evolvable. Those terms live in the kernel sources and in the
[System Semantic Kernel working paper](https://github.com/GrazianoGuiducci/maios-ssk-paper).

Normal use can begin from the operational depth. The deeper language is there
for people or systems that want to study, extend or reason about the
architecture itself.

### What is the fastest way to understand how it works?

Follow the smallest live path:

```text
README
-> AGENTS.md
-> Core / Competence only where the question makes them relevant
-> one real task
-> preserve one reusable difference
-> observe a later, different task
```

Reading the sources shows how the relations are formed. Using the kernel on
real work shows whether they actually change later behavior.

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

### 2. Install the conversational entry

Use the provider-neutral
[conversational instruction source](adapters/conversational/INSTRUCTIONS.template.md)
through the host's persistent/custom instruction mechanism or equivalent entry.

The [chat setup guide](docs/CHAT_SETUP.md) covers the supported source routes.

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

### Other conversational hosts

The portable entry lives under
[adapters/conversational/](adapters/conversational/README.md). A host-specific
adapter translates the same kernel relation into that host's real instruction,
persistence and source mechanisms.

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

For ordinary use, **Questions and answers** plus **Start using it** are enough
to begin. An AI assistant can continue through the linked owners when deeper
knowledge becomes relevant.

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
