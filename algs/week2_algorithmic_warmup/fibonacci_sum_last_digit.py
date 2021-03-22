# Uses python3
import sys


def fib_sum_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fib_sum_last_digit_fast(n):
    if n <= 1:
        return n

    period = 60
    fib_sum_last_digits = [0, 1]

    for i in range(2, period + 1):
        fib_sum_last_digits.append(
            (fib_sum_last_digits[i - 1] + fib_sum_last_digits[i - 2] + 1) % 10)

    return fib_sum_last_digits[n % period]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_last_digit_fast(n))
