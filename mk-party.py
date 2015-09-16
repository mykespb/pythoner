#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# mk-party.py
# myke 2013-11-15 1.1
# recount payments for participants of the party

#data = {'miko': 20, 'lana': 30, 'sasha': 0, 'pavel': 5}
names = 'misha nastya elya kostya'.split ()
money = 248, 140, 40, 40

data = dict ([(names [i], money [i]) for i in xrange (len (money))])


def main ():
    print "party.py by myke started\n"
    parts = len (data)
    sumo = sum ([v for v in data.values ()])
    share = 1.0 * sumo / parts
    print "%8d - participants\n%8d - all money given\n%8d - avg part for 1 person" % (parts, sumo, share)
    lpers = sorted (data.keys ())
    print "\n%-15s%15s%15s" % ('personally', 'gave', '+add/-take')
    print "%-15s%15s%15s" % ('----------', '----------', '----------')
    for pers in lpers:
        print "%-15s%15d%+15d" % (pers, data [pers], share - data [pers])
    print "%-15s%15s%15s" % ('----------', '----------', '----------')
    print "\njob done.\n"
    return 0


if __name__ == '__main__':
    main ()

