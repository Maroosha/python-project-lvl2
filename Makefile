install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff tests --cov-report xml

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
