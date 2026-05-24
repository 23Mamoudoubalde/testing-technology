#Fixtures allows to reusable code for multiple test cases
# Smoke tests are basic tests to verify core functionality works properly.
# Skip marker is used when we want pytest to ignore a test temporarily.
import pytest

@pytest.fixture(scope="module")
def prework():
    print("I am Setting the MODULE")
    return "pass"

@pytest.fixture(scope="function")
def seconWork():
    print("I set up function instance")
    yield #pause after the it hit yield and then come back to finish function call
    print("tear down validation")

@pytest.mark.smoke
def test_initialcheck(prework):
    print("This is the first test")
    #print("-------------------------------------------------------------------------------------------")
    #assert prework =="fail"
    assert prework == "pass"

@pytest.mark.smoke
def test_initialcheck_fix(prework, seconWork):
    print("This is the initial Check")

@pytest.mark.skip(reason="Feature still under development")
def test_initialcheck_fixSecond(prework, seconWork):
    print("FixSecond test")
    
