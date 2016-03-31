#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mtm = myke's 'time manager
# 2016-03-31 1.10

# use:
# mkm <cmd> params
# writes to file $MTM (or ./mtm.log in current dir if $MTM is absent):
#     dt args
# commands: on off slept gone back stat
# see full docs below
# may be launched at computer start/ stop? restart
# maybe electron/ nw.js versioon will be added
# text stats + graph reports to be done

import sys, datetime, os

version = "1.10"
fout = os.getenv('MTM', os.getcwd() + '/mtm.log')

dt = str(datetime.datetime.now())[:-7]

cmdlist = "? help on off out up down home bed slept read tv inet chat busy prog ate study watch tea away stat walk sport travel report".split()
cmdlist.sort()

def main(args):
    print ("This is MTM myke's Time Management routine ver. {}" .format (version))
    #~ print (dt, sys.argv, fout)

    if len(sys.argv) > 1 and sys.argv[1] in cmdlist:
        if sys.argv[1] == "?":
            sys.argv[1] = "help"
        print (dt, *sys.argv[1:])
        with open (fout, 'a') as mtm:
            print (dt, *sys.argv[1:], file=mtm)
    else:
        print ("available commands are:", *cmdlist)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
