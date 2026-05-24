#Fixtures allows to reusable code for multiple test cases
import pytest

@pytest.fixture(scope="module")
def prework():
    print("I am Setting the MODULE")
    return "pass"



def test_initialcheck(prework):
    print("This is the first test")
    #print("-------------------------------------------------------------------------------------------")
    #assert prework =="fail"
    assert prework == "pass"


def test_initialcheck_fix(prework):
    print("This is the first test run with the fixture")

def test_initialcheck_fixSecond(prework):
    print("" \
    "This is the second test run with the fixture")