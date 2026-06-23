# Makefile for AI Platform Engine

.PHONY: install lint format typecheck test clean

install:
	pip install --upgrade pip
	pip install -e .

lint:
	ruff src tests

format:
	black src tests

typecheck:
	mypy src tests

test:
 pytest

clean:
	rm -rf build dist .eggs *.egg-info .coverage htmlcov .pytest_cache .mypy_cache .tox .venv
