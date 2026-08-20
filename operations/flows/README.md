# Portable Flow Contract

A flow is durable only when losing its operational state would change continuation.

## Minimal relation

```text
flow_id
intent
status
source_owner_refs
faculty_owner_refs
trigger_relation
cursor_or_checkpoint
pending_relation
requested_or_possible_effect
review_or_effect_boundary
executor_route_optional
result_owner_or_destination
receipt_refs
recovery
stop_or_supersession
```

Use only fields that change the flow. A small flow should remain small.

Candidate statuses:

```text
active
waiting_input
waiting_result
waiting_decision
blocked
ready_for_review
completed
stopped
superseded
```

These labels are implementation aids, not a fixed ontology.

## Boundary

A flow records continuation, not project truth. Use source pointers instead of copying the project state.

A flow does not imply a running worker or scheduler.
