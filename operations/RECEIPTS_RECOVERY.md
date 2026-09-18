# Receipts and recovery

Preserve a receipt when an operation or effect matters to later continuation,
proof, replay protection, or recovery.

```text
attempt and source pointers
target or destination
what actually happened
result or evidence pointers
effect caused, if any
validation
recovery or rollback relation
remaining pending relation
```

A receipt is evidence. It does not authorize repetition.

A file that carries recovery-critical identity must not be truncated in place
before the replacement is safely prepared. `kernel_chat` therefore publishes
owned text files through a temporary file plus atomic replacement at the
single-file boundary.

```text
prepare replacement separately
-> flush durable candidate bytes
-> atomic replace one owned file
-> previous file survives preparation/replacement failure
```

This does **not** make a multi-file command transactional. A command can still
complete one owned-file replacement and fail before another. On failure, inspect
the actual resulting paths and receipts before retrying; rerun only the effects
whose current owner state shows they remain incomplete. Do not infer rollback
or replay from the command name alone.

Before continuing effect-bearing work, distinguish whether the earlier effect
never happened, completed, failed with recoverable state, remains unknown, or
was superseded. Recovery may mean rollback, compensating action, retry,
recheck, retained failure, or explicit stop; it is not automatically replay.

The operational state owns continuity, not the original executor. If that
executor is unavailable, preserve the cursor and choose another route only
when present capability, source, ownership, and authority support it.
