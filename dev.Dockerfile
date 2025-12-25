FROM python:3.12-slim-trixie

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app
RUN uv sync --locked

CMD ["app/.venv/bin/fastapi", "run", "app/src/main.py", "--port", "8123"]