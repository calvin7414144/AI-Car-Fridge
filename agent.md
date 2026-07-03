# Agent Notes

## Project Overview

This project is an AI vehicle refrigerator management system.

- Backend: Django 6.0.6
- Admin UI: django-simpleui
- Frontend: Vue 3 + Vite
- Database: SQLite, stored at `db.sqlite3`

The Django backend serves the admin panel at `/admin/` and serves the built Vue frontend at `/`.

## Directory Structure

- `config/`: Django project settings, URLs, and shared views.
- `fridge/`: Django app for refrigerator-related features.
- `frontend/`: Vue 3 frontend source code.
- `static/frontend/`: Built Vue frontend files served by Django.
- `templates/admin/`: Simple UI admin template overrides.
- `.venv/`: Python virtual environment.
- `requirements.txt`: Python dependency lock list.

## Python Environment

Use the existing virtual environment:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

If dependencies need to be restored:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Django Commands

Run checks:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

Run migrations:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

Start the Django development server:

```powershell
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

Main URLs:

- Frontend: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Admin Account

Current superuser:

- Username: `calvinchen`
- Email: `ziyan13457@gmail.com`
- Display name: `CalvinChen`

Do not expose or change credentials unless the user asks.

## Admin UI Notes

The admin uses `django-simpleui`.

Important customizations:

- Admin language can switch between Chinese and English from the top-right toolbar.
- The left title changes by language:
  - Chinese: `AI车载冰箱管理`
  - English: `AI Car Fridge Admin`
- Quick Actions are translated on the admin page before Simple UI initializes.
- Language switching clears Simple UI session tab cache to avoid mixed-language labels.
- Template overrides live in `templates/admin/`.

Relevant files:

- `templates/admin/index.html`
- `templates/admin/login.html`
- `templates/admin/includes/js-part.html`
- `config/views.py`
- `config/settings.py`
- `config/urls.py`

## Vue Frontend

Vue source lives in `frontend/`.

The Django root view serves the built file:

```text
static/frontend/index.html
```

After changing Vue files, rebuild:

```powershell
$env:PATH='C:\Users\75077\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin;C:\Users\75077\.cache\codex-runtimes\codex-primary-runtime\dependencies\bin;' + $env:PATH
cd frontend
pnpm build
```

If system Node.js/npm is installed later, the bundled PATH step may not be necessary.

Useful frontend commands:

```powershell
pnpm dev
pnpm build
pnpm preview
```

Vite is configured to build into:

```text
../static/frontend
```

## Development Guidelines

- Keep Django admin customizations scoped to `templates/admin/` and config files.
- Keep Vue frontend code inside `frontend/src/`.
- Rebuild Vue before expecting Django `/` to show frontend changes.
- Do not edit generated files in `static/frontend/` directly; edit Vue source and rebuild.
- Keep `/admin/` working independently from the Vue frontend.
- Run `manage.py check` after Django changes.
- Run `pnpm build` after Vue changes.

## Current Verification Checklist

Before handing off changes, verify:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

Then check:

- `http://127.0.0.1:8000/` loads the Vue frontend.
- `http://127.0.0.1:8000/admin/` loads the Simple UI admin.
- Chinese and English admin language modes do not leave stale mixed-language custom menu labels.
