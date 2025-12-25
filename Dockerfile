FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app 

RUN uv sync --frozen --no-cache

CMD ["/app/.venv/bin/fastapi", "run", "app/src/main.py", "--port", "8123"]