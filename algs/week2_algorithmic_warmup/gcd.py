# Uses python3
import sys


def gcd_naive(first_num, second_num):
    if first_num == 0:
        return second_num

    if second_num == 0:
        return first_num

    current_gcd = 1
    for d in range(2, min(first_num, second_num) + 1):
        if first_num % d == 0 and second_num % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(first_num, second_num):
    if first_num < second_num:
        dummy = first_num
        first_num = second_num
        second_num = dummy

    if second_num == 0:
        return first_num
    else:
        return gcd_fast(second_num, first_num % second_num)


if __name__ == "__main__":
    input_nums = sys.stdin.read()
    a, b = map(int, input_nums.split())
    print(gcd_fast(a, b))
