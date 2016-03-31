#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mtm = myke's 'time manager
# 2016-03-31 1.2

# use:
# mkm <cmd> params
# writes to file $MTM (or mtm.log in current dir if $MTM is absent):
#     dt args
# commands: on off slept gone back stat
# see full docs below
# may be launched at computer start/ stop? restart
# maybe electron/ nw.js versioon will be added
# text stats + graph reports to be done

import sys, datetime

version = "0.1"

dt = str(datetime.datetime.now())[:-7]

cmdlist = "? help on off out dreamt slept busy prog ate away stat report".split()

def main(args):
    print ("This is MTM myke's Time Management routine ver. {}" .format (version))
    #~ print (dt, sys.argv)

    if len(sys.argv) > 1 and sys.argv[1] in cmdlist:
        if sys.argv[1] == "?":
            sys.argv[1] = "help"
        print (dt, *sys.argv[1:])
        fout = 'mtm.log'
        with open (fout, 'a') as mtm:
            print (dt, *sys.argv[1:], file=mtm)
    else:
        print ("available commands are:", *cmdlist)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
