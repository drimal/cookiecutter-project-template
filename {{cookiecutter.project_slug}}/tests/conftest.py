"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return {
        "id": 1,
        "name": "test",
        "value": 42,
    }


@pytest.fixture
def temp_file(tmp_path):
    """Fixture providing a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    return file_path
