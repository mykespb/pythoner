#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myke ludoj/mk-kalah.py 2015-10-13 1.0
# kalah playing
# ver. 1. random move select
# simple move rules, single w/o additions

import sys, random

STONES = 3
HOLES = 6
KALAH = HOLES
ALLSTONES = 2 * HOLES * STONES
HALFSTONES = ALLSTONES // 2

cntgames = cntwins = 0
winner = 0

b = []

class AllBad (Exception): pass

def main (args):
    """main dispatcher and input processor"""
    global cntgames, cntwins
    print ("\nHello, this is Kalah.\n")

    while True:
        que = input("\nWanna play? (yY12?q)[q]: ")
        if que == "?":
            help()
            continue
        if que not in "yY12": break
        print ("OK, playing...")
#        print ("HALFSTONES= %d" % (HALFSTONES, ))
        init_board ()
        cntwins += play (que)
        cntgames += 1

    report ()
    return 0

def help ():
    """helper"""
    print ("""
type     to
-------- ----------------------------------------
1        play 1st player
2        play 2nd player
y or Y   play any player at random
?        this help
q        quit
""")

def init_board ():
    """init the board"""
    global b
    b = [[STONES for i in range(HOLES)], [STONES for i in range(HOLES)]]
    b[0].append(0)
    b[1].append(0)

def play (que):
    """determine order and play 1 game"""
    global b, winner
    if que not in "12".split():
        que = random.choice("12")
    print ("\nPlaying as %s\n" % que)
    show (b)
    print ("\n")

    que = int(que)-1
    while moveposs (b, que):
        if que:
            move (b, 1, makemove(b))
        else:
            m = getmove()
            if m:
                move (b, 0, m-1)
            else:
                averio ()
                break
        que = 1 - que
        show (b)

    theend()
    return winner

def averio ():
    """cancel user's game """
    global b
    for i in range(HOLES):
        b[1][KALAH] += b[0][i]
        b[0][i] = 0

def move (b, who, hole):
    """make move from row 0/1 and hole on board b"""
    if hole < 0:
        raise AllBad("Bad move -move-")
    todo = b[who][hole]
    b[who][hole] = 0
    to = hole + 1
    side = who
    while todo:
        if side == who:
            if to <= HOLES:
                todo -= 1
                b[side][to] += 1
                to += 1
            else:
                side = 1 - side
                to = 0
        else:
            if to < HOLES:
                todo -= 1
                b[side][to] += 1
                to += 1
            else:
                side = 1 - side
                to = 0

def moveposs (b, who):
    """see if move possible on board b for player who"""
    s = sum(b[who][:KALAH])
#    print ("moveposs = who=%d, s=%d, K0=%d, K1=%d" % (who, s, b[0][KALAH], b[1][KALAH]))
    return s > 0 and b[0][KALAH] <= HALFSTONES and b[1][KALAH] <= HALFSTONES

def getmove ():
    """user moves"""
    while True:
        m = input ("\nEnter yor move or q: ")
        print ()
        m = m.strip()
        if m == 'q':
            return 0
        if len(m) == 0:
            n = 0
        elif m in "123456":
            n = int(m)
        else:
            n = 0
        print ("Got move:", n, "\n")
        if n == 0:
            print ("\nBad move: no such cell 0! Please repeat!\n")
            show (b)
            continue
        if 1 <= n <= HOLES and b[0][n-1] == 0:
            print ("\nBad move: hole is empty! Please repeat!\n")
            show (b)
            continue
        if n < 0 or n > HOLES:
            return 0
        return n

def makemove1st (b):
    """computer moves: 1st possible move"""
    for i in range(HOLES):
        if b[1][i]:
            print ("\nComputer moves: %d\n" % (i+1,))
            return i
    raise AllBad("Bad move -makemove-")

def makemoverand (b):
    """computer moves: 1st possible move"""
    ms = [k for k in enumerate(b[1][:KALAH]) if k[1]]
    #print ("ms=", ms)
    mo = random.choice (ms)
    #print ("mo=", mo)
    i = mo[0]
    #print ("i=", i)

    print ("\nComputer moves: %d\n" % (i+1,))
    return i
    raise AllBad("Bad move -makemove-")

def makemove (b):
    """computer moves"""
#    return makemove1st (b)
    return makemoverand (b)

def theend ():
    """process end of game, calculate stones"""
    global winner
    for i in range(HOLES):
        b[0][KALAH] += b[0][i]
        b[0][i] = 0
        b[1][KALAH] += b[1][i]
        b[1][i] = 0
    if b[0][KALAH] > b[1][KALAH]:
        winner = 1
        print ("\nPlayer won!\n")
    elif b[0][KALAH] < b[1][KALAH]:
        winner = -1
        print ("\nComputer won!\n")
    else:
        winner = 0
        print ("\nWe have a draw!\n")
    show (b)

def report ():
    """ show report about session """
    global b
    print ("\n\nPlayed games: %d, your result: %d\n\n" % (cntgames, cntwins))

def show (b):
    """show board"""
    print ("%4d%4d%4d%4d%4d%4d%4d\n--------------------------------\n    %4d%4d%4d%4d%4d%4d%4d" % (*(b[1][::-1]), *(b[0])))
#    print ("%4d%4d%4d%4d%4d%4d%4d\n    %4d%4d%4d%4d%4d%4d%4d" % (*(b[1][::-1]), *(b[0])))
#    print (*(b[1][8:0:-1]), *(b[0]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
