#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mikhail (myke) Kolodin, 2015
# mk-line.py 2015-04-05 2015-04-05 1.2
# найти наибольший слившийся отрезок

from random import randint as ri

ALL  = 60   # общая длина
MLEN = 10   # макс длина отрезка
NUM  = 10   # всего отрезков

EOL  = "\n" # EOL :)
a = []
b = []
sa = []
need = 1

def generate():
    """ make source data """
    global a
    a = [(ri(0, ALL-MLEN), ri(1, MLEN)) for i in range(NUM)]

def regenerate():
    """ reformat source data """
    global a, sa
    a = [(x[1], x[0], x[0]+x[1]-1) for x in a]
    sa = a[:]

def show():
    """ show source data """
    SUP  = "".join(str(i) * 10 for i in range(ALL//10))[:ALL]
    METR = "0123456789" * (ALL//10)
    print ("\n" + SUP)
    print (METR, EOL)
    for s in a:
        print (" " * (s[1]-1), "*" * s[0], EOL, end="")
    print (METR, "\n"+SUP, EOL)

def inter (p, q):
    """ find intersections """
    global need
    if p[2]<q[1]-1 or q[2]<p[1]-1:
        return []
        #~ return [p, q]
    if p==q:
        return [p]
    if p[1]>=q[1] and p[2]<=q[2]:
        return [q]
    if q[1]>=p[1] and q[2]<=p[2]:
        return [p]
    al = min(p[1], q[1])
    ar = max(p[2], q[2])
    ll = ar-al+1
    need = 1
    return [(ll, al, ar)]

def solve():
    """ solve all """
    global a, b, need
    need = 1
    while need:
        need = 0
        b = []
        c = a
        for i in a[:]:
            for j in a[:]:
                b.extend (inter(i, j))
        a = list(set(b))
        a.sort(reverse=True)
        if a==c:
            return

def solvarr():
    """ simple solve """
    b = [0 for i in range(ALL)]
    for i in sa:
        for j in range(i[1], i[2]+1):
            b[j] = 1
    sl = sr = ll = state = maxl = maxr = maxs = 0
    for i in range(len(b)):
        if state == 0 and b[i]:
            sl = sr = i
            ll = state = 1
            if maxs == 0:
                maxl = maxr = i
                maxs = 1
        elif state and b[i]:
            sr = i
            ll += 1
            if maxs < ll:
                maxl = sl
                maxr = sr
                maxs = ll
        else:
            state = 0
    print ("\narray maximum:", (maxs, maxl, maxr))

def best():
    """ show best result """
    global a, b
    b = list(set(b))
    b.sort (reverse=True)
    print ("best =", b[0])
    SUP  = "".join(str(i) * 10 for i in range(ALL//10))[:ALL]
    METR = "0123456789" * (ALL//10)
    print ("\n" + SUP)
    print (METR)
    print (" " * (b[0][1]-1), "*" * b[0][0], EOL, end="")
    print (METR, "\n"+SUP, EOL)
    print ("all the best:",  sorted([x for x in b if x[0] == b[0][0]]))
    #~ print ("all totally:", b)

def main():
    """ main dispatcher """
    generate()
    regenerate()
    show()
    solve()
    best()
    solvarr()

main()

# 000000000011111111112222222222333333333344444444445555555555
# 012345678901234567890123456789012345678901234567890123456789
#
#                                           **********
#                                            ********
#                                  **
#                                                 *******
#            *******
#                    ***
#                                        **
#         **
#      ******
#       ********
# 012345678901234567890123456789012345678901234567890123456789
# 000000000011111111112222222222333333333344444444445555555555
#
# best = (13, 42, 54)
#
# 000000000011111111112222222222333333333344444444445555555555
# 012345678901234567890123456789012345678901234567890123456789
#                                           *************
# 012345678901234567890123456789012345678901234567890123456789
# 000000000011111111112222222222333333333344444444445555555555
#
# all the best: [(13, 5, 17), (13, 42, 54)]
#
# array maximum: (13, 5, 17)
