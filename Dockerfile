# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies using uv
RUN uv sync --frozen

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# We use uv run to ensure the virtualenv is correctly used
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
