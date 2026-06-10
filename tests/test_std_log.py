import os
import shutil
import pytest
import logging
from std_log import StandardLogger, StructLogger, SeriLogger

@pytest.fixture
def log_dir():
    dir_path = "test_logs"
    # Ensure cleanup before and after
    full_path = "." + dir_path
    if os.path.exists(full_path):
        shutil.rmtree(full_path)
    yield dir_path
    if os.path.exists(full_path):
        shutil.rmtree(full_path)

class TestStandardLogger:
    def test_initialization(self):
        logger = StandardLogger(name="test_std", dir="test_logs")
        assert logger.name == "test_std"
        assert logger.dir == ".test_logs"
        assert isinstance(logger.log, logging.Logger)

    def test_console_handler(self):
        logger = StandardLogger(name="test_console")
        logger.console_handler()
        assert logger.is_console is True
        # Test duplicate prevention
        logger.console_handler() 
        assert logger.is_console is True

    def test_file_handler(self, log_dir):
        logger = StandardLogger(name="test_file", dir=log_dir)
        logger.file_handler()
        assert logger.is_file is True
        assert os.path.exists(f".{log_dir}")
        assert os.path.exists(os.path.join(f".{log_dir}", "test_file"))

    def test_logging_methods(self, caplog):
        logger = StandardLogger(name="test_methods")
        logger.console_handler()
        with caplog.at_level(logging.DEBUG):
            logger.info("info message")
            logger.debug("debug message")
            logger.warn("warn message")
            logger.error("error message")
            logger.critical("critical message")
        
        assert "info message" in caplog.text
        assert "debug message" in caplog.text
        assert "warn message" in caplog.text
        assert "error message" in caplog.text
        assert "critical message" in caplog.text

class TestStructLogger:
    def test_initialization(self):
        logger = StructLogger(name="test_struct", dir="test_logs")
        assert logger.name == "test_struct"
        assert logger.dir == ".test_logs"

    def test_console_handler(self):
        logger = StructLogger(name="test_struct_console")
        logger.console_handler()
        assert logger.is_console is True

    def test_file_handler(self, log_dir):
        logger = StructLogger(name="test_struct_file", dir=log_dir)
        logger.file_handler()
        assert logger.is_file is True
        assert os.path.exists(f".{log_dir}")

    def test_logging_methods(self):
        logger = StructLogger(name="test_struct_methods")
        logger.info("struct info", key="value")

class TestSeriLogger:
    def test_initialization(self):
        logger = SeriLogger(name="test_seri", dir="test_logs")
        assert logger.name == "test_seri"
        assert logger.dir == ".test_logs"

    def test_console_handler(self):
        logger = SeriLogger(name="test_seri_console")
        logger.console_handler()
        assert logger.is_console is True

    def test_file_handler(self, log_dir):
        logger = SeriLogger(name="test_seri_file", dir=log_dir)
        logger.file_handler()
        assert logger.is_file is True
        assert os.path.exists(f".{log_dir}")
        assert os.path.exists(os.path.join(f".{log_dir}", "test_seri_file"))

    def test_logging_methods(self, capsys):
        logger = SeriLogger(name="test_seri_methods")
        logger.info("seri info")
        captured = capsys.readouterr()
        assert "seri info" in captured.out
