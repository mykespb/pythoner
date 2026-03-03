#!/usr/bin/env python
# solving queens problem for board of SIZE
# queens-26count.py non-recursive version
# Mikhail (myke) Kolodin, 2026-03-03, 2.6.1

LIMIT = 10

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
        print(f"{SIZE=}", end=" -> ")
        MAX  = SIZE-1
        cnt = 0
        run()
        print(f"{cnt} solution(s)")


main()


# ~ SIZE=1 -> 1 solution(s)
# ~ SIZE=2 -> 0 solution(s)
# ~ SIZE=3 -> 0 solution(s)
# ~ SIZE=4 -> 2 solution(s)
# ~ SIZE=5 -> 10 solution(s)
# ~ SIZE=6 -> 4 solution(s)
# ~ SIZE=7 -> 40 solution(s)
# ~ SIZE=8 -> 92 solution(s)
# ~ SIZE=9 -> 352 solution(s)
# ~ SIZE=10 -> 724 solution(s)
# ~ SIZE=11 -> 2680 solution(s)
# ~ SIZE=12 -> 14200 solution(s)
