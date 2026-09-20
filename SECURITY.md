# Security policy

## Supported state

Security corrections target the current public source. When a finding also
affects the latest tagged distribution or a host-specific adapter, that
applicability is determined and recorded separately; current `main`, a tagged
release, a configured bridge, an installed host entry and a user-owned instance
are distinct identities.

## Reporting a vulnerability

Do **not** publish exploitable details, credentials, tokens, private keys,
personal data, private repository content, client material, private logs or
hidden runtime state in a public Issue, Pull Request, discussion or Evolution
Feedback.

Use the private contact channel available through [MAIOS](https://maios.it/) and
include only the minimum information needed to reproduce and understand the
problem.

If a public report is already open and contains sensitive material, stop
reproducing it in new comments or commits. Remove the material from the current
public surface where possible and treat any already-published Git history as a
separate remediation problem.

## Security boundaries

`kernel_chat` is a semantic operating kernel. Its source, competences and
persistent state do not grant external authority by themselves.

Keep these relations distinct:

```text
semantic instruction
!= connector/tool permission
!= repository write authority
!= filesystem/runtime authority
!= account-setting authority
!= actual external effect
```

A host-specific adapter may help configure or record an integration, but the
actual host, connector, repository and account retain their own permission and
security boundaries.

## Persistent source and privacy

A user-owned kernel source may contain context, methods or state that should
remain private. Do not move private material into a public repository merely to
make it reachable by a receiving AI environment.

Never store secrets in kernel state, competence bodies, receipts, configured
instruction artifacts or feedback. Use the credential mechanisms supplied by
the actual host or external service.

## Supply-chain and evidence

Repository CI, package validation, receipts and hashes prove only the relations
they explicitly bind. They do not prove that a connector is trustworthy, that a
host has the expected permissions, that an installed instruction is current, or
that a model has assimilated the kernel.

Workflow dependencies should use immutable identities when practical. A green
workflow run belongs to the exact source/tree it tested and is not automatically
evidence for a later commit.
