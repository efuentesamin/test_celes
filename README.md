# Celes Tech Test

A simple FastAPI microservice to serve aggregated endpoints in front of a datamart.


## Test & Run

In a virtual environment ([virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [Anaconda](https://www.anaconda.com/), etc) install dependencies:

```bash
pip install -r requirements.txt
```

The install [Apache Spark](https://spark.apache.org/downloads.html)

### Test

```bash
pytest
```

### Run

* Rename `.env-example` to `.env` and fill the `JWT_SECRET` with a strong secret and `SPARK_HOME` with the path to the spark installation.
* run
```bash
  python main.py
```
* Visit `http://localhost:8080/docs` to see documentation


## Architecture

This project uses Ports & Adapters architecture.

### Domain layer

In the `<feature>/domain` forlder lives the entities and business logic. This layer has no dependencies to the outside.

### Application layer

In the `<feature>/application` folder lives the application layer. In here lives the use cases, ports and dtos (pydantic schemas). This layer uses the domain layer to orchrestate te use cases logic.

### Infra layer

In the `<feature>/infra` folder lives the infrastructure layer. All the infra details lives here, adapters for repositories, data models, etc.

### Shared Kernel

In the `shared kernel` lives a thin layer of cross features dependencies like database and auth handlers.
