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

dev-install:
	pipenv install --dev

shell:
	pipenv shell

docker-build:
	docker build -t sbf/converter:v0.0.1 -f Dockerfile .

docker-run:
	docker run -p 5000:5000 sbf/converter:v0.0.1