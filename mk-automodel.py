#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mk-automodel.py py3 2016-03-05 2016-03-05 0.1
# Ch.Wetherel modeling of autostrada

class Car():
    """ main car class """

    def __init__():
        self.pos = 0
        self.velo = 0
        self.state = 1
        # 0= out, 1=norm, -1=crash

    def show(self):
        """ show this car """
        return self.pos, "X-+" [self.state -1]

class Way():
    """ the autoroute """

    MILES = 50

    @property
    def miles(self):
        """ length of the way """
        return self.MILES

    def show(self):
        """ show all cars on way """
        out = "-" * self.miles
        for car in cars:
            pos, state = car.show()
            out [pos] = state
        print (out)

cars = []   # all cars

def main(args):
    way = Way()
    way.show()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
