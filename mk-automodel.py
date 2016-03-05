#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-automodel.py py3 2016-03-05 2016-03-05 0.1
# Ch.Wetherel modeling of autostrada

import random, time

TIMES = 3  # seconds to simulate

class Car():
    """ main car class """

    def __init__(self):
        self.pos = 0
        self.velo = 1.0
        self.state = 1
        # 0= out, 1=norm, -1=crash

    def show(self):
        """ show this car """
        return self.pos, "X-+" [self.state -1]

class Way():
    """ the autoroute """

    MILES = 50

    def __init__(self, prob=0.1, leng=MILES):
        self.prob = prob
        self.leng = leng
        self.sec  = 0

    @property
    def miles(self):
        """ length of the way """
        return self.leng

    def show(self):
        """ show all cars on way """
        out = "-" * self.leng
        for car in cars:
            pos, state = car.show()
            out [pos] = state
        print ("%5d %s" % (self.sec, out))

    def step(self):
        """ make iteration step of simulation """
        self.sec += 1
        self.movecars()
        self.makecar()
        self.delcars()

    def movecars(self):
        """ move cars to next position """
        for car in cars:
            car.pos += car.velo

    def makecar(self):
        """ make new car and put it on the way"""
        global cars
        if random.random() > self.prob:
            cars += [Car()]

    def delcars(self):
        """ delete cars that went off the way"""
        for car in cars:
            if car.pos >= self.leng:
                car.state=0

cars = []   # all cars

def main(args):
    print ("start simulation\n\n")
    way = Way()
    way.show()

    for atime in range(TIMES):
        way.step()
        time.sleep(1)

    print ("\n\nend simulation\n\n")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
