#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-3rd-smallest.py 2023-07-23 2023-07-23 1.0
# find n-th smallest value in given list

from random import randint

def solve(array: list[int], nth: int) -> int:
    """find number"""

    sarray = set(array)

    if len(sarray) < nth:
        return 0
    
    return sorted(sarray)[nth-1]


def test(array: list[int], nth: int) -> None:
    """prinr it and run test"""

    print(f"{array=}, {nth=} => {solve(array, nth)}")

test([], 1)
test([1], 1)
test([1, 2, 3], 2)
test([1, 2, 3, 4, 2, 88, 239], 3)
test([randint(1, 99) for _ in range(10)], 3)
test([randint(1, 99) for _ in range(10)], 3)
test([randint(1, 99) for _ in range(10)], 3)
test([randint(1, 99) for _ in range(10)], 3)
test([randint(1, 99) for _ in range(10)], 3)
test([randint(1, 99) for _ in range(10)], 3)

# array=[], nth=1 => 0
# array=[1], nth=1 => 1
# array=[1, 2, 3], nth=2 => 2
# array=[1, 2, 3, 4, 2, 88, 239], nth=3 => 3
# array=[33, 25, 46, 87, 42, 1, 67, 13, 3, 5], nth=3 => 5
# array=[18, 93, 79, 95, 70, 85, 90, 29, 85, 7], nth=3 => 29
# array=[42, 28, 96, 52, 3, 71, 42, 51, 95, 46], nth=3 => 42
# array=[79, 46, 35, 31, 18, 17, 68, 84, 6, 26], nth=3 => 18
# array=[39, 64, 59, 8, 12, 28, 98, 69, 56, 68], nth=3 => 28
# array=[89, 92, 26, 23, 79, 99, 36, 99, 18, 84], nth=3 => 26

# remarks:
# all given numbers should be positive, 
# result = 0 means that array is too short to get nth smallest value
