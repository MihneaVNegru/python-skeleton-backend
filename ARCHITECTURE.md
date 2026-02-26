# System Architecture

This project follows a Modular Layered Architecture. The goal is to separate concerns so that logic is easy to test, maintain, and scale.

## The Layers

### 1. The API Layer (api/)
The entry point for all HTTP communication.
- **Responsibility**: Routing, HTTP status codes, and input validation via Pydantic.
- **Restriction**: Should not contain business logic or direct database queries.

### 2. The Service Layer (services/)
The core logic of the application.
- **Responsibility**: Business logic, data transformation, and orchestration.
- **Rationale**: Isolating logic from the transport layer ensures reusability across different interfaces (e.g., CLI, background tasks).

### 3. The Data Layer (models/ & core/database.py)
Data persistence and management.
- **Responsibility**: Defining database entities and managing database sessions via SQLAlchemy.

### 4. The Schema Layer (schemas/)
Data Transfer Objects (DTOs).
- **Responsibility**: Defining data shapes for API requests and responses.
- **Rationale**: Strict separation between Database Models and API Schemas prevents accidental exposure of sensitive internal data.

## Dependency Injection
The project utilizes FastAPI's dependency injection system to manage shared resources such as database sessions and authentication context. This architecture facilitates modularity and enhances testability.

## Security Architecture
Authentication is implemented using OAuth2 with Password Flow and JWT tokens.
1. The client provides credentials to the authentication endpoint.
2. The server validates credentials and issues a signed JWT.
3. The client includes the JWT in the Authorization header for protected requests.
4. The security dependency validates the token signature and retrieves the user context.

## Migration Management
Database schema changes are managed through Alembic. This ensures that the database state is version-controlled and reproducible across different environments.
