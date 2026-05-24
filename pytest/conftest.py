import pytest
@pytest.fixture(scope="function")
def preSetup():
    print("I am getting the browser ready")


