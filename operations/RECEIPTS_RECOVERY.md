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

For `state/INSTANCE.json`, atomic replacement also does not preserve a
concurrent read-modify-write by itself. Cooperative configurator writers use
`state/.INSTANCE.write.lock`: acquire it before reading INSTANCE, keep it
through the write, and fail visibly if another writer already owns it.

A stale lock is evidence of an interrupted/uncertain writer, not permission for
automatic deletion:

```text
lock present
-> inspect lock metadata + current INSTANCE + active writer reality
-> writer active: wait / hand off
-> no writer remains: remove stale lock explicitly
-> re-read current INSTANCE
-> continue from actual resultant
```

An external API/repository writer that cannot participate in the local lock must
coordinate at its own owner boundary and reconcile a fresh current state before
writing. Do not narrate local locking as universal serialization.

Before continuing effect-bearing work, distinguish whether the earlier effect
never happened, completed, failed with recoverable state, remains unknown, or
was superseded. Recovery may mean rollback, compensating action, retry,
recheck, retained failure, or explicit stop; it is not automatically replay.

The operational state owns continuity, not the original executor. If that
executor is unavailable, preserve the cursor and choose another route only
when present capability, source, ownership, and authority support it.
