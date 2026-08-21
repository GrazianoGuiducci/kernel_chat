# Requests and results

Use a request when the current chat cannot close a bounded operational need
and another available executor may contribute.

```text
request:
  identity, flow, needed capability, intended result, input pointers,
  exact effect if any, return contract, expiry or supersession

result:
  request identity, executor attestation, observed result or failure,
  evidence pointers, effects actually caused, remaining unknowns
```

A request delegates a bounded operation, not semantic ownership or unrestricted
authority. A returned result is evidence; the continuing project decides how
it changes the present field.
