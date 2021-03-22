from collections import namedtuple

import pytest

from tests.profiler import Profiler
from tests.helpers import read_from_file
from data_structures.week1_basic_data_structures.\
    II_tree_height.tree_height import main


func_to_test = main

Setup = namedtuple("Setup", ["correct_result", "params"])
setups = [
    Setup(5, dict(parents=[3, -1, 3, 1, 1, 1, 5, 6, 7])),
    Setup(3, dict(parents=[3, -1, 3, 1, 3, 3, 3, 3])),
    Setup(10**5 + 1, dict(parents=[-1, *list(range(10**5))])),
    Setup(4, dict(parents=[-1, *list(range(3))]))
    ]


@pytest.fixture(autouse=True)
def setup_functions():
    def _prepare_setup(setup):
        return {
            "correct_result": setup[0],
            "profiler_instance": Profiler(
                func=func_to_test, **setup[1])
        }

    yield [_prepare_setup(setup) for setup in setups]
