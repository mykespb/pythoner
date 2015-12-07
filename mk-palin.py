#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-palin.py 2015-12-07 1.1
# build & check palinndromic numbers

#  test data
todo = "1 12 135 256 196" .split()

# max number of repetitions
MAX = 1000
# MAX=30000 is not enough for 196 (!)
# MAX number of printed iterations
MAXPRINT = 100

def proc (n):
    """process number (given as line)"""

    print ("Given:              ", n)

    if len(n) == 0:
        print ("Error: empty string")
        return 0

    if len(n) == 1:
        print ("OK: ", n)
        return 1

    steps = 0
    while steps < MAX:

        steps += 1
        obr = n[::-1]

        if n == obr:
            print ("Hurra: we've got a palindom {}" .format(n))
            return 1

        if steps < MAXPRINT:
            print ("Reversed:           ", obr)
        n = str (int (n) + int (obr))
        if steps < MAXPRINT:
            print ("Next {0:10}:     {1}" . format (steps, n))

    print ("Alas, MAX ({}) is achieved" . format(MAX))
    return 0

def main(args):
    """main dispatcher"""
    divline = "\n\n==================================================\n"
    for n in todo:
        print (divline, "\nProcessing: ", n)
        proc (n)
    print (divline)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
