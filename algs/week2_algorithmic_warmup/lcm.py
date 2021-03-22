# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(first_num, second_num):
    if first_num < second_num:
        dummy = first_num
        first_num = second_num
        second_num = dummy

    if second_num == 0:
        return first_num
    else:
        return gcd_fast(second_num, first_num % second_num)


def lcm_fast(a, b):
    return int(a * b / gcd_fast(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
