# Uses python3
import sys


def get_change(m):
    total_coins = 0
    while m >= 10:
        total_coins += m // 10
        m = m % 10

    while m >= 5:
        total_coins += m // 5
        m = m % 5

    while m >= 1:
        total_coins += 1
        m -= 1

    return total_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
