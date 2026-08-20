# Portable Request / Result Handoff

Use this surface when the current conversational host cannot directly close a bounded operational need and another executor may contribute.

## Request candidate

```text
request_id
flow_id
capability_needed
intent_or_result_needed
input_refs
exact_effect_requested_if_any
authority_relation_if_already_selected
return_contract
supersession_or_expiry
```

## Result candidate

```text
request_id
executor_identity_or_attestation
observed_result_or_failure
evidence_or_artifact_refs
effects_actually_caused
receipt_or_recovery_refs
remaining_unknowns
```

## Boundary

A request delegates a bounded operation, not semantic ownership or unrestricted authority.

A returned result is evidence. The receiving host/project decides how it changes the continuing field according to current sources and owner relations.

Do not repeat a request merely because a historical transcript says it was sent; inspect current request/result/receipt state first.
