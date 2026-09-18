# User-owned state

The configurator can create three durable state surfaces in this directory:

```text
INSTANCE.json
  kernel instance / package / bridge identity
  + source-contact observation

CURRENT.md
  compact current relation or context

SOURCES.md
  owner-native sources that can change the result
```

## INSTANCE

`INSTANCE.json` owns configuration/update identity that should not be mixed with
user or project knowledge:

- user-owned instance repository;
- canonical upstream;
- package source version;
- host adapter;
- bridge-template version currently available from the package;
- configured-bridge template provenance, when known;
- configured bridge repository target, when known;
- configured bridge raw-byte digest;
- operator-reported host-installation state;
- raw-byte digest, repository target and template provenance of the bridge last
  confirmed by the operator as installed, when known;
- last observed upstream source-contact state.

Keep these bridge relations distinct:

```text
available_bridge_template_version
  template offered by the package currently present in the repository

configured_bridge_template_version
  template version known to have produced the preserved local configured bridge

configured_bridge_template_version = unknown
  configured bridge exists, but its template provenance cannot be established
  from available evidence

configured_bridge_repository
  repository target recorded for the configured incarnation when known

configured_bridge_sha256
  SHA-256 of the raw bytes of the configured incarnation recorded by INSTANCE

host_installation.installed_bridge_sha256
  raw-byte digest of the configured bridge the operator last confirmed as
  copied/saved in ChatGPT

host_installation.installed_bridge_repository
host_installation.installed_bridge_template_version
  semantic target/provenance snapshot of that operator-confirmed incarnation
  when known
```

`unknown` template provenance is not structural invalidity and does not mean the
bridge is unusable. It is a reconciliation signal. Preserve the configured
bridge until its fit or origin is actually understood; do not relabel it as the
current template merely because the package has changed.

A standard configured bridge also names the user-owned repository it reaches.
When that observable target differs from `INSTANCE.instance_repository`, the
instance and bridge are not describing the same continuity relation. The
configurator prevents this mismatch during ordinary legacy migration; the
validator can expose it if manual/customized state later creates it.

A bridge replacement performed by the current configurator can establish the
configured bridge byte identity, repository target and provenance because that
exact template produced the new local bridge. For an existing INSTANCE it does
not migrate `instance_repository`. A package/instance refresh can update what
bridge template is currently available without changing configured identity or
provenance; independently changed local bytes remain drift until a selected
replacement/reconciliation occurs.

When a configured bridge is delivered to the operator, its
`confirmation_bridge_sha256` is the correlation identity for that handoff.
After the operator actually copies/saves that delivered bridge in ChatGPT,
`--confirm-host-installation --expected-bridge-sha256 ...` can record the
operator report only if the delivered incarnation is still current. If local
bytes or the delivery identity no longer match, confirmation stops instead of
transferring evidence across incarnations. This does not inspect ChatGPT
directly.

If the local configured bridge later changes, preserve the previous installed
digest until the operator confirms the new host update. The difference is useful
readback rather than a reason to rewrite history.

The configured/installed repository/provenance fields added in 0.6 are
**optional additive fields of `kernel_chat.instance.v1`**. Older v1 receipts
remain valid when those fields are absent. Missing legacy fields can be
backfilled only from evidence that still matches the persisted artifact
identity; absence or unobservable target remains unknown rather than inferred.

`INSTANCE` does **not** prove that Custom Instructions were installed, that
GitHub is reachable from ChatGPT, or that the kernel changed host behavior.
Even `installed_operator_confirmed` means exactly that: the operator reported
the UI effect and the receipt records which configured digest that report
referred to.

## CURRENT

`CURRENT.md` is the compact reentry surface: where the current relation is, why
it matters, what is active, what remains open and what would change
continuation.

A project may be the current context, but a project is not required for the
instance to exist.

## SOURCES

`SOURCES.md` identifies owner-native sources, their ownership/evidence role and
when reading them can change the result. Availability is not automatic
activation or authority.

Keep state small. Point to owner-native sources instead of copying their
histories. Reusable methods belong in the competence/kernel owner that must use
them; state keeps the current implication and pointer when needed.

Do not store credentials, tokens, passwords, private keys, secret logs or
unapproved sensitive material here.

The canonical upstream package does not own a user's configured state. A
user-owned instance does. For non-public continuity, prefer a private standalone
repository initialized from the public package; a deliberately public fork is
valid when public state is intended.
