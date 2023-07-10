#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-jewels.py 2023-07-10 2023-07-10 1.0

import random 

from string import ascii_lowercase as letters

def make_string(lim):
    return "" .join( [ random.choice(letters) for _ in range(lim) ] )


def solve(jewels, stones):
    return sum([1 if stone in set(jewels) else 0 for stone in stones])


def test():
    jewels = make_string(5)
    stones = make_string(10)
    print(f"{jewels=}, {stones=}, solution={solve(jewels, stones)}")

test()

# jewels='eak', stones='qyasqqtrjq', solution=1
# jewels='wio', stones='ykevbpmdgz', solution=0
# jewels='wmb', stones='lhejfmtios', solution=1
# jewels='rxqcu', stones='pjbedcxzzc', solution=3

# Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.
