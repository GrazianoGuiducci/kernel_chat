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

Before continuing effect-bearing work, distinguish whether the earlier effect
never happened, completed, failed with recoverable state, remains unknown, or
was superseded. Recovery may mean rollback, compensating action, retry,
recheck, retained failure, or explicit stop; it is not automatically replay.

The operational state owns continuity, not the original executor. If that
executor is unavailable, preserve the cursor and choose another route only
when present capability, source, ownership, and authority support it.
