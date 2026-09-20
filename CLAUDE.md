# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

Spendly is a Flask expense tracker being built incrementally as a step-by-step exercise. Routes and functions
marked `# Step N` (see `app.py`, `database/db.py`) are intentional placeholders, not bugs — implement the
requested step when asked, don't jump ahead to future steps or refactor stubs away on your own.

## Development Commands

- Activate the venv before running anything: `source venv/bin/activate`
- Run the app: `python app.py` (starts on port 5001)
- Install dependencies: `pip install -r requirements.txt`
- Tests: `pytest` — pytest/pytest-flask are installed but no test files or config exist yet, so there's no
  existing suite convention to match.

## Architecture and Structure

- `app.py`: all routes and app configuration in one file. Unimplemented routes (`/logout`, `/profile`,
  `/expenses/*`) currently return plain placeholder strings.
- `database/db.py`: empty stub; will own `get_db()`, `init_db()`, `seed_db()` against a SQLite file at
  `expense_tracker.db` (gitignored, created at runtime — never committed).
- `templates/`: Jinja2 templates; every page extends `base.html` via `{% block title/head/content/scripts %}`.
- `static/`: plain `css/style.css` and `js/main.js` — no frontend framework or JS build step is used; keep
  additions vanilla.
