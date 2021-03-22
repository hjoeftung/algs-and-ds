from importlib import import_module
from random import randint
from time import sleep, time


class Tests:
    def __init__(self, name, package, naive_func, tested_func,
                 test_data_type, max_int_1=20, max_int_2=20,
                 num_of_tests=1000):
        self.name = name
        self.tested_module = import_module(name=package + "." + name,
                                           package=__package__)
        self.naive_func = naive_func
        self.tested_func = tested_func
        self.max_int_1 = int(max_int_1)
        self.max_int_2 = int(max_int_2)
        self.num_of_tests = int(num_of_tests)
        self.test_data_type = test_data_type

    def generate_test_data(self):
        if self.test_data_type == "single_int":
            return [randint(0, self.max_int_1)
                    for _ in range(self.num_of_tests)]

        elif self.test_data_type == "pair_of_ints":
            test_data = []

            for i in range(self.num_of_tests):
                test_data.append([randint(1, self.max_int_1),
                                  randint(2, self.max_int_2)])

            return test_data

    def test_correctness(self):
        test_data = self.generate_test_data()

        print("\n" + "=" * 75 + f"\n\nCorrectness tests for "
                                f"{self.name.upper()}:\n")

        for index, data_unit in enumerate(test_data):
            if self.test_data_type == "single_int":
                num = data_unit
                correct_answer = getattr(self.tested_module,
                                         self.naive_func)(num)
                tested_answer = getattr(self.tested_module,
                                        self.tested_func)(num)
            else:    # self.test_data_type = "pair_of_ints"
                a, b = data_unit
                correct_answer = getattr(self.tested_module,
                                         self.naive_func)(a, b)
                tested_answer = getattr(self.tested_module,
                                        self.tested_func)(a, b)

            if correct_answer == tested_answer:
                print("\r", f"{index + 1} out of {self.num_of_tests} "
                      f"tests passed", sep="", end="", flush=True)
                sleep(0.0001)

                if index + 1 == self.num_of_tests:
                    print("\n")

            else:
                print(f"{index + 1} test failed: {data_unit}. "
                      f"Correct answer: {correct_answer}, "
                      f"Tested answer: {tested_answer}")

                return None

    def test_timing(self, function_name):
        print(f"Testing timing for {function_name}\n")

        test_data = self.generate_test_data()
        function = getattr(self.tested_module, self.tested_func)

        if self.test_data_type == "single_int":
            time_before_run = time()
            for num in test_data:
                function(num)

            time_after_run = time()
            total_runtime = time_after_run - time_before_run

        else:  # self.test_data_type == "pair_of_ints"
            time_before_run = time()
            for num_pair in test_data:
                a, b = num_pair
                function(a, b)

            time_after_run = time()
            total_runtime = time_after_run - time_before_run

        runtime_per_case = total_runtime / self.num_of_tests

        print(f"Results for function {function_name}:\n"
              f"    Total runtime: = {total_runtime}\n"
              f"    Runtime per test case: {runtime_per_case}\n")

        return {"total_runtime": total_runtime,
                "runtime_per_case": runtime_per_case}

    def benchmark_timing(self):
        funcs_to_benchmark = [self.tested_func, self.naive_func]
        test_data = self.generate_test_data()
        runtimes = {}

        print(f"Benchmarking tests for {self.name.upper()}:\n")

        for function_name in funcs_to_benchmark:
            testing_results = self.test_timing(function_name)
            runtimes[f"{function_name}"] = testing_results

        tested_func_total = runtimes[f"{self.tested_func}"]["total_runtime"]
        naive_func_total = runtimes[f"{self.naive_func}"]["total_runtime"]

        if tested_func_total <= naive_func_total:
            print(f"Tested function {funcs_to_benchmark[0]} is faster than "
                  f"naive function by "
                  f"{round(naive_func_total / tested_func_total, 2)} times\n")
        else:
            print(f"Naive function {funcs_to_benchmark[1]} is faster than "
                  f"tested function by "
                  f"{round(tested_func_total / naive_func_total, 2)} times\n")


if __name__ == "__main__":
    fib_tests = Tests(
        name="fibonacci",
        package="1_fibonacci_number",
        tested_func="fib_fast",
        naive_func="fib_naive",
        test_data_type="single_int",
        max_int_1=20,
        num_of_tests=1000
    )

    fib_last_digit_tests = Tests(
        name="fibonacci_last_digit",
        package="2_last_digit_of_fibonacci_number",
        tested_func="fib_last_digit_instant",
        naive_func="fib_last_digit_naive",
        test_data_type="single_int",
        max_int_1=1000,
        num_of_tests=1000
    )

    gcd_tests = Tests(
        name="gcd",
        package="3_greatest_common_divisor",
        tested_func="gcd_fast",
        naive_func="gcd_naive",
        test_data_type="pair_of_ints",
        max_int_1=1000,
        max_int_2=1000,
        num_of_tests=1000
    )

    lcm_tests = Tests(
        name="lcm",
        package="4_least_common_multiple",
        tested_func="lcm_fast",
        naive_func="lcm_naive",
        test_data_type="pair_of_ints",
        max_int_1=100,
        max_int_2=100,
        num_of_tests=1000
    )

    fib_mod_tests = Tests(
        name="fibonacci_huge",
        package="5_fibonacci_number_again",
        tested_func="fib_mod_fast",
        naive_func="fib_mod_naive",
        test_data_type="pair_of_ints",
        max_int_1=1000,
        max_int_2=1000,
        num_of_tests=1000
    )

    fib_sum_tests = Tests(
        name="fibonacci_sum_last_digit",
        package="6_last_digit_of_the_sum_of_fibonacci_numbers",
        tested_func="fib_sum_last_digit_fast",
        naive_func="fib_sum_last_digit_naive",
        test_data_type="single_int",
        max_int_1=1000,
        num_of_tests=1000
    )

    fib_partial_sum_tests = Tests(
        name="fibonacci_partial_sum",
        package="7_last_digit_of_the_sum_of_fibonacci_numbers_again",
        tested_func="fib_partial_sum_fast",
        naive_func="fib_partial_sum_naive",
        test_data_type="pair_of_ints",
        max_int_1=1000,
        max_int_2=1000,
        num_of_tests=1000
    )

    fib_sum_of_squares = Tests(
        name="fibonacci_sum_squares",
        package="8_last_digit_of_the_sum_of_squares_of_fibonacci_numbers",
        tested_func="fib_sum_squares_fast",
        naive_func="fib_sum_squares_naive",
        test_data_type="single_int",
        max_int_1=10**18,
        num_of_tests=1000
    )

    tests = [fib_sum_of_squares, fib_tests, fib_last_digit_tests,
             gcd_tests, lcm_tests, fib_mod_tests, fib_sum_tests,
             fib_partial_sum_tests]

    for test in tests:
        # test.test_correctness()
        test.test_timing(test.tested_func)
        # test.benchmark_timing()
