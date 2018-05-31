#!/usr/bin/env python3
# (C) Mikhail Kolodin, 2018, ver. 2018-05-31 1.1
# class ic test task: find 1st recurring character in a string

import random
import string

MINSIZE = 1       # min size of test string
MAXSIZE = 19      # its max size
TESTS = 10        # no of tests

alf = string.ascii_uppercase   # test alphabet

arr = []
size = 0


def prepare():
    """organize tests"""
    global arr, size

    size = random.randint(MINSIZE, MAXSIZE)
    arr = "".join([random.choice(alf) for i in range(size)])


def solve():
    """find char, reusable function"""

    found = ""

    for c in arr:
        if c in found:
            return c
        else:
            found += c
    else:
        return ""


def show():
    """find and show char, function to show result only"""

    c = solve()
    return c if c else "None"


def main():
    """run all"""

    for test in range(TESTS):
        prepare()
        print ("test =", test, ", size = %2d" % (size), ", arr =", arr.ljust(MAXSIZE), ", found recurrent:", show())


if __name__ == "__main__":
    main()
