#!/usr/bin/env python

SIZE = 4

def rc_queens(n_col, width, sol):
    global cnt
    if len(sol) == width:
        cnt += 1
        print("solution %2d:" % cnt, sol)
    else:
        for n_row in range(width):
            if safe_queen(n_row, n_col, sol):
                rc_queens(n_col+1, width, sol+[n_row])

def safe_queen(new_row, new_col, sol):
    for col in range(len(sol)):
        if sol[col] == new_row or abs(col - new_col) == abs(sol[col] - new_row):
            return False
    return True

def main():
    for n in range(SIZE):
        rc_queens(1, SIZE, [n])

cnt = 0
main()
