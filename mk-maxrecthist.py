#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-maxrecthist.py
#  find rectangle in histogram with max square
#
#  See also: https://www.youtube.com/watch?v=VNbkzsnllsU
#  Coding Interview Problem: Largest Rectangle in a Histogram
#  (but solving method is not from there)
#
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-02 0.2

import random

NO_TESTS = 1       # # of tests
MAX_HOR = 10       # max # of columnes
MAX_VERT = 10      # max column height

HOR = 0            # sizes for this run
VERT = 0

hist = ()          # histoghram, global


def generate():
    """generate histogram"""
    global hist, HOR, VERT
    HOR = random.randint(1, MAX_HOR)
    VERT = random.randint(MAX_VERT//2, MAX_VERT)
    hist = [random.randint(0, VERT) for _ in range(HOR)]
    print(hist)


def solve():
    """solve task: find max area"""
    #TODO
    pass


def main(args):
    """runner"""
    for test in range(NO_TESTS):
        print("\n*** test", test, "***\n")
        generate()
        solve()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
