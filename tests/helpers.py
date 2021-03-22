import random


def generate_random_ints(max_int, num_of_ints):
    return random.sample(range(max_int), k=num_of_ints)


def read_from_file(filename):
    with open(filename, "r") as f:
        return f.read()
