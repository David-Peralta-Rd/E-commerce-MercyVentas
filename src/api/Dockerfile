# ==================================== #
# ==== Initial construction phase ==== #
# ==================================== #
FROM python:3.14-slim-bookworm AS builder

# Variables for optimizing the UV environment
ENV UV_COMPILE_BYTECODE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app

# 1. Copy the uv binary from the official Astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 2. Copy dependency files to leverage the Docker layer cache.
COPY pyproject.toml uv.lock ./

# 3. Copy your package's source code
COPY . ./

# 4. Build the project. This will generate the .whl file in the /app/dist/ folder.
RUN uv build --wheel




# ============================== #
# ==== Second runtime stage ==== #
# ============================== #
FROM python:3.14-slim-bookworm AS runtime


WORKDIR /app

# 1. We're also bringing `uv` to the runtime for ultra-fast installation.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# 2. We copy the precompiled installation package from the previous stage.
COPY --from=builder /app/dist/*.whl /tmp/

# 3. Copying startup commands
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

# 4. Install and remove the precompiled version
RUN uv pip install --system --no-cache-dir /tmp/*.whl && rm /tmp/*.whl

# 5. Running entrypoint commands
ENTRYPOINT [ "bash", "./entrypoint.sh"]

# 6. Executing commands within the system
CMD [ "core", "runserver", "0.0.0.0:8000" ]
