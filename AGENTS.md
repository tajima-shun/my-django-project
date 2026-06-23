# AGENTS.md

## Project scope

This is a Django web application for the "Great Hotels" single-night hotel booking platform.

Main apps / modules:
- `apps/bookings` — hotel rooms, availability, and reservation lifecycle
- `apps/accounts` — users, authentication, and login sessions
- `apps/search` — city filtering and 14-day calendar queries

## Important project conventions

- [cite_start]Put core business workflow logic and availability validation in `services.py`, not directly in views or serializers.
- [cite_start]Put reusable read/query logic (e.g., fetching available hotels by city and date) in `selectors.py`.
- Keep the system optimized for a strict 1-night stay calculation unless explicitly asked.

## Commands

- Run server: `uv run python manage.py runserver`
- [cite_start]Run tests: `uv run pytest` 
- Create migrations: `uv run python manage.py makemigrations`
- Apply migrations: `uv run python manage.py migrate`

## Things that are easy to break

- [cite_start]Room availability status transitions in `apps/bookings/services.py` during concurrent bookings.
- Session-based user information persistence and autofill checks between the Auth screen and the Booking screen.
- UI layout and error mapping when search parameters return zero matching hotel results.

## Change coupling

If you change:
- [cite_start]a Django Model (e.g., User, Hotel, Room, Booking) → also check serializers, factories, and admin views.
- [cite_start]booking workflow or status parameters → also check associated context tasks and success notifications.
- [cite_start]search/filter parameters → also check both the front-end templates and back-end view parameters.

## Constraints

- [cite_start]Do not edit old migrations; create a new one instead.
- Maintain a strict 1-night stay rule for all hotel room reservations.
- [cite_start]Prefer small, targeted changes over broad architectural refactors.

## Documentation use

- [cite_start]Use `openspec/specs/*` as the canonical source for technical/runtime documentation and database ERDs.
- [cite_start]Use `AGENTS.md` as a concise agent-facing summary and pointer to OpenSpec; do not treat it as the only source of truth.
- [cite_start]Keep technical/runtime truth in sync; report any detected inconsistency between code, OpenSpec docs, and AGENTS.md.

## Agent guidance

- [cite_start]Prefer small, targeted changes and explicit tests over broad refactors.
- [cite_start]When a behavioral or architecture decision is unclear, ask the user before implementing.
- [cite_start]Use `uv` commands and existing pytest patterns rather than creating new tooling.

## Testing expectations

Add or update pytest tests for:
- [cite_start]Hotel filtering accuracy based on Room Type and City combinations.
- [cite_start]Success notifications displaying exact confirmation details (Date, City, Hotel Name, Room Type).
- [cite_start]User authentication status validation and autofill persistence.