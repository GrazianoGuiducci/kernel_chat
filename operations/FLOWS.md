# Flows

A flow is durable only when losing its state would change continuation.

Its smallest useful form records:

```text
flow identity and intent
current status
source pointers
cursor or checkpoint
pending relation
possible exact effect, if one exists
result destination
receipt pointers
recovery, stop, or supersession
```

A flow records continuation, not a transcript and not project truth. It does
not imply a running worker, daemon, or scheduler.
