import pytest


def test_timing(setup_functions):
    results = [func_setup["profiler_instance"].measure_timing() < 2
               for func_setup in setup_functions]
    assert all(results)


def test_correctness(setup_functions):
    results = [func_setup["profiler_instance"].call_function() ==
               func_setup["correct_result"] for func_setup in setup_functions]
    assert all(results)


def test_memory_usage(setup_functions):
    results = [func_setup["profiler_instance"].measure_memory_usage() < 20
               for func_setup in setup_functions]
    assert all(results)
