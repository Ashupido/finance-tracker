# Finance Tracker

A modern Django-based personal finance tracker with transactions, budgets, dashboard analytics, and AI-powered insights.

## Features

- **User Authentication** — Secure registration and login
- **Dashboard** — Real-time income, expenses, balance summary with spending pie chart
- **Transactions** — Create, edit, delete, and track all transactions
- **Budgets** — Set monthly budget goals and monitor spending vs. limits
- **Financial Insights** — Ask questions about your finances and get instant analysis
- **CSV Export** — Download transaction data for external analysis
- **Responsive Design** — Tailwind CSS styling optimized for mobile and desktop
- **Admin Panel** — Manage users, transactions, and budgets via Django admin

## Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (`.venv/` included)

### Installation

1. **Activate virtual environment:**
```powershell
& ".\.venv\Scripts\Activate.ps1"
```

2. **Install dependencies:**
```powershell
python -m pip install -r requirements.txt
```

3. **Run migrations:**
```powershell
python manage.py migrate
```

4. **Create admin account:**
```powershell
python manage.py createsuperuser
```
Follow prompts to enter username, email, and password.

5. **Start server:**
```powershell
python manage.py runserver
```

6. **Access the app:**
- Main app: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Dashboard
- View total income, expenses, and balance at a glance
- See spending breakdown by category in an interactive pie chart
- Quick access to recent transactions

### Manage Transactions
- Add income and expense transactions with category and date
- Edit or delete existing transactions
- View all transactions in a sortable table

### Budget Goals
- Create monthly budgets per category
- Track spending vs. budget limit
- Visual progress bars show budget status

### Financial Insights
- Click "💡 Financial Insights" in the navigation
- Ask questions like:
  - "What are my top spending categories?"
  - "Am I over budget?"
  - "Where should I save money?"
- Get instant analysis based on your actual financial data

### Export Data
- Click "Export CSV" to download all transactions
- Use for external analysis or backup

## Project Structure

```
finance_tracker/
├── accounts/              # User authentication (register, login, logout)
├── dashboard/             # Dashboard and analytics views
├── transactions/          # Transaction and budget models/views
├── insights/              # Financial insights analysis
├── templates/             # HTML templates (Tailwind CSS)
├── manage.py              # Django management commands
├── db.sqlite3             # Local SQLite database
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Troubleshooting

### Forgot Admin Password?
```powershell
python manage.py changepassword <username>
```

### Database Issues?
Reset the database:
```powershell
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use?
```powershell
python manage.py runserver 8001
```

## Deployment

This project is pre-configured for platforms like **Railway**:

- `Procfile` — Specifies gunicorn as the server
- `runtime.txt` — Pins Python version
- `whitenoise` — Handles static files in production
- `.env` — Environment variables (create on deployment platform)

### Deploy to Railway

1. Push code to GitHub
2. Connect repo to Railway
3. Set environment variables:
   - `SECRET_KEY` — Django secret key
   - `DEBUG=False` — Disable debug mode
   - `ALLOWED_HOSTS` — Your domain
4. Railway auto-deploys on push

## Technologies

- **Backend:** Django 5.2.1
- **Frontend:** Tailwind CSS, Chart.js
- **Database:** SQLite (local), PostgreSQL (production)
- **Server:** Gunicorn + WhiteNoise
- **Deployment:** Railway

## Notes

- Use the same virtual environment for all Django commands
- Keep `.env` file secure and never commit to version control
- Update dependencies regularly: `pip install --upgrade -r requirements.txt`
