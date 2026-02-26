# 🏗️ System Architecture

This project follows a **Modular Layered Architecture**. The goal is to separate concerns so that logic is easy to test, maintain, and scale.

## 🧱 The Layers

### 1. The API Layer (`api/`)
The entry point for all HTTP communication.
- **Responsibility**: Routing, HTTP status codes, and input validation via Pydantic.
- **Restriction**: Should NOT contain business logic or direct database queries.

### 2. The Service Layer (`services/`)
The "Brain" of the application.
- **Responsibility**: Business logic, data transformation, and orchestration.
- **Why?**: Keeping logic here allows you to reuse it (e.g., calling a service from a CLI script instead of an API endpoint).

### 3. The Data Layer (`models/` & `core/database.py`)
How the application persists data.
- **Responsibility**: Defining database tables and managing sessions via SQLAlchemy.

### 4. The Schema Layer (`schemas/`)
Data transfer objects (DTOs).
- **Responsibility**: Defining how data looks over the wire.
- **Why?**: Separation between Database Models and API Schemas prevents leaking sensitive data (like password hashes) directly from the database to the client.

## 🔄 Dependency Injection
We use FastAPI's `Depends` system to inject dependencies (like the Database Session or the Current User) into routes. This makes the code highly testable because you can easily swap a real database for a mock one during testing.

## 🛡️ Security Pattern
We use **OAuth2 with Password Flow and JWT Tokens**.
1. User provides credentials to `/api/auth/login`.
2. Server verifies credentials and returns a signed JWT.
3. User includes this JWT in the `Authorization: Bearer <token>` header for subsequent requests.
4. The `get_current_user` dependency verifies the token signature on every protected request.

## 🔄 Migrations (Alembic)
Instead of manually modifying the database, we use Alembic to track schema changes. Every change to a `model/` should be accompanied by an Alembic migration script.
