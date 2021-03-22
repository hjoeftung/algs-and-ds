# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0, 0)
    stops.append(distance)
    stops_count = 0
    current_refill = 0
    distance_passed = 0

    for i in range(1, len(stops)):
        if distance > distance_passed:
            if stops[i] - stops[current_refill] <= tank:
                continue
            else:
                if stops[i] - stops[i - 1] <= tank:
                    stops_count += 1
                    distance_passed += stops[i - 1] - stops[current_refill]
                    current_refill = i - 1
                else:
                    return -1

    return stops_count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
