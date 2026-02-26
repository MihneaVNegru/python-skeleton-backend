# Fast and Secure Python Backend Skeleton

A professional, production-ready backend skeleton built with FastAPI, SQLAlchemy, and JWT Authentication. This project follows a clean, modular architecture designed for scalability and long-term maintenance.

---

## Key Features

- **FastAPI**: Modern, high-performance web framework for building APIs.
- **JWT Authentication**: Secure user signup, login, and protected routes using JSON Web Tokens.
- **SQLAlchemy**: Powerful ORM for database interactions.
- **Alembic**: Database migration management.
- **Clean Architecture**: Layered structure (API, Services, Models, Schemas) for clean separation of concerns.
- **Modern Tooling**: Managed by uv for dependency management.
- **Automated Documentation**: Interactive Swagger UI and ReDoc documentation.
- **Testing Suite**: Comprehensive testing setup with pytest.
- **Containerization**: Ready for production with Docker and Docker Compose.

---

## Tech Stack

- **Language**: [Python 3.12+](https://www.python.org/)
- **Web Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [SQLite](https://www.sqlite.org/) (configurable for PostgreSQL/MySQL)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Security**: [Bcrypt](https://pypi.org/project/bcrypt/), [Python-JOSE](https://python-jose.readthedocs.io/)
- **Package Manager**: [uv](https://docs.astral.sh/uv/)

---

## Project Structure

```text
├── alembic/            # Database migration scripts
├── api/                # API Routers & request handling
│   ├── auth.py         # Login & Signup endpoints
│   ├── items.py        # Business resource endpoints
│   └── deps.py         # Dependencies (Auth, DB)
├── core/               # Global configurations & security logic
├── models/             # Database tables (SQLAlchemy)
├── schemas/            # Data validation (Pydantic)
├── services/           # Business logic
├── tests/              # Automated test suite
├── main.py             # Application entry point
└── pyproject.toml      # Project configuration and dependencies
```

---

## Installation and Setup

### 1. Prerequisites
Install [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage the development environment.

### 2. Initial Setup
Clone the repository and install dependencies:
```bash
# Install dependencies
uv sync

# Create environment configuration
cp .env.example .env
```

### 3. Database Initialization
Apply the latest migrations to the local database:
```bash
uv run alembic upgrade head
```

### 4. Running the Application
Start the development server:
```bash
uv run uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Testing

Run the automated test suite with pytest:
```bash
uv run pytest
```

---

## Docker Deployment

Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

---

## License
This project is open-source and available under the MIT License.
