lint:
	flake8 .

run-dev:
	FLASK_ENV=development FLASK_APP=app.py flask run

env:
	pipenv shell

install:
	pipenv install