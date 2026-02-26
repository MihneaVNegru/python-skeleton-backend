# 🚀 Fast & Secure Python Backend Skeleton

A professional, production-ready backend skeleton built with **FastAPI**, **SQLAlchemy**, and **JWT Authentication**. This project follows a clean, modular architecture designed for scalability and ease of understanding.

---

## ✨ Key Features

- ⚡ **FastAPI**: Modern, high-performance web framework for building APIs.
- 🔐 **JWT Authentication**: Secure user signup, login, and protected routes using JSON Web Tokens.
- 🗃️ **SQLAlchemy**: Powerful ORM for database interactions.
- 📜 **Alembic**: Database migration management (like Git for your database).
- 🏗️ **Clean Architecture**: Layered structure (API, Services, Models, Schemas) for clean separation of concerns.
- 📦 **Modern Tooling**: Managed by **uv** for blazing-fast dependency management.
- 📄 **Auto-Docs**: Interactive Swagger UI and ReDoc documentation.

---

## 🛠️ Tech Stack

- **Laguage**: [Python 3.12+][python]
- **Web Framework**: [FastAPI][fastapi]
- **Database**: [SQLite][sqlite] (easily swappable to PostgreSQL/MySQL)
- **ORM**: [SQLAlchemy][sqlalchemy]
- **Migrations**: [Alembic][alembic]
- **Security**: [Passlib][passlib] (bcrypt), [Python-JOSE][jose] (JWT)
- **Package Manager**: [uv][uv]

---

## 📂 Project Structure

```text
├── alembic/            # Database migration scripts
├── api/                # API Routers & request handling
│   ├── auth.py         # Login & Signup endpoints
│   ├── items.py        # Example CRUD endpoints
│   └── deps.py         # Dependencies (Auth, DB)
├── core/               # Global configurations & security logic
├── models/             # Database tables (SQLAlchemy)
├── schemas/            # Data validation (Pydantic)
├── services/           # Business logic (The "brain")
├── main.py             # App entry point
└── pyproject.toml      # Project dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites
Install [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage the environment.

### 2. Setup
Clone the repository and install dependencies:
```bash
# Install dependencies
uv sync

# Create your environmental variables
cp .env.example .env  # If provided, or create manually
```

### 3. Database Migrations
Initialize the local database:
```bash
uv run alembic upgrade head
```

### 4. Run the Server
```bash
uv run uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## 📖 API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔐 Configuration

The project uses a `.env` file for configuration. Key variables:

- `DATABASE_URL`: Connection string for the database.
- `SECRET_KEY`: Used for JWT token signing.
- `ALGORITHM`: Encryption algorithm (default: HS256).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token lifespan.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

[python]: https://www.python.org/
[fastapi]: https://fastapi.tiangolo.com/
[sqlite]: https://www.sqlite.org/
[sqlalchemy]: https://www.sqlalchemy.org/
[alembic]: https://alembic.sqlalchemy.org/
[passlib]: https://passlib.readthedocs.io/
[jose]: https://python-jose.readthedocs.io/
[uv]: https://docs.astral.sh/uv/
