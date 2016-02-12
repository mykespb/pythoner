#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-anagram.py 2016-02-12 2016-02-12 1.0
# find all anagrams in given text

text = """
123 345 231
ethic thetic tethic
удача учада чаадаев овин вино нави винна
"""

def base (t):
    """ find basic form of word """
    return str("".join(sorted(t)))

def trovu (t):
    """ find all anagrams in given list of words """
    res = {}
    for w in t:
        ind = base(w)
        if ind in res:
            res [ind] += [w]
        else:
            res [ind] = [w]
    res = [res[x] for x in res if len(res[x])>1]
    res = [sorted(x) for x in res]
    return sorted(res)

def main(args):
    print (trovu (text.split()))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
