# -*- Makefile -*-
.PHONY: help pip black
.DEFAULT_GOAL := help
# Define Variables
PY_SOURCES=*.py */*.py
export PYTHONPATH=$(shell pwd)
help:
	@echo Shortcuts for useful commands
pip:
	pip install -r requirements.txt
black:
	python -m black -v $$(find * -name '*.py')
lint:
	python -m pylint main.py
test:
	python -m pytest --cov=main
run:
	uvicorn main:app --reload
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache