# MenaIQ API

Backend service for **MenaIQ**, an enterprise governance and visibility layer over AI-assisted software development.

## Tech Stack

- **Python 3.11+**
- **FastAPI** for the REST API
- **Pydantic** for data validation and settings
- **SQLAlchemy 2.x** as the ORM
- **PostgreSQL 16** as the database
- **Alembic** for database migrations
- **Docker Compose** for running PostgreSQL locally

## Prerequisites

- Python 3.11 or newer
- Docker Desktop
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<org>/menaiq-api.git
cd menaiq-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Run database migrations

```bash
alembic upgrade head
```

### 7. Start the API

```bash
uvicorn app.main:app --reload
```

- Health check: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `APP_NAME` | Application name | `MenaIQ API` |
| `ENVIRONMENT` | Runtime environment | `development` |
| `DEBUG` | Enable debug mode and SQL logging | `true` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+psycopg://menaiq:menaiq@localhost:5432/menaiq` |

## Project Structure

```
menaiq-api/
├── alembic/              # Database migrations
│   └── versions/         # Migration scripts
├── app/
│   ├── api/
│   │   ├── routes/       # API endpoints
│   │   └── router.py     # Registers all routes
│   ├── core/
│   │   └── config.py     # App settings (loaded from .env)
│   ├── db/
│   │   ├── base.py       # SQLAlchemy declarative base
│   │   └── session.py    # Database engine and session
│   ├── models/           # SQLAlchemy ORM models
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # FastAPI application entry point
├── .env.example          # Example environment variables
├── alembic.ini           # Alembic configuration
├── docker-compose.yml    # Local PostgreSQL
└── requirements.txt      # Python dependencies
```

## Database Migrations

Create a new migration after adding or changing models:

```bash
alembic revision --autogenerate -m "describe your change"
```

Apply migrations:

```bash
alembic upgrade head
```

Roll back the last migration:

```bash
alembic downgrade -1
```

> New models must be imported in `app/models/__init__.py` so Alembic can detect them.

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Checks that the API and database are reachable |