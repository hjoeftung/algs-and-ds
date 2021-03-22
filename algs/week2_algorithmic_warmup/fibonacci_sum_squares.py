# Uses python3
from sys import stdin


def fib_last_digit_instant(n):
    period = 60

    if n <= 1:
        return n

    fib_last_digits = [0, 1]

    for i in range(2, period + 1):
        fib_last_digits.append(
            (fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10)

    return fib_last_digits[n % period]


def fib_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fib_sum_squares_fast(n):
    period = 60

    fib_last_digits = [0, 1]

    for i in range(2, period + 1):
        fib_last_digits.append(
            (fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10)

    return (fib_last_digits[n % period] *
            (fib_last_digits[n % period] +
             fib_last_digits[(n - 1) % period]) % 10) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_sum_squares_fast(n))
