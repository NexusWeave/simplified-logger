# Testing Guide

This guide explains how we test the `simplified-logger` project.

## Testing Tool
We use [pytest](https://docs.pytest.org/) for our tests.

## Running Tests Locally

### Prerequisites
First, install the development tools:

```bash
pip install .[dev]
```

### Run All Tests
Run this command in the project folder to start all tests:

```bash
pytest
```

### More Information
If you want to see more details while the tests run, use:

```bash
pytest -v
```

## How we test

### 1. Unit Testing
We test each part of the code on its own:
- **Setup:** We check if loggers are created correctly.
- **Handlers:** We make sure handlers are added properly and not duplicated.
- **Folders:** We verify that log folders are created automatically.

### 2. Tools and Fixtures
- We use `pytest.fixture` to create and clean up temporary log folders.
- We use `caplog` and `capsys` to check what the logger outputs without creating real files every time.

## CI/CD (Automation)
GitHub Actions runs our tests automatically whenever you push code. This makes sure that:
- New changes do not break the project.
- The project works on Python 3.10, 3.11, and 3.12.
- We only release and deploy code that passes all tests.

## Coverage
To see how much of the code is tested, use `pytest-cov`:

```bash
pytest --cov=std_log tests/
```
