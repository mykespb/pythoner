#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-concells.py
#  find largest area of connected cells in rectangular matrix
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-05 1.0

import random, pprint

# setting
NO_TESTS = 1
# size of  matrix
ROWS = 10
COLS = 10

#randomization parameter, the more it is the less 1s exist in matrix
RAND = 3

# global default matrix for manual testing
# size of  matrix
mat = []
#mat = [[1, 0, 0, 1],
#       [1, 0, 0, 1],
#       [0, 1, 1, 0],
#       [0, 0, 0, 0]]
# default size
#ROWS = 10
#COLS = 10

# results
best_i = best_j = best_size = 0

def generate():
    """fill the matrix"""
    global mat

    for i in range(ROWS):
        row = [1 if not random.randint(0, RAND) else 0 for _ in range(COLS)]
        mat += [row]
    pprint.pprint(mat)


def solve():
    """solve the problem"""
    global mat, best_i, best_j, best_size

    for i in range(ROWS):
        for j in range(COLS):
            if mat[i][j]:
                size = proc_group(i, j)

    if best_size:
        print("\nWe found the best groupi at", best_i, best_j, "of size", best_size)
    else:
        print("\nAlas, no groups found in matrix")


def proc_group(i, j, size=0):
    """process one group"""
    global mat, best_i, best_j, best_size

    if i<0 or i>=ROWS or j<0 or j>=COLS or mat[i][j] != 1:
        return 0

    mat[i][j] = 2
    size += 1

    size += proc_group(i-1, j-1)
    size += proc_group(i-1, j)
    size += proc_group(i-1, j+1)
    size += proc_group(i,   j-1)
    size += proc_group(i,   j+1)
    size += proc_group(i+1, j-1)
    size += proc_group(i+1, j)
    size += proc_group(i+1, j+1)

    if size > best_size:
        best_size = size
        best_i = i
        best_j = j

    return size


def main(args):
    """runner"""
    for test in range(NO_TESTS):
        print("\n*** test", test, "***\n")
        generate()
        solve()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

