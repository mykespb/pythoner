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
#  ver. 2018-06-02 1.0 naive slow solution

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

    print(hist, "\n")
    pretty(hist)


def pretty(h):
    """print pretty histogram"""

    for j in range(VERT, 0, -1):
        for i in range(HOR):
            print("* " if hist[i] >= j else "  ", end="")
        print()

    for i in range(HOR):
        print(i, end=" ")
    print("\n")


def solve():
    """solve task: find max area"""
    # bests
    best_start = 0
    best_area = 0
    best_top = 0
    best_end = 0

    for si in range(HOR):
        if hist[si] == 0:
            continue
        for sj in range(1, hist[si]+1):
            area, bend = calc_area(si, sj)
            if area > best_area:
                best_start = si
                best_end = bend
                best_area = area
                best_top = sj
                print("debug: found better: start=", best_start, ", end=", best_end, ", top=", best_top, ", area=", best_area)

    print("\nsolution: start=", best_start, ", end=", best_end, ", top=", best_top, ", area=", best_area)


def calc_area(si, sj):
    """calc area of rectangle in histogram starting in column si and having height sj"""

    area = sj
    bend = si
    for ei in range(si+1, HOR):
        if hist[ei] >= sj:
            area += sj
            bend = ei
        else:
            break

    return area, bend


def main(args):
    """runner"""
    for test in range(NO_TESTS):
        print("\n*** test", test, "***\n")
        generate()
        solve()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
