#!python3.10

# tests with python3.10 - OK
# (C) Mikhail (myke) Kolodin, 2021
# 2021-10-05 2021-10-05 1.0

import sys
print (sys.version)

import uuid

from pprint import pprint as pp

from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

pp (list(Color))

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return uuid.uuid4().hex

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

pp (list(Ordinal))

# ~ 3.10.0 (default, Oct  5 2021, 12:37:28) [GCC 9.3.0]
# ~ [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
# ~ [<Ordinal.NORTH: 'de3dcf4d80e34c589141c9994a2179f5'>,
 # ~ <Ordinal.SOUTH: 'c0a8c7fb0812461f8997cb62e323c2d8'>,
 # ~ <Ordinal.EAST: '3f3495b309924070ba1845ce99fb17b4'>,
 # ~ <Ordinal.WEST: '42288dbbeb0c4754af0295107c264eab'>]

import statistics

year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]
slope, intercept = statistics.linear_regression(year, films_total)

print (f"{slope=}, {intercept=}, calc={round(slope * 2019 + intercept)}")

vals = [1, 2, 3, 4, 4]
print (vals, "mean1=", statistics.mean(vals))

vals = [-1.0, 2.5, 3.25, 5.75]
print (vals, "mean2=", statistics.mean(vals))

vals = [1, 2, 3, 4, 4]
print (vals, "fmean1=", statistics.fmean(vals))

vals = [-1.0, 2.5, 3.25, 5.75]
print (vals, "fmean2=", statistics.fmean(vals))

vals = [1, 3, 5]
print (vals, "median=", statistics.median(vals))

vals = [1, 3, 5, 7]
print (vals, "median=", statistics.median(vals))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print (f"for correlation: {x=}, {y=}")

print (statistics.correlation(x, x))
print (statistics.correlation(x, y))
