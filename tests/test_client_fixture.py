from typing import Generator
import pytest
from gateway import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client