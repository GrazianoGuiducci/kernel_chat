# MAIOS Conversation Kernel

An open-world, user-owned kernel for sustained work with conversational AI.

It gives a conversation a durable way to recover the present, follow exact
sources, compose or create faculties, evaluate what actually changed and
preserve useful evolution without making one model, prompt, tool catalog or
host interface the boundary of the system.

> Status: `0.1.0-alpha` — generated and locally validated source candidate.
> The first host adapter targets ChatGPT; host installation and behavioral
> activation remain separate evidence.

## Why it exists

Conversational systems can reason deeply while the current chat is hot, but
continuity is easily fragmented across chats, files, repositories and host
memory. Long instructions try to compensate by carrying the whole system in
every turn. That adds latency and still leaves source, ownership and effects
unclear.

MAIOS Conversation Kernel uses another relation:

```text
present conversation when sufficient
+ selective source-bound reentry when needed
+ user-owned state and receipts
+ an open field of faculties
+ replaceable host adapters
-> situated work that can continue and evolve
```

## What is inside

- A generated Project Meta-Faculty with `open_world: true`.
- A source-bound Problem/Possibility Seed.
- KA-derived orientation: source, difference, evidence, invalidation,
  reversibility and separate effect authority.
- Exportable current state, source atlas, decisions and receipts.
- A minimal ChatGPT Custom Instructions adapter.
- Host capability attestations that never turn unavailable into impossible.
- Positive and negative behavioral evals.
- A dependency-free validator and CI workflow.

The initial function families are inspectable in
[`PROJECT_META_FACULTY.json`](.repokernel/meta/PROJECT_META_FACULTY.json).
They are coverage, not a ceiling. A material relation outside them remains
source-bound as an explicit unknown or becomes a reviewed project-local
extension.

## Start with ChatGPT

1. Fork or clone this repository into an account and location you control.
2. Replace the repository placeholder in
   [`CUSTOM_INSTRUCTIONS.md`](adapters/chatgpt/CUSTOM_INSTRUCTIONS.md).
3. Paste only that short adapter into ChatGPT Personalization → Custom
   Instructions.
4. Confirm the installed version in
   [`INSTALLATION_STATE.md`](adapters/chatgpt/INSTALLATION_STATE.md).
5. Use normal work. Open the repository only when a missing relation can
   change the result.

The adapter is not the kernel. Replacing it does not rewrite repository state,
and changing repository source does not install the adapter in a host.

## Operating entry

```text
ordinary request
-> use the current conversation directly

continuity, source, owner or capability gap changes the result
-> read CURRENT_STATE.md
-> open only the closest source or faculty that becomes material

material effect
-> attest host capability
-> identify owner and authority
-> act, validate, receipt and preserve recovery
```

For repository-aware assistants, start with [`AGENTS.md`](AGENTS.md). For a
human-readable architecture map, read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Current evidence

```text
RepoKernel input bundle: valid
deterministic generation: verified locally
Project Meta-Faculty: generated, open-world
private-residue boundary: pending final public scan
public GitHub repository: not yet published
ChatGPT installation: not part of this repository proof
behavioral activation: not yet claimed
```

## Identity and attribution

MAIOS Conversation Kernel is an independent MAIOS/D-ND project. ChatGPT is an
OpenAI product and is named only to identify a compatible host adapter. This
project is not created, supported, certified or endorsed by OpenAI.

The kernel uses portable relations derived from KA — Kernel Assiomatico. It
does not include KA's private repository, collaboration history, node state or
authority. See [`docs/KA_LINEAGE.md`](docs/KA_LINEAGE.md).

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
