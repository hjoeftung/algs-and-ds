# python3

from collections import namedtuple, deque


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = deque()
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i + 1))

        if char in ")]}":
            if opening_brackets_stack:
                last_left_bracket = opening_brackets_stack.pop()
                if are_matching(last_left_bracket[0], char):
                    continue

            return i + 1

    if not opening_brackets_stack:
        return "Success"
    return opening_brackets_stack.popleft()[1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
