import logging
import tracemalloc
import functools
import time


class Profiler:
    def __init__(self, func, **kwargs):
        self.func = func
        self.kwargs = kwargs

    def __repr__(self):
        return f"Profiler({self.func.__name__}, args={self.kwargs})"

    def measure_timing(self):
        @functools.wraps(self.func)
        def timer():
            start = time.perf_counter()
            self.result = self.func(**self.kwargs)
            stop = time.perf_counter()
            runtime = stop - start
            logging.info(
                f"Function '{self.func.__name__}' returned in {runtime:.4f} sec"
            )
            return runtime
        return timer()

    def measure_memory_usage(self):
        tracemalloc.start()
        self.func(**self.kwargs)
        _, peak_memory_usage = tracemalloc.get_traced_memory()
        peak_memory_usage = peak_memory_usage / (1024 ** 2)
        tracemalloc.clear_traces()

        logging.info(
            f"{peak_memory_usage:.6f} MiB - peak memory usage "
            f"for '{self.func.__name__}'."
        )
        return peak_memory_usage

    def call_function(self):
        result = self.func(**self.kwargs)
        logging.info(
            f"{result} is the result of a function '"
            f"{self.func.__name__}' call.")

        return result