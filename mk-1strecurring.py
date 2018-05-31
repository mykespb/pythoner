#!/usr/bin/env python3
# (C) Mikhail Kolodin, 2018, ver. 1.0
# class ic test task: find 1st recurring character in a string

import random
import string

MINSIZE = 1       # min size of test string
MAXSIZE = 9       # its max size
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
    """find char"""
    global arr

    found = ""

    for c in arr:
        if c in found:
            return c
        else:
            found += c
    else:
        return "None"


def main():
    """run all"""
    global arr, szie

    for test in range(TESTS):
        prepare()
        print ("test =", test, ", size =", size, ", arr =", arr.ljust(MAXSIZE), ", found recurrent:", solve())

main()
