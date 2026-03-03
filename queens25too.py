# solving queens problem for board of SIZE
# queens-25too.py non-recursive version
# Mikhail (myke) Kolodin, 2026-03-03, 2.5.0
# most time inefficient version

from itertools import permutations

SIZE = 8

def psolution():

    print("solution:", cnt, ", board:", p, end=", letters: ")
    for i, c in enumerate(p):
        print("abcdefghijklmnopqrstuvwxyz"[i] + str(c+1), end=" ")
    print()


def ok():

    for i in range(1, SIZE):
        for j in range(i):
            if p[i] == p[j] or i-j == abs(p[i]-p[j]):
                return False
    return True


def main():

    global p, cnt
    cnt = 0
    
    for p in permutations( range(SIZE), SIZE):
        if ok():
            cnt += 1
            psolution()

    if cnt == 0:
        print("no solutions")

main()
