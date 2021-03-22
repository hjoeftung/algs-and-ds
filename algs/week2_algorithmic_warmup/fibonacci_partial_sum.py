# Uses python3
import sys


def fib_partial_sum_naive(start_idx, end_idx):
    dummy = start_idx
    start_idx = min(start_idx, end_idx)
    end_idx = max(dummy, start_idx, end_idx)

    sum = 0

    current = 0
    next  = 1

    for i in range(end_idx + 1):
        if i >= start_idx:
            sum += current

        current, next = next, current + next

    return sum % 10


def fib_partial_sum_fast(start_idx, end_idx):
    dummy = start_idx
    start_idx = min(start_idx, end_idx)
    end_idx = max(dummy, start_idx, end_idx)

    period = 60
    fib_sum_last_digits = [0, 1]

    for i in range(2, period + 1):
        fib_sum_last_digits.append(
            (fib_sum_last_digits[i - 1] + fib_sum_last_digits[i - 2] + 1) % 10)

    return (10 + fib_sum_last_digits[end_idx % period] -
            fib_sum_last_digits[(start_idx - 1) % period]) % 10


if __name__ == '__main__':
    pair_input = sys.stdin.read()
    start, end = map(int, pair_input.split())

    print(fib_partial_sum_fast(start, end))
