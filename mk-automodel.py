#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-automodel.py py3 2016-03-05 2016-03-10 0.5
# Ch.Wetherel modeling of autostrada

import random, time

TIMES = 50      # seconds to simulate
PAUSE = 0.01     # viewer speed

class Car():
    """ main car class """

    def __init__(self):
        self.pos = 0
        self.velo = 1.0

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
        self.dist = 1

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
            out = out[:pos] + "+" + out[pos+1:]
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
            self.cars = [Car()] + self.cars

    def movecars (self):
        """ move cars to next position """
        for carnum in range(self.line):
            car      = self.cars [carnum]
            delta    = 0.8 + 0.4 * random.random()
            car.velo *= delta
            if carnum < self.line-1:
                distance = self.cars [carnum+1] .pos - car.pos
                #print ("dist=%f" % distance)
                if distance < 0.01:         # crash!
                    car.velo *= 0.2
                    self.cars [carnum+1] .velo *= 0.2
                elif distance < self.dist:   # slow down!
                    car.velo *= 0.5
                    self.cars [carnum+1] .velo *= 1.5
            car.pos  += car.velo
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
        time.sleep(PAUSE)

    print ("\n\nend simulation\n\n")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
