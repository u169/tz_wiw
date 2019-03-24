import os

import pytest

from src.Params import Params


real_path_absolute = os.path.dirname(os.path.abspath(__file__))


def test__good_test_in():
    path_in = '{}/files/params/good_test.in'.format(real_path_absolute)

    expected_paths = {
      "a": {
        "b": 10.1,
        "c": 15,
        "d": 35
      },
      "b": {
        "c": 3,
        "d": 7
      },
      "c": {
        "a": 2,
        "d": 4,
        "b": 1
      },
      "d": {
        "a": 25,
        "c": 9,
        "b": 1
      }
    }

    params = Params(path_in)

    assert params.points == ['a', 'd']
    assert params.paths == expected_paths


def test__good_test_in2():
    path_in = '{}/files/params/good_test.in2'.format(real_path_absolute)

    expected_paths = {
      "a": {
        "b": 1
      },
      "b": {
        "c": 1
      },
      "c": {
        "a": 1
      }
    }

    params = Params(path_in)

    assert params.points == ['a', 'b', 'c']
    assert params.paths == expected_paths


def test__bad_test_in():
    path_in = '{}/files/params/bad_test.in'.format(real_path_absolute)

    with pytest.raises(IOError):
        Params(path_in)
