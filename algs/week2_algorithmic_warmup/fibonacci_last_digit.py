# Uses python3
import sys

def fib_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def fib_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fib_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


def find_period_of_last_num():
    for i in range(1, 101):
        if fib_fast(i) % 10 == 0 and fib_fast(i+1) == 1:
            return i


def fib_last_digit_instant(n):
    period = 60

    if n <= 1:
        return n

    fib_last_digits = [0, 1]

    for i in range(2, period + 1):
        fib_last_digits.append(
            (fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10)

    return fib_last_digits[n % period]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    print(fib_last_digit_instant(60))
