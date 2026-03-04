#!/usr/bin/env python
# solving queens problem for board of SIZE
# queens-26count.py non-recursive version
# Mikhail (myke) Kolodin, 2026-03-04, 2.6.2

import time

LIMIT = 4

def ok():
    """is it good so far?"""
    global SIZE, MAX, cnt, b, v

    if v == 0:
        return True
        
    for i in range(v):
        if b[i] == b[v] or v-i == abs(b[v] - b[i]):
            return False
    return True
    

def run():
    """run one size version"""
    global SIZE, MAX, cnt, b, v
    
    b = [0 for _ in range(SIZE)]
    v = 0

    while v >= 0:

        if b[v] > MAX:
            v -= 1
            b[v] += 1
            continue
        
        if ok():
            if v == MAX:
                cnt += 1
                v -= 1
                b[v] += 1
            else:
                v += 1
                b[v] = 0
        else:
            b[v] += 1


def main():
    """run all sizes"""

    global SIZE, MAX, cnt, b, v

    for SIZE in range(1, LIMIT+1):
        was = time.time()
        print(f"{SIZE=}", end=" -> ")
        MAX  = SIZE-1
        cnt = 0
        run()
        now = time.time()
        delta = now - was
        print(f"{cnt} solution(s), time = {delta:.8f}")


main()


# ~ SIZE=1 -> 1 solution(s), time = 0.00000477
# ~ SIZE=2 -> 0 solution(s), time = 0.00000715
# ~ SIZE=3 -> 0 solution(s), time = 0.00000572
# ~ SIZE=4 -> 2 solution(s), time = 0.00001454
# ~ SIZE=5 -> 10 solution(s), time = 0.00005174
# ~ SIZE=6 -> 4 solution(s), time = 0.00024366
# ~ SIZE=7 -> 40 solution(s), time = 0.00104189
# ~ SIZE=8 -> 92 solution(s), time = 0.00495005
# ~ SIZE=9 -> 352 solution(s), time = 0.02443624
# ~ SIZE=10 -> 724 solution(s), time = 0.12696886
# ~ SIZE=11 -> 2680 solution(s), time = 0.70354080
# ~ SIZE=12 -> 14200 solution(s), time = 4.32257199
# ~ SIZE=13 -> 73712 solution(s), time = 26.63431382
# ~ SIZE=14 -> 365596 solution(s), time = 177.84346104
