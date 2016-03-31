#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mtm = myke's 'time manager
# 2016-03-31 1.13

# use:
# mkm <cmd> params
# writes to file $MTM (or ./mtm.log in current dir if $MTM is absent):
#     dt args
# commands: on off slept gone back stat
# see full docs below
# may be launched at computer start/ stop? restart
# maybe electron/ nw.js versioon will be added
# text stats + graph reports to be done

import sys, datetime, os, pprint

version = "1.11"

dt = str(datetime.datetime.now())[:-7]
dtdir = dt[:10]
fout = os.getenv('MTM', os.getcwd()) + "/" + dtdir + '.log'

grocc = {
    "status":     "on off out away".split(),
    "state":      "up down".split(),
    "busy":       "busy prog study".split(),
    "home":       "home life eat tea child".split(),
    "rest":       "walk bed sleep chat fun tv inet watch".split(),
    "active":     "travel sport".split(),
    "result":     "stat report".split(),
    "info":       "? help".split()
}

occs = []
for x in grocc.values():
    occs.extend(x)
occs.sort()

def main(args):
    print ("This is MTM myke's Time Management routine ver. {}" .format (version))
    print ("Log goes to", fout)
    #~ print (dt, sys.argv, fout)

    if len(sys.argv) > 1 and sys.argv[1] in occs:
        if sys.argv[1] == "?":
            sys.argv[1] = "help"
        print (dt, *sys.argv[1:])
        with open (fout, 'a') as mtm:
            print (dt, *sys.argv[1:], file=mtm)
    else:
        print ("available commands are:")
        pprint.pprint (grocc)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
