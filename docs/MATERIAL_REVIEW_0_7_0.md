# kernel_chat 0.7.0 — material release review

```text
review_type: source-side material release review
review_target: 10755f36a7764b8694e73a35e022efa69368e961
review_tree: baac361fb194c10cffafbd9163758dd9f125ec98
review_target_ci: 35519877372
review_target_validator: valid=true / errors=[] / warnings=[]
review_target_tests: 62
review_target_matrix: 8/8 Python 3.11-3.14 x Ubuntu/Windows
baseline_release: v0.6.0@d2c94ca4e4523f1f7a343601d6beec1e84031fac
result: no_material_blocker
selected_source_version: 0.7.0
```

## Scope

This review asks whether the current public source can coherently become the
next released product identity. It is not an external-review claim and does
not establish host behavior or longitudinal assimilation.

The review moved across product identity, portable carrier/adoption, semantic
owners, competence/evolution behavior, state/migration compatibility, security,
public-source hygiene, discovery/consumer proof and release/version boundaries.

## Resultant

The released `v0.6.0` and current source are no longer the same product
resultant. The current source adds or materially deepens:

- modality-neutral carrier identity and canonical `adapters/portable/` entry;
- receiver-relative adoption without requiring a host-specific adapter;
- experience-to-capability / competence learning and visible competence trace;
- mobile observation, closure convergence and stronger claim/proof relations;
- semantic continuity across reentry: information transfer is not assumed to
  preserve meaning, and unchanged source identity does not close pending work;
- public product narrative and user-guide convergence around the actual object;
- `SECURITY.md`, public/private reporting boundaries and pinned workflow actions;
- stronger discovery, rendered-consumer proof and historical-state hygiene.

The instance schema remains `kernel_chat.instance.v1`; the portable entry stays
`3.0.0`; legacy conversational and ChatGPT paths remain compatibility/adaptation
surfaces. No deliberate incompatible migration contract was introduced.

## Version decision

`0.7.0` is selected.

A patch release would understate the accumulated new capability surface.
`1.0.0` would assert a maturity/stable-contract boundary that this movement has
not established. A pre-1.0 minor version preserves lineage while making the
material product expansion explicit.

## Release boundary

The source promotion may update root `VERSION`, CURRENT_STATE, CHANGELOG,
release notes and release-specific invariants. That promotion must be proved on
its exact commit before tagging.

The `v0.7.0` tag/release, user-instance migration, configured adapter refresh,
installed host instructions and announcements are separate effects.

## Review result

No material source blocker remains for a `0.7.0` promotion candidate.

