FROM python:3.10.6-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYSETUP_PATH="/code" \
    VIRTUAL_ENV="/opt/.venv" \
    WEB_USER="uvicorn_user" \
    # poetry
    POETRY_VERSION=1.5.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR="/tmp/poetry_cache"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

FROM base AS builder

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update  \
    && apt-get install --no-install-recommends -y \
    build-essential=12.* \
    curl=7.* \
    libpq-dev=13.* \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && curl -sSL https://install.python-poetry.org | python - \
    && poetry --version \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y  \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $PYSETUP_PATH

COPY pyproject.toml poetry.lock ./
RUN python3 -m venv "$VIRTUAL_ENV" && poetry install --without dev && rm -rf "$POETRY_CACHE_DIR"

COPY . ./
RUN chmod +x "$PYSETUP_PATH/web.entrypoint.sh"


FROM builder AS development

WORKDIR $PYSETUP_PATH

RUN poetry install --with dev && rm -rf "$POETRY_CACHE_DIR"

CMD ["/bin/bash", "web.entrypoint.sh"]


FROM builder AS production

CMD ["/bin/bash", "web.entrypoint.sh"]