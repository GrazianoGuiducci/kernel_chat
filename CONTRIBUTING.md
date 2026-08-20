# Contributing

Contributions should improve a real resulting behavior, preserve source and
remain reversible.

## Capability or kernel changes

Include:

```text
source_refs:
observed_behavior:
desired_behavior:
evidence:
invalidator:
reusable_delta:
private_or_host_residue_to_exclude:
effect_authority:
validation:
rollback_or_supersession:
```

Compare the candidate with the accepted baseline. Passing syntax alone is not
an improvement. `no_change`, `regression`, `tradeoff`, `unverified` and
`retained_unknown` are valid results.

Run:

```bash
python scripts/validate_kernel.py
```

Do not submit credentials, private project state, client data, provider
configuration, hidden reasoning or claims of third-party endorsement.
