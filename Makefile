lint:
	pipenv run flake8 .

cov:
	pipenv run pytest --cov-fail-under 68 --cov converter

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
	docker build -t sbf/converter:v0.0.1 -f Dockerfile .

docker-run:
	docker run -p 5000:5000 sbf/converter:v0.0.1