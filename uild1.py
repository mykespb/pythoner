#!/usr/bin/env python

# testing ULID
# https://github.com/ahawker/ulid  -- Universally Unique Lexicographically Sortable Identifier (ULID) in Python 3

import ulid

def test1 ():
    """ simply print ulid """

    u = ulid.new ()
    print (u.str)
    print (u.int)


def better (n : int) -> str :
    """ function to convert ulid to even better coding 62 """

    if n == 0:
        return '0'

    alf = '0123456789'
    alf += 'abcdefghijklmnopqrstuvwxyz'
    alf += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lalf = len(alf)
    res = ''

    while n:
        r  = n % lalf
        res = alf[r] + res
        n //= lalf

    return res


def test3 ():
    """ test better coding """

    alf = '0123456789'
    alf += 'abcdefghijklmnopqrstuvwxyz'
    alf += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lalf = len(alf)

    print (f"alf = [{alf}], len-alf={lalf}")
    for i in range(300):
        print (f"{i} -> {better(i)}")


def test2 ():
    """ test ulid + better """

    for i in range (100):
        c = ulid.new()
        print (f"ulid = {c.str}, n = {c.int}, better={better(c.int)}")

test1 ()
test2 ()
test3 ()

# the end.

