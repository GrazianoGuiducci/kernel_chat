# Portable Active Relations

Status: working candidate

This file holds only compact relations that have earned low-latency attention because losing them would materially change recurring recognition, routing or operation.

It is intentionally expected to remain small.

## Admission

A relation belongs here only after real use supports that keeping it active is materially better than recovering it cold from source/evidence.

```text
stored != active
used once != assimilated
important sounding != low-latency necessary
```

## Active relations

```text
none installed by default
```

Kernel/core relations belong in `kernel/`; active user/project learning belongs here only when later work demonstrates the need.

## Cooling

When an active relation no longer changes present work:

```text
remove from active attention
-> preserve source/evidence elsewhere when useful
-> reactivate only if a future field calls for it
```

Cooling is not deletion or falsification.
