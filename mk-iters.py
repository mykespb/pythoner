#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-iters.py 2015-03-11 M.Kolodin
# convert to py3 2018-05-02

import itertools, pprint, functools
# note that itertools now do not have reduce, it is moved to functools

SIZE = 6

l = [list(itertools.combinations(range(1, SIZE+1), n)) for n in range(1, SIZE+1)]
pprint.pprint (l)

#lm = lambda ll: sum(ll, [])
#lm = lambda ll: [el for l in ll for el in l]
lm = lambda s: functools.reduce(lambda d,el: d.extend(el) or d, s, [])
pprint.pprint(lm(l))

#~ [[(1,), (2,), (3,), (4,), (5,), (6,)],
 #~ [(1, 2),
  #~ (1, 3),
  #~ (1, 4),
  #~ (1, 5),
  #~ (1, 6),
  #~ (2, 3),
  #~ (2, 4),
  #~ (2, 5),
  #~ (2, 6),
  #~ (3, 4),
  #~ (3, 5),
  #~ (3, 6),
  #~ (4, 5),
  #~ (4, 6),
  #~ (5, 6)],
 #~ [(1, 2, 3),
  #~ (1, 2, 4),
  #~ (1, 2, 5),
  #~ (1, 2, 6),
  #~ (1, 3, 4),
  #~ (1, 3, 5),
  #~ (1, 3, 6),
  #~ (1, 4, 5),
  #~ (1, 4, 6),
  #~ (1, 5, 6),
  #~ (2, 3, 4),
  #~ (2, 3, 5),
  #~ (2, 3, 6),
  #~ (2, 4, 5),
  #~ (2, 4, 6),
  #~ (2, 5, 6),
  #~ (3, 4, 5),
  #~ (3, 4, 6),
  #~ (3, 5, 6),
  #~ (4, 5, 6)],
 #~ [(1, 2, 3, 4),
  #~ (1, 2, 3, 5),
  #~ (1, 2, 3, 6),
  #~ (1, 2, 4, 5),
  #~ (1, 2, 4, 6),
  #~ (1, 2, 5, 6),
  #~ (1, 3, 4, 5),
  #~ (1, 3, 4, 6),
  #~ (1, 3, 5, 6),
  #~ (1, 4, 5, 6),
  #~ (2, 3, 4, 5),
  #~ (2, 3, 4, 6),
  #~ (2, 3, 5, 6),
  #~ (2, 4, 5, 6),
  #~ (3, 4, 5, 6)],
 #~ [(1, 2, 3, 4, 5),
  #~ (1, 2, 3, 4, 6),
  #~ (1, 2, 3, 5, 6),
  #~ (1, 2, 4, 5, 6),
  #~ (1, 3, 4, 5, 6),
  #~ (2, 3, 4, 5, 6)],
 #~ [(1, 2, 3, 4, 5, 6)]]

#~ l= list(itertools.combinations(range(1, 6), 3))
#~ print l

#~ http://habrahabr.ru/post/63539/
