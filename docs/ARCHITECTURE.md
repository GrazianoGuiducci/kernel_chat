# Architecture

`kernel_chat` separates the portable relation from its current delivery and
persistence mechanisms.

```text
portable kernel
  present-first work
  source distinction
  situated competence and metacompetence
  FDLA self-observation
  revisable evolution

host adapter
  translates the kernel into a host-native entry
  states only capabilities the host can actually expose

user-owned state
  current point, source pointers, corrections, open work, next movement

operational continuity
  optional flows, requests/results, receipts, replay protection, recovery

persistence adapter
  makes state inspectable and reachable across conversations
```

Version `0.4.0` uses ChatGPT Custom Instructions as the host adapter and a
GitHub repository as the persistence adapter.

## Reentry

The default relation is direct work. Reentry begins only when a missing durable
relation can change the result.

```text
conversation
-> state/CURRENT.md
-> only the relevant source in state/SOURCES.md
-> current result
```

State remains a compact index. Owner-native project sources remain the truth
owners. The kernel repository does not become a copy of every connected
project.

## Unfinished work

When losing a cursor, pending relation, result, or effect receipt would change
continuation, the optional [`operations/`](../operations/) organ preserves the
smallest causal state needed to resume. It does not create a worker, scheduler,
daemon, or permission to repeat an historical effect.

## Competence field

The kernel does not ship a closed capability taxonomy. A configured fork may
point to competences, metacompetences, guides, or project-specific methods.
They become active when the present relation makes them useful and the current
host can actually reach them.

## Choice and self-observation

FDLA gives the core a way to notice when its own form is acting as an
unjustified limit. It preserves real invariants and present limits while
removing closures introduced by the interpretation. This function changes the
formation of the result; it is not a second workflow before the work.

## Effects

The following facts are orthogonal:

```text
useful action
host capability
source access
target ownership
current authorization
```

An adapter can help distinguish them. It cannot manufacture any of them.

## Extension

A new provider adapter should define:

- the host's real persistent-instruction surface;
- how the host reaches user-owned state;
- what it can read or write in the current interaction;
- how a user verifies reentry;
- which local mechanisms must not be simulated.

The core may evolve when another host exposes a relation that the current form
cannot represent without loss.
