# Uses python3
from math import sqrt


def fib_naive(n):
    if (n <= 1):
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def fib_instant(n):
    return int((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5))


if __name__ == "__main__":
    n = int(input())
    print(fib_fast(n))
