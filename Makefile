lint:
	flake8 .

cov:
	pytest --cov-fail-under 75 --cov converter

test:
	pytest

run-dev:
	FLASK_ENV=development FLASK_APP=app.py flask run

env:
	pipenv shell

install:
	pipenv install