"""
Sample tests for pytest

Examples
--------
Use pytest to search for files that start with test_*.py or *_test.py,
and within those files run `test` prefixed functions and methods
>>> poetry run pytest
"""

def increment(x):
    return x+1 

def test_increment_pass():
    """
    Since this function has the `test` prefix, pytest will
    find this and run it and check the result
    """
    assert increment(3) == 4

# def test_increment_fail():
#     """You shall not pass!"""
#     assert increment(3) == "4"