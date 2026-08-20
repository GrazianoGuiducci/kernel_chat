# Portable Operational Recovery

## Purpose

Recover unfinished causal work without replaying historical effects or depending on the original executor.

## Reentry relation

```text
recover operations/CURRENT_STATE.md
-> identify relevant flow/request/receipt
-> inspect latest observed result/effect
-> determine what remains live now
-> attest current host/executor capability only if operative
-> resolve current authority only for an exact live effect
-> continue or preserve blocked state
```

## Replay protection

Never infer from a historical plan, transcript or request that an effect should be repeated.

Before an effect-bearing continuation, determine whether the effect:

```text
never happened
happened and is complete
happened but needs a separately authorized follow-up
failed with recoverable state
is unknown and needs evidence before movement
was superseded or cancelled
```

## Executor replacement

The operational state owns continuity, not the executor.

If the prior executor is unavailable:

```text
preserve flow + cursor + pending relation
-> mark route unavailable/unknown
-> use an alternative only if current capability/source/effect relations support it
```

## Recovery is not rollback by default

Some operations cannot be reversed. Preserve the truthful recovery relation: rollback, compensating action, retry, recheck, retained failure or explicit stop.
