# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    max_value = 0.
    # write your code here
    sorted_items = list(sorted(
        zip(weights, values),
        key=lambda weight_value_pair: weight_value_pair[1] / weight_value_pair[0],
        reverse=True
    ))

    for item in sorted_items:
        if item[0] <= capacity:
            max_value += item[1]
            capacity -= item[0]
            continue
        else:
            fitting_item_fraction_weight = capacity / item[0]
            fitting_item_fraction_value = fitting_item_fraction_weight * item[1]
            max_value += fitting_item_fraction_value
            break

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
