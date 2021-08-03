#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# таблица умножения

def tabmult2():
    for i in range(1, 10):
        for j in range(1, 10):
            print ( "%3d" % (i*j,), end="")
        print()

def main(args):
    tabmult2()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
