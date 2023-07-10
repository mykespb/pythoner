#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-anagram-cnt.py 2023-07-10 2023-07-10 1.0
# find all anagrams in given text
# return tuple of tuples with anagramix words

from collections import Counter

text = """
123 231
ethic cithe
удача дочка
"""

def tests():
    for atest in text.split("\n"):
        if atest == "":
            continue
        print("test:", atest, "=>", test(atest))

def test(atest):
    s1, s2 = atest.split()
    return Counter(s1) == Counter(s2)

tests()

# test: 123 231 => True
# test: ethic cithe => True
# test: удача дочка => False
