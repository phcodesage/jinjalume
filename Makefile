.PHONY: install test lint css visual demo

install:
	python -m pip install -e ".[dev]"
	npm install

test:
	python -m pytest

lint:
	ruff check .

css:
	npm run build:css

visual:
	npm run test:visual

demo: css
	flask --app demo.app run --debug
