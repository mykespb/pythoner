#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-uniqchar1.py myke 2016-08-28 1.3

from collections import Counter

tests = "string to be tested", "another string as we see it", "строка по-русски"

def check (stroka):
    """ checker for unique characters """
    print (stroka, "=>", [k for k, v in Counter (stroka) .items() if v==1])

def main():
    """ dispatcher """
    for test in tests: check (test)

main()
