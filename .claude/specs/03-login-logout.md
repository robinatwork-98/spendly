---
# Spec: Login and Logout

## Overview
This feature enables users to authenticate their identity and maintain a secure session. It allows registered users to access their personal expense data and ensures that only authorized users can view or modify their account information.

## Depends on
- 01 Database Setup
- 02 Registration

## Routes
- `GET /login` — Renders the login page — public
- `POST /login` — Validates credentials and starts a session — public
- `GET /logout` — Ends the user session and redirects to landing — logged-in

## Database changes
No database changes.

## Templates
- **Create:** `templates/login.html` (if not already fully implemented)
- **Modify:** `templates/base.html` to show Login/Logout links based on session state.

## Files to change
- `app.py` — Implement login and logout logic and session management.

## Files to create
- No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Use `flask.session` for session management.
- Use `werkzeug.security.check_password_hash` to verify passwords.

## Definition of done
- [ ] User can successfully log in with valid email and password.
- [ ] User is redirected to a protected page (e.g., profile or landing) upon successful login.
- [ ] User sees an error message when attempting to log in with invalid credentials.
- [ ] Logged-in users see a "Logout" link in the navigation.
- [ ] Guest users see a "Login" and "Register" link in the navigation.
- [ ] Clicking "Logout" destroys the session and redirects the user to the landing page.
---
