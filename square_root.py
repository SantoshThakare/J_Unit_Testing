import math
"""
Write a static function sqrt to compute the square root of a non-negative number c
given in the input using Newton's method:
"""


def square_root(number):

    return round(math.sqrt(number), 3)


if __name__ == "__main__":
    root = square_root(9)
    print(root)