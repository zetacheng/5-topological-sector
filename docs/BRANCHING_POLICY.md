# Branching Policy

## Branch names

```text
gate/<gate-name>
paper/<paper-version>
review/<review-topic>
fix/<issue>
archive/<retired-route>
```

## Rules

- `main` contains accepted infrastructure and accepted closed gates only.
- Active calculations stay on a `gate/` branch.
- Failed gate branches are preserved.
- Do not squash scientific derivation history.
- Prefer conventional commits.
- Tags mark accepted scientific milestones.
- One branch corresponds to one scientific gate or one paper-edit task.
