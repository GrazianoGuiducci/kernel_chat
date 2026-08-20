# Architecture

## Stable separation

```text
MAIOS Conversation Kernel
├── capability core
│   ├── KERNEL.md
│   ├── Project Meta-Faculty
│   ├── Problem/Possibility Seed
│   └── source, state, evaluation and evolution contracts
├── host adapters
│   └── ChatGPT Custom Instructions adapter
├── user-owned state
│   ├── CURRENT_STATE.md
│   ├── .repokernel/state
│   ├── evidence and receipts
│   └── capability attestations
└── validation
    ├── static kernel validator
    ├── positive/negative eval cases
    └── CI projection
```

The capability core is not cloned into each host. An adapter connects the host
to the same user-owned sources and states its real capabilities for the current
effect.

## Open-world faculty field

The generated Project Meta-Faculty contains an initial coverage map. Its
extension rule is causal:

```text
material relation outside current families
-> retain it source-bound without distortion
-> compose existing faculties
-> if a material gap remains, create a falsifiable project-local candidate
-> evaluate changed behavior
-> accept, revise, reject, retire or retain unknown
```

No schema update is required merely because cognition notices a new relation.
Typing becomes necessary only when representation, execution, validation,
exchange or automation needs a stable contract.

## State and memory

Active attention and available memory are different. Normal work uses the
current conversation and only the decision-relevant source set. Durable state
is admitted when it changes later behavior, proof, recovery or reentry, or
preserves a non-reconstructible relation whose loss would reduce the
possibility field.

## Capability and effect reality

```text
possible != represented != generated != installed
installed != discovered != active != maintained
available != authorized
```

A host attestation names what can actually be read, written, invoked or sent
in the current environment. An exact effect then applies the owner gate,
validation, receipt and recovery for that surface only.

## Evolution

Compatible evolution may improve knowledge, evaluators or implementation while
preserving declared contracts. New data sources, tools, permissions, effects
or incompatible schemas require explicit review. A candidate never approves
or promotes itself.
