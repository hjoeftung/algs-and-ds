from random import randint
from timeit import timeit

from week1_programming_challenges.max_pairwise_product \
    import max_pairwise_product as fast_implementation


def slow_implementation(num_array):
    product = num_array[0] * num_array[1]

    for i in range(len(num_array)):
        for j in range(i + 1, len(num_array)):
            product = max(product, num_array[i] * num_array[j])

    return product


def test_correctness(max_len_of_array=50, max_num=1000, num_of_tests=1000):
    for i in range(num_of_tests):
        len_of_test_array = randint(2, max_len_of_array)
        test_array = [randint(-max_num, max_num)
                      for _ in range(len_of_test_array)]

        correct_result = slow_implementation(test_array)
        tested_result = fast_implementation(test_array)

        if correct_result == tested_result:
            print(f"{i} test passed")

        else:
            print("Test failed: ", test_array,
                  correct_result, tested_result)
            return


def test_timing():
    print(timeit(test_correctness, number=1) / 1000)


if __name__ == "__main__":
    test_timing()
