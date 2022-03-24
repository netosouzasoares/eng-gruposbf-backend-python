FROM python:3.9-alpine

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip \
    && pip install pipenv gunicorn

RUN pipenv install --system
COPY . .

ENV NEW_RELIC_CONFIG_FILE newrelic.ini

EXPOSE 5000

CMD ["newrelic-admin", "run-program", "gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "wsgi"]
