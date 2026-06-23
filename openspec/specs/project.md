# Project Specification

## Purpose

This Django project implements the "Great Hotels" single-night hotel booking platform.

## Scope

- `apps/bookings` — hotel rooms, availability, and reservation lifecycle.
- `apps/accounts` — users, authentication, and login sessions.
- `apps/search` — city filtering and 14-day calendar queries.

## Business rules

- All bookings must remain a strict one-night stay unless the user explicitly requests a multi-night feature.
- Availability validation and booking workflow logic belong in `services.py`.
- Reusable query and read logic belong in `selectors.py`.

## Commands

- Run server: `uv run python manage.py runserver`
- Run tests: `uv run pytest`
- Create migrations: `uv run python manage.py makemigrations`
- Apply migrations: `uv run python manage.py migrate`

## Risks and sensitive areas

- Room availability status transitions in `apps/bookings/services.py` during concurrent bookings.
- Session-based user persistence and autofill between Auth and Booking flows.
- Search parameter handling when zero hotels match.

## Change coupling

If a change touches:

- a Django model (`User`, `Hotel`, `Room`, `Booking`) → verify serializers, factories, and admin views.
- booking workflow or status states → verify context tasks and success notifications.
- search/filter behavior → verify both templates and backend view/query logic.

## Constraints

- Do not edit old migrations; create new migrations instead.
- Prefer small, targeted changes over broad architectural refactors.
- Use existing ecosystem tooling (`uv`, `pytest`) rather than adding unnecessary build tools.

## Documentation guidance

This file is the canonical source of truth for project scope and runtime behavior.
Keep `AGENTS.md` as a summary and pointer to OpenSpec; keep both documents in sync when requirements change.
