# Meta Semantic Kernel

**A user-owned semantic kernel for ChatGPT: a logical and structural harness
for persistent awareness, situated capabilities, operational continuity, and
reversible evolution.**

Meta Semantic Kernel organizes how a conversational AI relates its present
context, durable state, sources, capabilities, unfinished work, authority, and
learning. A GitHub repository you control makes that field persistent and
inspectable across chats. Continuity is one resulting function, not the whole
kernel.

Version `0.3.0` includes the ChatGPT adapter, an offline configurator, and a
structural validator. The adapter still has to be installed and exercised in
your own ChatGPT account; repository source alone does not verify host behavior.

[![Release](https://img.shields.io/github/v/release/GrazianoGuiducci/Meta_Semantic_Kernel)](https://github.com/GrazianoGuiducci/Meta_Semantic_Kernel/releases/latest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Adapter](https://img.shields.io/badge/adapter-ChatGPT-10a37f.svg)](adapters/chatgpt/)

[Install for ChatGPT](INSTALL.md) · [Read the user guide](docs/USER_GUIDE.md) · [Explore the architecture](docs/ARCHITECTURE.md)

## From isolated conversations to persistent awareness

A useful conversation can accumulate project decisions, open questions,
sources, and ways of working. Starting a new chat usually means explaining all
of that again—or pasting a transcript that contains far more history than the
next result needs.

Persistent awareness here means that a compatible host can recover where the
work is, why it matters, which sources govern it, which capabilities are
relevant, and what should happen next. It does not require the host to load all
stored history or administer the repository during every conversation.

Meta Semantic Kernel uses a fork of this repository as a user-owned continuity
surface. The fork keeps a concise current context and pointers to the sources
that own the real project information. The adapter instructs the host to read
them selectively when they can change the result. Records of unfinished work
stay separate until they are relevant again.

The intended routing is simple:

```text
ordinary question
-> work directly from the conversation

missing durable context
-> recover only the relevant state or source

unfinished work
-> resume from operational state and receipts

reusable improvement
-> preserve the smallest change that should survive the chat
```

The design keeps continuity available without making repository administration
part of every conversation.

## Quick start with ChatGPT

You need a GitHub account, Python 3, and a ChatGPT account where a GitHub
connection is available.

### Configure your fork locally

1. Fork this repository to your GitHub account.
2. Clone your fork and enter the repository:

   ```bash
   git clone https://github.com/YOUR_GITHUB_USER/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

3. Generate the adapter for your fork:

   ```bash
   python scripts/configure_chatgpt_adapter.py --github-user YOUR_GITHUB_USER --repository YOUR_REPOSITORY
   ```

The local result is
`adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md`, containing the exact
reentry path for your fork. The configurator does not call GitHub, change your
ChatGPT settings, or store credentials.

### Activate it in ChatGPT

1. Open the generated file and copy the complete text into ChatGPT Custom
   Instructions.
2. Use the GitHub connection available in the same ChatGPT account and give it
   read access to your fork.
3. Before relying on continuity, verify that a new chat can open
   `YOUR_GITHUB_USER/YOUR_REPOSITORY/state/CURRENT_PRESENT.md`.

Connection controls and repository access depend on the current ChatGPT
account and host capabilities; the local configurator cannot complete or prove
this phase. See the [complete installation guide](INSTALL.md) for configuration
boundaries, removal, and provider notes.

## What the kernel organizes

### Ordinary requests should remain direct

The adapter tells the host to use the current message and conversation when
they are sufficient. It does not require repository reentry or workflow
narration for every request.

### Relevant capabilities should participate when needed

The cognitive core defines a relational route from the present problem to an
existing competence, a useful composition, or a real capability gap. A fixed
catalogue is never treated as the ceiling of what the system can recognize or
develop.

### A new conversation receives a reentry path

When continuity can materially change the result, the ChatGPT adapter points
to [`state/CURRENT_PRESENT.md`](state/CURRENT_PRESENT.md). Your fork can connect
that concise state to the original sources of the projects you work on,
without copying their full histories into the kernel.

### The repository can preserve unfinished work

Flows, pending decisions, bounded requests, results, effect receipts, and
recovery live under [`operations/`](operations/). The adapter keeps this area
out of ordinary conversation unless unfinished work changes what should happen
next. A historical instruction never becomes automatic permission to repeat
an effect.

### Improvements have a durable destination

The evolution layer separates a stored observation from a reusable change. It
provides a place to revise state, routing, competence, adapters, or the core
when real use exposes a material difference, while project-specific truth stays
with its source.

## Toward autopoietic AI

The long-term direction is an autopoietic AI architecture: a system able to
preserve its operational identity, observe changes in its own functioning,
integrate useful capabilities, and revise its organization while keeping
provenance, causal coherence, reversibility, and authority over effects
legible.

The kernel is the logical and structural harness for that movement. It connects
reasoning with durable state, competence formation, unfinished operations,
learning, and reentry, so an AI can preserve and evolve the relations through
which it works—not only the content of previous conversations.

This foundation may contribute to future systems that can meaningfully be
described as artificial general intelligence. Version `0.3.0` does not claim
AGI or demonstrate autonomous self-evolution inside ChatGPT. It implements the
inspectable substrate from which persistent and progressively self-evolving
behavior can be developed and evaluated through real use.

## What is included

| Surface | Role |
| --- | --- |
| [`adapters/`](adapters/) | Host-specific activation and capability binding. Version 0.3.0 includes a ChatGPT Custom Instructions adapter. |
| [`kernel/`](kernel/) | Host-neutral cognitive core, relational routing, and competence participation. |
| [`state/`](state/) | Concise current context and the small set of relations that deserve active attention. |
| [`operations/`](operations/) | Optional continuity for unfinished work, requests, results, receipts, replay protection, and recovery. |
| [`evolution/`](evolution/) | Rules for deciding which useful changes should persist, where they belong, and how they remain reversible. |
| [`evals/`](evals/) | Behavioral discriminants that make failure conditions inspectable; they are not automatic proof of host behavior. |
| [`scripts/`](scripts/) | Dependency-free adapter configuration and structural validation. |

## Ownership, capability, and authority

Your fork owns its state. Connected projects keep ownership of their own
truth. A host adapter describes how a particular chat surface can reenter the
repository; it does not grant that host capabilities or authority it does not
actually have.

For a concrete external effect, the system keeps separate:

- what would be useful;
- what the current host can really do;
- which source and target are involved;
- who controls the target;
- whether the current interaction authorizes that exact effect.

Do not store access tokens, passwords, or secret keys in kernel state, Custom
Instructions, or repository files. Choose the visibility of your fork and its
connected-service permissions according to the state you intend to preserve.

## Current support

Version `0.3.0` packages the first integrated implementation. It includes a
configurable ChatGPT adapter and a structural validator. Repository source
alone does not prove that the adapter was installed, that GitHub was accessible
in a particular chat, or that later behavior incorporated a change.

The cognitive core is designed to accept replaceable host adapters. Version
`0.3.0` does not ship adapters for other providers, so cross-provider
compatibility is not claimed from similarity alone.

Run the structural validator from the repository root:

```bash
python scripts/validate.py
```

The validator checks package structure and claim boundaries. It does not
simulate ChatGPT or certify behavior in a connected account.

## Documentation

- [Install](INSTALL.md) — fork configuration and ChatGPT setup.
- [User guide](docs/USER_GUIDE.md) — normal use, project bindings, continuity,
  learning, recovery, privacy, and troubleshooting.
- [Architecture](docs/ARCHITECTURE.md) — how the package's organs cooperate
  without collapsing ownership or authority.
- [Update and portability](docs/UPDATE_AND_PORTABILITY.md) — update a fork or
  move user-owned state without replacing it with upstream defaults.
- [Current project state](CURRENT_STATE.md) — project reentry and maturity
  evidence.
- [Changelog](CHANGELOG.md) — the movement from exploration to the current
  integrated package.

## License

Copyright 2026 Graziano Guiducci. Licensed under the
[Apache License 2.0](LICENSE).
