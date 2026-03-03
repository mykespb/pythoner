#!/usr/bin/env python
# solving queens problem for board of SIZE
# queens-24nr.py non-recursive version
# Mikhail (myke) Kolodin, 2026-03-03, 2.4.1

SIZE = 8
MAX  = SIZE-1

def psolution(sol):
    """print solution from sol"""
    global cnt

    cnt += 1
    print(f"solution {cnt}: {b}", end=" -> ")
    
    for i, c in enumerate(sol):
        print("abcdefghijklmnopqrstuvwxyz"[i] + str(c+1), end=" ")
    print()


def ok():
    """is it good so far?"""

    if v == 0:
        return True
        
    for i in range(v):
        if b[i] == b[v] or v-i == abs(b[v] - b[i]):
            return False
    return True
    

def main():
    """run it all"""
    global b, v
    
    b = [0 for _ in range(SIZE)]
    v = 0

    while v >= 0:

        if b[v] > MAX:
            v -= 1
            b[v] += 1
            continue
        
        if ok():
            if v == MAX:
                psolution(b)
                v -= 1
                b[v] += 1
            else:
                v += 1
                b[v] = 0
        else:
            b[v] += 1


assert SIZE > 1
cnt = 0
main()


# ~ solution 92: [7, 3, 0, 2, 5, 1, 6, 4] -> a8 b4 c1 d3 e6 f2 g7 h5
