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
 - [] [CD]()
 - [] [CI]()
 - [] [Docker]()
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

```
make docker-run
```


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

TODO: explain how deploy on k8s