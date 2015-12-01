#!/usr/bin/python2
# myke pil-primes1.py 2010-09-14 2010-09-15 1.1
# draw prime numbers to bmp file

from PIL import Image
import math

limit = 500000
debug = 1
limitsqrt = int(math.sqrt(limit)) +1
limshalf = limitsqrt // 2
pset = [2, 3, 5, 7, 11]

def primes():
    global pset
    print "\ncount: ",
    for tested in xrange (13, limit+1):
        if debug and tested % limitsqrt == 0 : 
            print tested,
        for tester in pset:
            if tested % tester == 0:
                break
        else:
            pset.append(tested)

def show():
    global im
    print "\nshow: ",
    x = y = limshalf
    inum = 0
    bar = 1
    doit = True
    while doit:
        for i in xrange(bar):
            inum += 1
            if debug and inum % limitsqrt == 0 : 
                print inum,
            if inum >= limit:
                doit = False
                break
            x += 1
            if inum in pset:
                if x<limitsqrt and y<limitsqrt:
                    im.putpixel ((x, y), 1)
        for i in xrange(bar):
            inum += 1
            if debug and inum % limitsqrt == 0 : 
                print inum,
            if inum >= limit:
                doit = False
                break
            y += 1
            if inum in pset:
                if x<limitsqrt and y<limitsqrt:
                    im.putpixel ((x, y), 1)
        bar += 1
        for i in xrange(bar):
            inum += 1
            if debug and inum % limitsqrt == 0 : 
                print inum,
            if inum >= limit:
                doit = False
                break
            x -= 1
            if inum in pset:
                if x<limitsqrt and y<limitsqrt:
                    im.putpixel ((x, y), 1)
        for i in xrange(bar):
            inum += 1
            if debug and inum % limitsqrt == 0 : 
                print inum,
            if inum >= limit:
                doit = False
                break
            y -= 1
            if inum in pset:
                if x<limitsqrt and y<limitsqrt:
                    im.putpixel ((x, y), 1)
        bar += 1
        

def main():
    global im
    im = Image.new('1', (limitsqrt, limitsqrt))
    primes()
    show()
    im.save ("primes.bmp")

main()
