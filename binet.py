#!/usr/bin/env python

# (C) Mikhail Kolodin, 2022
# 2022-01-18 2022-01-18 1.0

# ~ вычисление чисел фибоначчи по формуле Бине
# ~ https://habr.com/ru/post/645829/?fbclid=IwAR2F2OyE82KGlyTQpZA2Zw4kkkgRTX3olsO0ZS0-lVAPOnIMit83jweMhyk

import math

def binet(n):
    s5 = math.sqrt(5)
    return (((1 + s5) / 2) **n - ((1 - s5) / 2) **n ) / s5

def test1(k=30):
    for n in range(1, k+1):
        print(n, "->", binet(n))

test1()

# ~ 1 -> 1.0
# ~ 2 -> 1.0
# ~ 3 -> 2.0
# ~ 4 -> 3.0000000000000004
# ~ 5 -> 5.000000000000001
# ~ 6 -> 8.000000000000002
# ~ 7 -> 13.000000000000002
# ~ 8 -> 21.000000000000004
# ~ 9 -> 34.00000000000001
# ~ 10 -> 55.000000000000014
# ~ 11 -> 89.00000000000003
# ~ 12 -> 144.00000000000006
# ~ 13 -> 233.00000000000006
# ~ 14 -> 377.00000000000017
# ~ 15 -> 610.0000000000003
# ~ 16 -> 987.0000000000005
# ~ 17 -> 1597.000000000001
# ~ 18 -> 2584.000000000002
# ~ 19 -> 4181.000000000003
# ~ 20 -> 6765.000000000005
# ~ 21 -> 10946.000000000007
# ~ 22 -> 17711.00000000001
# ~ 23 -> 28657.000000000022
# ~ 24 -> 46368.00000000004
# ~ 25 -> 75025.00000000006
# ~ 26 -> 121393.00000000009
# ~ 27 -> 196418.00000000017
# ~ 28 -> 317811.0000000003
# ~ 29 -> 514229.00000000047
# ~ 30 -> 832040.0000000008