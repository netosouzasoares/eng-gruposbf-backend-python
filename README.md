## SBF - Converter

It's an API (Python) to do the convertion from REAL to USD,EUR and INR.

# Manifest

Converter API...

- convert from REAL to USD,EUR and INR
- can have many conversions

# Built With

- [Python](https://www.python.org/) 3.9
- [Flask](http://flask.pocoo.org/) 2.0.3
- [Flake8](http://flake8.pycqa.org/en/latest/) 4.0.1
- [dynaconf](https://github.com/rochacbruno/dynaconf) 3.1.7
- [flasgger](https://github.com/rochacbruno/flasgger) 0.9.5
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

Now you can see swagger at: http://127.0.0.1:5000/apidocs/

## Application Checklist

 - [] [Code Quality](link to the code quality tool sonar e etc..)
 - [] [New Relic/DataDog]()
 - [X] [CD](https://github.com/netosouzasoares/eng-gruposbf-backend-python/actions)
 - [X] [CI](https://github.com/netosouzasoares/eng-gruposbf-backend-python/actions)
 - [X] [Docker](https://hub.docker.com/repository/docker/neto123/converter)
 - [] [Sentry] ()

TODO: Implement.

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
6. Access route /apidocs to see app

## How Contribute

See the [opened issues](https://github.com/netosouzasoares/eng-gruposbf-backend-python/issues)