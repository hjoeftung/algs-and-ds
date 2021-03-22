# Uses python3
import sys
from importlib import import_module


def fib_mod_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fib_mod_fast(n, m):
    fib_nums = [0, 1, 1]
    fib_nums_mods = [0, 1, 1]

    if n <= 2:
        return fib_nums_mods[n]

    cur_index = 3
    while True:
        if fib_nums_mods[cur_index - 1] == 1 and \
                fib_nums_mods[cur_index - 2] == 0:
            break

        fib_nums.append(fib_nums[cur_index-1] + fib_nums[cur_index-2])
        fib_nums_mods.append(fib_nums[cur_index] % m)
        cur_index += 1

    period = len(fib_nums_mods) - 2

    return fib_nums_mods[n % period]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fib_mod_fast(n, m))
