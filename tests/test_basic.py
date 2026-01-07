"""
Basic tests for the Generative AI for Beginners course examples.

These tests validate that core dependencies and imports work correctly
without requiring API keys, allowing for anonymous test conduction.
"""

import sys
import os
import pytest


# Helper constant for repository root directory
REPO_ROOT = os.path.dirname(os.path.dirname(__file__))


class TestEnvironmentSetup:
    """Test that the environment is set up correctly."""

    def test_python_version(self):
        """Verify Python version is 3.9 or higher."""
        assert sys.version_info >= (3, 9), "Python 3.9+ is required"

    def test_openai_import(self):
        """Test that openai package can be imported."""
        try:
            import openai
            assert openai is not None
        except ImportError:
            pytest.fail("openai package is not installed")

    def test_dotenv_import(self):
        """Test that python-dotenv package can be imported."""
        try:
            from dotenv import load_dotenv
            assert load_dotenv is not None
        except ImportError:
            pytest.fail("python-dotenv package is not installed")

    def test_numpy_import(self):
        """Test that numpy package can be imported."""
        try:
            import numpy
            assert numpy is not None
        except ImportError:
            pytest.fail("numpy package is not installed")

    def test_pandas_import(self):
        """Test that pandas package can be imported."""
        try:
            import pandas
            assert pandas is not None
        except ImportError:
            pytest.fail("pandas package is not installed")

    def test_tiktoken_import(self):
        """Test that tiktoken package can be imported."""
        try:
            import tiktoken
            assert tiktoken is not None
        except ImportError:
            pytest.fail("tiktoken package is not installed")


class TestCodeStructure:
    """Test that code examples have proper structure."""

    def test_env_copy_exists(self):
        """Verify that .env.copy template exists."""
        env_copy_path = os.path.join(REPO_ROOT, '.env.copy')
        assert os.path.exists(env_copy_path), ".env.copy template file is missing"

    def test_readme_exists(self):
        """Verify that main README.md exists."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        assert os.path.exists(readme_path), "README.md file is missing"

    def test_requirements_file(self):
        """Verify that requirements.txt exists and is not empty."""
        req_path = os.path.join(REPO_ROOT, 'requirements.txt')
        assert os.path.exists(req_path), "requirements.txt file is missing"
        
        with open(req_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert len(content) > 0, "requirements.txt is empty"
            assert 'openai' in content, "openai dependency is missing"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
