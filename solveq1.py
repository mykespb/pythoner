#!/usr/bin/env python

# (C) Mikhail Kolodin, 2022
# 2022-01-15 2022-01-15 1.1

# ~ численное решение системы 2 произвольных уравнений

def fun1(x):
    return x**2

def fun2(x):
    return x**3

def solve(x1, x2, eps):
    x = x1
    step = (x2 - x1) / 100
    while x <= x2:
        if abs(fun1(x) - fun2(x)) <= eps:
            print("solution:", x)
        x += step

solve(-10, 10, 1e-3)

# ~ solution: -2.0539125955565396e-15
# ~ solution: 0.999999999999998
