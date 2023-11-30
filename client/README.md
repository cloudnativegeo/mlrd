# MLRD client
Python client which can read a MLRD training dataset catalog and provide an iterator which for each iteration loads a label chip and its source imagery and returns a numpy array for use in training

## Install Dependencies

With dev dependencies:
```shell
poetry install
```

Without dev dependencies:
```shell
poetry install --no-dev
```

## Update Dependencies

```shell
poetry update
```

## Add new Dependency

```shell
poetry add requests
```
Development-only dependency:
```shell
poetry add --dev pytest
```

## Build project

```shell
poetry build
```

## Lint project

```shell
poetry run flake8
```

## Run Tests

```shell
poetry run pytest tests
```