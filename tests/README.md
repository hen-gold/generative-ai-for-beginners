# Test Suite

This directory contains automated tests for the Generative AI for Beginners course repository.

## Overview

The test suite validates the repository structure, dependencies, and code setup without requiring API keys. This enables "anonymous test conduction" - tests that can run in any environment without credentials.

## Test Files

- `test_basic.py` - Basic environment and structure validation tests
  - **TestEnvironmentSetup**: Validates Python version and dependency installations
  - **TestCodeStructure**: Validates essential files and repository structure

## Running Tests

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Classes

```bash
# Run only environment tests
pytest tests/test_basic.py::TestEnvironmentSetup -v

# Run only structure tests
pytest tests/test_basic.py::TestCodeStructure -v
```

### Run with Coverage

```bash
pytest tests/ --cov=. --cov-report=html
```

## Test Categories

Tests are organized by markers defined in `pytest.ini`:

- `unit` - Unit tests that don't require API keys
- `integration` - Integration tests that may require API keys
- `slow` - Tests that take a long time to run

Currently, all tests are unit tests that run quickly without API keys.

## CI/CD Integration

Tests run automatically on:
- Pull requests to the main branch
- Pushes to the main branch

See `.github/workflows/run-tests.yml` for the GitHub Actions configuration.

## Adding New Tests

When adding new tests:

1. Create test files with the prefix `test_`
2. Use descriptive test names starting with `test_`
3. Group related tests in classes with the prefix `Test`
4. Add appropriate markers for test categorization
5. Ensure tests can run without API keys when possible
6. Document any special setup requirements

Example:

```python
import pytest

class TestNewFeature:
    """Tests for new feature."""
    
    @pytest.mark.unit
    def test_feature_validation(self):
        """Test that feature works correctly."""
        assert True
```

## Best Practices

- Keep tests independent and isolated
- Use descriptive names that explain what is being tested
- Tests should be fast and reliable
- Avoid requiring external API calls or credentials when possible
- Use mocking for external dependencies
