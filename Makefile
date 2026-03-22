SHELL := /bin/bash

install:
uv sync --no-dev

install-dev:
uv sync

run:
uv run python main.py

test:
uv run pytest --cov --cov-report=term --cov-report=term-missing

docker-build:
docker build -f docker/build.Dockerfile -t fastapi-template-build .

docker-test:
docker build -f docker/test.Dockerfile -t fastapi-template-test .
docker run --rm fastapi-template-test

docker-curl-test:
bash tests/docker/test_with_curl.sh
