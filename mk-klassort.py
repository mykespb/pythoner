#!/usr/bin/python2
# myke qp.py 2012-12-19 2
# myke: klass sorting

from pprint import pprint as pp
from random import choice as rc, randint as ri
klen, god, godplus = 20, 2000, 4
exmin, exmax, pointmin, pointmax = 0, 4, 2, 5
nfirst = 'kate john mike pete jack max gleb alex sara tony ann'.split()
nlast  = 'green doomy lucky geany smith tall white long easy tiny'.split()

klass = [(k+1, (rc(nlast), rc(nfirst)), (ri(1, 28), ri(1, 12), ri(god, god+godplus)), [ri(pointmin, pointmax) for j in range(ri(exmin, exmax))] ) for k in xrange(klen)]
print "klass as is="; pp(klass)

klasdated = sorted(klass, key = lambda x: (x[2][1], x[2][0]))
print "\n\nklass by dates="; pp(klasdated)
klaspointed = sorted(klass, key = lambda x: sum(x[3]))[::-1]
print "\n\nklass by exam points="; pp(klaspointed)

#~ result:
#~ klass as is=
#~ [(1, ('green', 'tony'), (13, 1, 2001), []),
 #~ (2, ('lucky', 'alex'), (28, 12, 2002), [5, 3, 5]),
 #~ (3, ('easy', 'mike'), (4, 9, 2003), [2]),
 #~ (4, ('white', 'jack'), (2, 5, 2000), [4, 3, 4]),
 #~ (5, ('smith', 'mike'), (26, 10, 2003), [5]),
 #~ (6, ('green', 'jack'), (19, 6, 2003), []),
 #~ (7, ('white', 'gleb'), (25, 4, 2000), [2, 3, 4, 3]),
 #~ (8, ('geany', 'pete'), (24, 7, 2003), [3, 5, 4]),
 #~ (9, ('lucky', 'gleb'), (24, 5, 2002), [2, 5, 5]),
 #~ (10, ('white', 'gleb'), (5, 5, 2004), []),
 #~ (11, ('smith', 'gleb'), (12, 3, 2000), [5, 4, 5, 4]),
 #~ (12, ('geany', 'jack'), (23, 10, 2003), []),
 #~ (13, ('green', 'pete'), (19, 7, 2001), []),
 #~ (14, ('geany', 'mike'), (12, 1, 2004), [5, 2, 4, 4]),
 #~ (15, ('smith', 'sara'), (21, 7, 2001), [5, 4, 4, 5]),
 #~ (16, ('lucky', 'kate'), (19, 1, 2002), [2, 5, 4]),
 #~ (17, ('geany', 'ann'), (10, 12, 2004), [2, 5, 5, 4]),
 #~ (18, ('lucky', 'max'), (23, 7, 2001), [5]),
 #~ (19, ('long', 'max'), (28, 3, 2004), [3, 2, 2]),
 #~ (20, ('lucky', 'sara'), (11, 10, 2001), [4, 3, 2, 3])]
#~ 
#~ 
#~ klass by dates=
#~ [(14, ('geany', 'mike'), (12, 1, 2004), [5, 2, 4, 4]),
 #~ (1, ('green', 'tony'), (13, 1, 2001), []),
 #~ (16, ('lucky', 'kate'), (19, 1, 2002), [2, 5, 4]),
 #~ (11, ('smith', 'gleb'), (12, 3, 2000), [5, 4, 5, 4]),
 #~ (19, ('long', 'max'), (28, 3, 2004), [3, 2, 2]),
 #~ (7, ('white', 'gleb'), (25, 4, 2000), [2, 3, 4, 3]),
 #~ (4, ('white', 'jack'), (2, 5, 2000), [4, 3, 4]),
 #~ (10, ('white', 'gleb'), (5, 5, 2004), []),
 #~ (9, ('lucky', 'gleb'), (24, 5, 2002), [2, 5, 5]),
 #~ (6, ('green', 'jack'), (19, 6, 2003), []),
 #~ (13, ('green', 'pete'), (19, 7, 2001), []),
 #~ (15, ('smith', 'sara'), (21, 7, 2001), [5, 4, 4, 5]),
 #~ (18, ('lucky', 'max'), (23, 7, 2001), [5]),
 #~ (8, ('geany', 'pete'), (24, 7, 2003), [3, 5, 4]),
 #~ (3, ('easy', 'mike'), (4, 9, 2003), [2]),
 #~ (20, ('lucky', 'sara'), (11, 10, 2001), [4, 3, 2, 3]),
 #~ (12, ('geany', 'jack'), (23, 10, 2003), []),
 #~ (5, ('smith', 'mike'), (26, 10, 2003), [5]),
 #~ (17, ('geany', 'ann'), (10, 12, 2004), [2, 5, 5, 4]),
 #~ (2, ('lucky', 'alex'), (28, 12, 2002), [5, 3, 5])]
#~ 
#~ 
#~ klass by exam points=
#~ [(15, ('smith', 'sara'), (21, 7, 2001), [5, 4, 4, 5]),
 #~ (11, ('smith', 'gleb'), (12, 3, 2000), [5, 4, 5, 4]),
 #~ (17, ('geany', 'ann'), (10, 12, 2004), [2, 5, 5, 4]),
 #~ (14, ('geany', 'mike'), (12, 1, 2004), [5, 2, 4, 4]),
 #~ (2, ('lucky', 'alex'), (28, 12, 2002), [5, 3, 5]),
 #~ (20, ('lucky', 'sara'), (11, 10, 2001), [4, 3, 2, 3]),
 #~ (9, ('lucky', 'gleb'), (24, 5, 2002), [2, 5, 5]),
 #~ (8, ('geany', 'pete'), (24, 7, 2003), [3, 5, 4]),
 #~ (7, ('white', 'gleb'), (25, 4, 2000), [2, 3, 4, 3]),
 #~ (16, ('lucky', 'kate'), (19, 1, 2002), [2, 5, 4]),
 #~ (4, ('white', 'jack'), (2, 5, 2000), [4, 3, 4]),
 #~ (19, ('long', 'max'), (28, 3, 2004), [3, 2, 2]),
 #~ (18, ('lucky', 'max'), (23, 7, 2001), [5]),
 #~ (5, ('smith', 'mike'), (26, 10, 2003), [5]),
 #~ (3, ('easy', 'mike'), (4, 9, 2003), [2]),
 #~ (13, ('green', 'pete'), (19, 7, 2001), []),
 #~ (12, ('geany', 'jack'), (23, 10, 2003), []),
 #~ (10, ('white', 'gleb'), (5, 5, 2004), []),
 #~ (6, ('green', 'jack'), (19, 6, 2003), []),
 #~ (1, ('green', 'tony'), (13, 1, 2001), [])]
