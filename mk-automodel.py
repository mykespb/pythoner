#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-automodel.py py3 2016-03-05 2016-03-08 0.3
# Ch.Wetherel modeling of autostrada

import random, time

TIMES = 20  # seconds to simulate

class Car():
    """ main car class """

    def __init__(self):
        self.pos = 0
        self.velo = 1.0
        self.state = 1
        # 0= out, 1=norm, -1=crash

    def show(self):
        """ show this car """
        return self.pos

class Way():
    """ the autoroute """

    MILES = 50

    def __init__(self, prob=0.1, leng=MILES):
        self.prob = prob
        self.leng = leng
        self.sec  = 0
        self.cars = []

    @property
    def miles (self):
        """ length of the way """
        return self.leng

    @property
    def line (self):
        """ length of queue of active cars """
        return len (self.cars)

    def show (self):
        """ show all cars on way """
        out = "-" * self.leng
        for car in self.cars:
            pos = int(car.pos)
            if pos:
                out = out[:pos] + "X" + out[pos:]
        print ("%5d %s" % (self.sec, out))

    def step (self):
        """ make iteration step of simulation """
        self.sec += 1
        self.movecars()
        self.gencars()
        self.show()

    def gencars (self):
        """ generate new car ramdomly """
        if random.random() < self.prob:
            self.cars += [Car()]
            #print ("!", end="")
        #else:
            #print (" ", end="")

    def movecars (self):
        """ move cars to next position """
        for car in self.cars:
            car.pos += car.velo
        exited = [car for car in self.cars if car.pos >= self.miles]
        for car in exited:
            del car
        self.cars = [car for car in self.cars if car.pos < self.miles]

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
