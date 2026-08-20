# Host Adapter Contract

A host adapter connects a conversation or agent runtime to the kernel without
becoming its identity, state owner or capability authority.

## Required fields

```text
adapter_id:
host_name:
adapter_version:
entry_surface:
kernel_locator:
state_locator:
available_capabilities:
unverified_capabilities:
blocked_capabilities:
authority_ceiling:
installation_method:
verification:
replacement_or_removal:
```

## Rules

- Keep the always-present adapter smaller than the kernel.
- Use the live conversation directly when it is sufficient.
- Reenter only when a missing relation can change the result.
- Attest capabilities per host and material effect.
- Do not turn an unavailable function into a universal impossibility.
- Do not infer installation from repository source or behavior from
  installation.
- Preserve complete replacement and removal instructions.
