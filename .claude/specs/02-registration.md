# Spec: Registration

## Overview
This feature implements the user registration process, allowing new users to create an account by providing their name, email, and password. This is a foundational step in the Spendly roadmap, enabling personalized expense tracking and secure access to user data.

## Depends on
- Step 01: Database Setup

## Routes
- `GET /register` — Display the registration form — public
- `POST /register` — Process registration and create user account — public

## Database changes
No database changes. (The `users` table already exists with required columns: `name`, `email`, `password_hash`).

## Templates
- **Modify:** `templates/register.html` — Update from a placeholder to a functional HTML form with fields for name, email, and password.

## Files to change
- `app.py` — Implement the `POST /register` route and update the `GET /register` route to handle form submission.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Navigating to `/register` displays a registration form.
- [ ] Submitting the form with valid details successfully creates a user in the `users` table.
- [ ] Entering an email that already exists in the database returns an appropriate error message.
- [ ] Passwords stored in the database are hashed, not plain text.
- [ ] After successful registration, the user is redirected to the login page or landed on a success page.
