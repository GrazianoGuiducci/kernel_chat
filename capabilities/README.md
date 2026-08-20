# Capability Field

This directory makes current capabilities inspectable without turning them
into the boundary of the kernel.

`manifest.json` records represented capability families, host-dependent
functions and the extension contract. The generated detailed map remains in
`.repokernel/meta/PROJECT_META_FACULTY.json`.

## Open-world rule

```text
not listed != impossible
listed != installed
installed != active
active != authorized
```

A material new relation may remain `retained_unknown`, compose existing
faculties, or become a reviewed extension. Add a stable manifest entry only
when discovery, exchange, execution, validation or reentry benefits from a
durable contract.
