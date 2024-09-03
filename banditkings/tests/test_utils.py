"""
Sample tests for pytest

Examples
--------
Use pytest to search for files that start with test_*.py or *_test.py,
and within those files run `test` prefixed functions and methods
>>> poetry run pytest
"""

from banditkings.utils import pathfinder

def test_find_project_root():
    path = pathfinder.find_project_root()
    assert type(path) == str

def test_data_pathfinder():
    paths = pathfinder.data_pathfinder()
    assert type(paths) == dict
    assert paths['raw'] is not None