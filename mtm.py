#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mtm = myke's 'time manager
# 2016-04-26 1.38

# use:
# mkm <cmd> params
# writes to file $MTM (or ./mtm.log in current dir if $MTM is absent):
#     dt args
# commands: on off slept gone back stat
# see full docs below
# may be launched at computer start/ stop? restart
# maybe electron/ nw.js versioon will be added
# text stats + graph reports to be done

import sys, datetime, os, collections
# pprint

version = "2016-04-26 1.38"

dt = str(datetime.datetime.now())[:-7]
dtdir = dt[:7]  # just YYYY-MM
fout = os.getenv('MTM', os.getcwd()) + "/mtm-" + dtdir + '.log'

LASTS = 20  # lines to show by 'last' command

# categories and keywords
grocc = {
    "status":     "on off out away with at" .split(),
    "state":      "up down ill well" .split(),
    "busy":       "plan busy meet money conf work prog study trans" .split(),
    "home":       "home shop tax game life talk build child wash clean self doctor" .split(),
    "arts":       "art book lang bards concert museum cinema theater" .split(),
    "rest":       "eat tea coffee drink read write walk bed sleep" .split(),
    "exter":      "chat fun tv inet watch demo city" .split(),
    "active":     "travel sport ski byke run hike boat drive ride" .split(),
    "result":     "stat report" .split(),
    "info":       "? help query log last" .split()
}

cutup   = "busy active hime arts".split()
cutdown = "rest exter".split()

occs = []
for x in grocc.values():
    occs.extend(x)
occs.sort()

# how we print them when in text mode; others aren't printed or are shown in other way
todisplay = {"busy": "b", "home": "h", "arts": "a", "rest": "r", "exter": "x", "active": "v"}

def help():
    """ print list of options """
    loks = sorted(grocc.keys())
    for ok in loks:
        print (ok + ":", end="")
        tou = 0
        for ov in sorted(grocc[ok]):
            tou += 1
            if tou % 10 == 1:
                print ("\n\t", end="")
            print (ov + ", ", end="")
        print ()

def main(args):
    """ main routine """
    print ("This is MTM myke's Time Management routine ver. {}" .format (version))
    print ("Log goes to", fout)
    #~ print (dt, sys.argv, fout)

    if len(sys.argv) > 1 and sys.argv[1] in occs:

        if sys.argv[1] == "?":
            sys.argv[1] = "help"

        cmd = sys.argv[1]

        # print entire file
        if cmd == "log":
            with open (fout) as flog:
                txt = flog.read()
                print (txt)
            return

        # count stats from entire file
        if cmd == "stat":

            cm = collections.Counter()
            with open (fout) as flog:
                for line in flog:
                    dm = line[:10]
                    cm [dm] += 1

            if len(cm) == 0:
                return

            print ("data for last month")

            if "hor" in sys.argv:
                vmax = max(cm.values())
                #~ print ("max=", vmax)
                TOP = 20
                norma = 1. * TOP / vmax
                lok = sorted(list(cm))
                prep = lok[0][:8]
                #~ print ("norma=", norma, "prep=", prep, "lok=", lok)
                for h in range(TOP, 0, -1):
                    hlim = h * norma
                    #~ print (hlim)
                    for k in lok:
                        v = cm[k]
                        if v*norma/2. >= hlim:
                            print ("  *", end="")
                        else:
                            print ("   ", end="")
                    print()
                for s in lok:
                    print ("", s[-2:], end="")
                print ()
                for s in lok:
                    print ("%3d" % cm[s], end="")
                print ()

            else:
                for dm in sorted(cm):
                    print ("{0}: {1:3d}" .format (dm , cm[dm]))
            return

        # print last lines
        if cmd == "last":
            amt = LASTS
            try:
                if len(sys.argv) == 3:
                    amt = int(sys.argv[2])
            except:
                amt = 10
            with open (fout) as flog:
                txt = flog.readlines()
            print ("showing {} last lines" .format(amt))
            for lino in txt[-amt:]:
                print (lino, end="")
            return

        # perform log record
        print (dt, *sys.argv[1:])

        with open (fout, 'a') as mtm:
            print (dt, *sys.argv[1:], file=mtm)

    else:
        # default output w/o parameters
        print ("available commands are:")
        #~ pprint.pprint (grocc)
        help()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
