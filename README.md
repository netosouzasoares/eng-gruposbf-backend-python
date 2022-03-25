## SBF - Converter

It's an API (Python) to do the convertion from REAL to USD,EUR and INR.

# Manifest

Converter API...

- convert from REAL to USD,EUR and INR
- can have many conversions

# Built With

- [Python](https://www.python.org/) 3.9
- [Pytest] (https://docs.pytest.org/en/7.1.x/#) 7.1.1
- [Pytest-Cov] (https://pytest-cov.readthedocs.io/en/latest/readme.html) 3.0.0
- [Requests](https://docs.python-requests.org/en/latest/) 2.27.1
- [newrelic](https://newrelic.com) 7.6.0.173
- [Mock](https://mock.readthedocs.io/en/latest/) 4.0.3
- [Toml](https://github.com/uiri/toml) 0.10.2
- [Gunicorn](https://gunicorn.org) 20.1.0
- [Sentry](https://github.com/getsentry/sentry-python) 1.5.8
- [Flask](http://flask.pocoo.org/) 2.0.3
- [Flake8](http://flake8.pycqa.org/en/latest/) 4.0.1
- [dynaconf](https://github.com/rochacbruno/dynaconf) 3.1.7
- [flask-swagger-ui](https://github.com/sveint/flask-swagger-ui) 3.36.0
- [awesomeapi](https://docs.awesomeapi.com.br)

# Run development

We are using pipenv as repository, if you don't have, see: https://pipenv.pypa.io/en/latest/

Install all dependencies (`make install`) and run the command:

After that you need active virtual env, run the command:

```
make shell
```

```
make run-dev
```

Now you can see swagger at: http://127.0.0.1:5000/swagger/

## Application Checklist

 - [X] [CD](https://github.com/netosouzasoares/eng-gruposbf-backend-python/actions)
 - [X] [CI](https://github.com/netosouzasoares/eng-gruposbf-backend-python/actions)
 - [X] [Docker](https://hub.docker.com/repository/docker/neto123/converter)
 - [X] [Sentry](https://sentry.io/organizations/neto-nq/projects/converter/?project=6275976)
 - [X] [NewRelic](https://one.newrelic.com/nr1-core/apm-nerdlets/overview/MzQ1NzI0NnxBUE18QVBQTElDQVRJT058MTEzMDAyNzg1MA?account=3457246)

 OBS: sentry and newrelic are private and i am using my account... if you want i can show to you

## Lint

Run command:

```
make lint
```

## Test

Run command:

```
make test
```

## Coverage

Run command:

```
make cov
```


## Build and Run Docker

Run command:

```
make docker-build
```

and then run with `docker run {IMAGE NAME}`

##  Model examples to requests

```
  {

    "price": 100,29,
  }
```

## Architecture:

awesomeapi: responsibility for values from EUR,USD and INR updated.

![alt_text](/docs/converter.png)

To edit use https://www.draw.io/ and open docs/architecture.xml

## How to Deploy:

1. Create a PR with your changes
2. Merge to master after approve and build
3. Create a release on github, after that github actions will push image to dockerhub (now image is public to tests, but to internal company we can create a private repository on dockerhub/ecr e etc...)


## How to deploy to kubernetes (using minikube to tests)

1. Execute steps on how to deploy
2. Replace TAG on files deployment on k8s folder
3. Start minikube: https://minikube.sigs.k8s.io/docs/start/
4. Execute the command on folder k8s `minikube kubectl -- apply  -f deployment.yaml`
5. Expose service with command: `minikube service converter`
6. Access route /swagger to see app

## How Contribute

See the [opened issues](https://github.com/netosouzasoares/eng-gruposbf-backend-python/issues)


If you create a new route or change please, update docs to swagger


## Performance Tests

We used the lib https://locust.io to a simple test running our app on minikube locally

You can see the simple results executed opening the file `report_24-03.html` on your broswer

## How to execute performance test

1. Run app locally or deploy on minikube as `How to deploy to kubernetes`
2. Create a virtualenv to running performance tests
3. Execute the command: `pip3 install locust`
4. Navigate to /scripts and then execute command: `locust`, the webpage will open, so you can configure your test