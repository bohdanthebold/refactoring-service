# -*- Makefile -*-
.PHONY: help pip black
.DEFAULT_GOAL := help
# Define Variables
PY_SOURCES=*.py */*.py
export PYTHONPATH=$(shell pwd)/src/refactoring_service
help:
	@echo Shortcuts for useful commands
pip:
	pip install -r requirements.txt
black:
	python -m black -v src
lint:
	python -m pylint src
test:
	python -m pytest --cov=src
run:
	uvicorn main:app --reload
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache