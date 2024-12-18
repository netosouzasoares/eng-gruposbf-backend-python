lint:
	pipenv run flake8 .

cov:
	pipenv run pytest --cov-fail-under 80 --cov converter --cov-report xml

test:
	pipenv run pytest

run-dev:
	FLASK_ENV=development FLASK_APP=app.py flask run

install:
	pipenv install

shell:
	pipenv shell

dev-install:
	pipenv install --dev

docker-build:
	docker build -t neto123/converter:latest -f Dockerfile .