# Project Architecture

## Overview
`simplified-logger` is a simple Python library. It wraps the standard `logging` module to make it easier to set up. It provides a clear way to start logging in your applications.

## Architecture Diagram
You can see how the components work together here:

![Architecture Diagram](./architecture.drawio)

*Note: Use [diagrams.net](https://app.diagrams.net/) to edit the `.drawio` file.*

## Main Components

The library has three logger classes in `src/std_log/std_log.py`:

### 1. `StandardLogger`
This wraps the standard Python `logging` module. It has no extra dependencies. It is best for simple scripts.

### 2. `StructLogger`
This wraps the `structlog` library. it is used for structured logging and outputs JSON. This is good for modern cloud tools like Datadog or ELK.

### 3. `SeriLogger`
This wraps `serilog-python`. It is inspired by the .NET Serilog library. It focuses on modern structured logging.

## How it works

### 1. Handler Management
Each logger manages its own handlers. The `StandardLogger` uses flags to make sure it doesn't add the same handler twice.

### 2. Automatic Folders
When you start a file logger, the library automatically creates the log folder for you. It uses `os.makedirs(exist_ok=True)`.

## CI/CD Pipeline
We use GitHub Actions to automate our workflow. The pipeline has three separate steps:

1. **`test.yml`**: This is the first step. it runs tests using Pytest on Python 3.10, 3.11, and 3.12. It starts when you push code or a tag.
2. **`release.yml`**: This starts after the tests pass. If you pushed a version tag (like `v1.0`), it builds the package and creates a GitHub Release.
3. **`deploy.yml`**: This starts after the release is created. It uploads the package to PyPI.

This system ensures that:
- Tests must pass before a Release.
- A Release must exist before we Deploy to PyPI.

## Testing Strategy
Tests are in the `tests/` folder. We use `pytest`. We test:
- How loggers are created.
- How handlers are managed.
- How folders are created.
- Basic logging for all three logger types.

Read the [Testing Guide](./testing.md) for more details.

