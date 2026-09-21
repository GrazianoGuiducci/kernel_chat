# kernel_chat 0.9.0 material review

```text
review_date: 2026-09-21
semantic_review_target: f66b9b13265a4bd7a3fb0d2d9c0b78eeaf986455
semantic_review_ci: 35593403680
review_target_matrix: 8/8 Python 3.11-3.14 x Ubuntu/Windows
tests_per_job: 65
validator: valid=true / errors=[]
baseline_release: v0.8.0@e5520de198454552d8d9cc4a2be1d310dd5fcbb9
selected_source_version: 0.9.0
portable_entry_candidate: 3.1.0
result: no_material_blocker
release_selected: false
```

## Scope

The candidate deepens a relation already present in Core, Competence and
Evolution: competence work is constitutive of the task rather than an optional
post-framing helper.

The portable entry now makes the compact generative seed reachable at first
contact:

```text
present relation
-> reuse / deepen / compose pertinent competences
-> form a new owner only when a durable capability is genuinely useful
-> concrete work / resultant
-> causal learning to the closest owner
-> competence formation can learn from its own selection and formation
-> later work reenters from the changed competence field
```

The same change distinguishes transient state from durable capability:
current facts, settings, plans and asset paths remain state/context; a durable
operator preference with reasons, recurring decision criterion, reusable
strategy/planning method or asset/tool handling method can become competence
knowledge when it should change later non-identical work.

## Non-effects

The candidate does not add:
- a central planner;
- a supervisor or admission layer;
- a fixed competence taxonomy;
- background execution;
- new effect authority;
- a new instance schema;
- a required host-specific adapter.

Existing v0.8.0 users remain compatible. A package/source update does not
automatically replace installed host instructions or user-owned state. Portable
entry 3.1.0 is an available newer entry contract, not evidence that any host has
installed it.

## Version decision

`0.9.0` is selected as the source version.

This is a backward-compatible expansion of a constitutive competence relation,
larger than a wording-only patch. The package is still pre-1.0, so a new minor
version preserves the current versioning policy without asserting a 1.0 maturity
boundary.

Portable entry `3.1.0` advances separately because its persistent instruction
contract now carries the generative seed.

## Review evidence

GitHub Actions run `35593403680` completed successfully on the exact semantic
target `f66b9b1`:

- Ubuntu Python 3.11, 3.12, 3.13, 3.14: success;
- Windows Python 3.11, 3.12, 3.13, 3.14: success;
- 65 tests per job;
- validator valid=true / errors=[].

The first implementation commit exposed two useful proof defects: a relative
portable-entry link resolved from the wrong directory, and test assertions
depended on Markdown line wrapping. Both were corrected before this review
target. That failed run remains historical evidence for the earlier candidate,
not a blocker on the corrected resultant.

## Release boundary

No tag or GitHub Release is selected by this review.

The immutable Latest release remains `v0.8.0`. This material-review/current
state commit is a source resultant and must receive its own CI readback before
the 0.9.0 source candidate is considered closed. A later release decision,
installed-host migration and user-instance update remain distinct effects.
