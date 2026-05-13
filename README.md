# Finance Tracker

A Django-based personal finance tracker with transactions, budgets, dashboard charts, and CSV export.

## Features

- User authentication with registration and login
- Dashboard summary with income, expenses, balance, and category pie chart
- Transaction list, create, edit, and delete
- Budget goals and progress tracking
- CSV export for transactions
- Tailwind CSS styling for a clean interface

## Setup

1. Activate the virtual environment:

```powershell
& ".\.venv\Scripts\Activate.ps1"
```

2. Install dependencies:

```powershell
python -m pip install -r .\requirements.txt
```

3. Run migrations:

```powershell
python .\manage.py migrate
```

4. Create a superuser (admin account):

```powershell
python .\manage.py createsuperuser
```

5. Start the development server:

```powershell
python .\manage.py runserver
```

6. Open in browser:

```text
http://127.0.0.1:8000/
```

## Deployment

This project is configured for platforms like Railway with:

- `Procfile`
- `runtime.txt`
- `whitenoise` for static files

## Notes

- If you forget the superuser password, reset it with:

```powershell
python .\manage.py changepassword <username>
```

- Use the same virtual environment to run all Django commands.
