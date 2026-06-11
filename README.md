# Simplified Logger
Simplified Logger is a small Python tool. it makes it easier to use the standard Python logging module. You can log to the console and to files with very little setup.

## Features
- **Easy API**: Simple methods for all log levels.
- **File & Console Logs**: Supports both terminal and file output.
- **Ready-to-use Format**: Includes timestamps and log levels by default.
- **Auto Folders**: Automatically creates folders for your logs.
- **No Duplicates**: Stops the logger from adding the same handler multiple times.
- **All Log Levels**: Supports INFO, DEBUG, WARNING, ERROR, and CRITICAL.

## Installation
You can install it using pip:

```bash
pip install simplified-logging
```

## How to use

### Standard Logging (No extra dependencies)
The `StandardLogger` uses the built-in Python `logging` module.

```python
from std_log import StandardLogger

# Set up the logger
logger = StandardLogger(name="app.log", dir="logs")
logger.console_handler()
logger.file_handler()

logger.info("The application has started")
```

### Structured Logging (JSON)
The `StructLogger` uses `structlog`. It outputs JSON, which is good for cloud services.

```python
from std_log import StructLogger

logger = StructLogger(name="app.json", dir="logs")
logger.info("user_login", user_id=123, ip="1.2.3.4")
```

### Serilog-Style Logging
The `SeriLogger` uses `serilog-python`. It works like the Serilog library in .NET.

```python
from std_log import SeriLogger

logger = SeriLogger(name="serilog")
logger.info("Task finished", duration_ms=450, status="success")
```

## API Reference

### Logger Class

#### `__init__(name: str, dir: str)`
Creates a new logger.
- **name**: The name of the log file.
- **dir**: The folder where logs are saved (it adds a '.' automatically).

#### `console_handler()`
Shows logs in the terminal.

#### `file_handler()`
Writes logs to a file. It creates the folder if it is missing.

#### `info(message: str)`, `debug(message: str)`, `warn(message: str)`, `error(message: str)`, `critical(message: str)`
Logs a message at the chosen level.

## Project Structure
```
simplified-logger/
├── .github/workflows/    # CI/CD scripts
├── docs/                 # Documentation
├── src/std_log/         # Source code
├── tests/                # Test suite
├── pyproject.toml        # Settings
└── README.md
```

## Development & CI/CD
We use GitHub Actions to automate our work:
1. **Test**: Runs every time you push code.
2. **Release**: Creates a GitHub Release when you push a version tag (like `v1.0`).
3. **Deploy**: Uploads the package to PyPI after a successful Release.

Read our [Testing Guide](./docs/testing.md) for more information.

## License
[MIT License](./LICENCE)

## Author
krigjo25 - krigjo25@outlook.com
