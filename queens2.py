#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rc_queens(n_col, width, sol):
    if len(sol) == width:
        print sol
    else:
        for n_row in range(width):
            if (safe_queen(n_row, n_col, sol)):
                rc_queens(n_col+1, width, sol+[n_row])

def safe_queen(new_row, new_col, sol):
    for col in range(len(sol)):
        if (sol[col] == new_row or
            abs(col - new_col) == abs(sol[col] - new_row)):
                return 0
    return 1

if __name__ == "__main__":
    for n in range(8):
        rc_queens(1, 8, [n])
