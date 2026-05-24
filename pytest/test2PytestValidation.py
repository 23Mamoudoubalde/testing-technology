# Fixtures allow reusable setup code for multiple test cases.
# preSetup is defined in conftest.py.
# conftest.py is shared globally across tests.

def test_initialcheck_third(preSetup):
    print("This is the third test run")