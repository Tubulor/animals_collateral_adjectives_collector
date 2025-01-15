FROM python:3.12-slim

RUN pip install poetry==2.0.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY animals_collateral_adjectives_collector ./animals_collateral_adjectives_collector

RUN poetry install --without dev

ENTRYPOINT ["poetry", "run", "animals_collateral_adjectives_collector"]
