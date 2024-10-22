.PHONY: all

SHELL=/bin/bash -e

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

run:
	docker-compose build
	docker-compose up 