FROM python:3.9-alpine

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip \
    && pip install pipenv gunicorn

RUN pipenv install --system
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "wsgi"]
