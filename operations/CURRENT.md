# Operational continuity

Read this surface only when unfinished causal work can change what should
happen next.

```text
active_flows: none
waiting_results: none
waiting_decisions: none
pending_effects: none
recovery_required: false
```

No background runtime, scheduler, worker, or external executor is implied.

When operational continuity matters:

```text
read this file
-> identify only the relevant flow, request, result, or receipt
-> recover the latest truthful cursor and effect state
-> resolve present capability and authority only for an exact live effect
-> continue, recover, or preserve the blocked relation
```

A configured fork may add small objects under this directory. Keep project
truth in its owner-native source and link to it rather than copying it here.
