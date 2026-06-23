# Agentic Guidelines

## Canonical source

- `openspec/specs/*` is the authoritative source for project scope, domain rules, and runtime documentation.
- `AGENTS.md` is a concise summary for agents and reviewers. It should point to OpenSpec and keep high-level instructions.

## Agent behavior

- Prefer small, targeted changes over broad refactors.
- Preserve critical workflow logic in `services.py` and reusable query/read logic in `selectors.py`.
- Use existing tools and commands (`uv`, `pytest`) rather than introducing new build or test infrastructure.
- When a decision is ambiguous, ask the user before implementing.

## Documentation updates

- When requirements change, update `openspec/specs/project.md` first, then sync `AGENTS.md`.
- When you detect a mismatch between code and documentation, update both the source of truth and the agent-facing summary.
- Add new OpenSpec files for new domains, workflows, or architectural constraints.

## Review focus

- Validate that public-facing behavior is documented, not just code comments.
- Keep cross-cutting rules and coupling notes close to the relevant source files.
- Ensure testing expectations are explicit and actionable.
