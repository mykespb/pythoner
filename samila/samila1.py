#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-01 2022-02-01 1.1
# samila1.py
# ~ https://habr.com/ru/post/648955/
# ~ Python и Samila. Делаем красиво
# ~ Python * Обработка изображений *

import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage, Projection

def t01():
    g = GenerativeImage()
    g.generate()
    g.plot()
    plt.show()

def t02():
    g = GenerativeImage()
    g.generate()
    g.plot()
    g.save_image(file_adr="test.png")

def t03():
    for i in range(10):
        g = GenerativeImage()
        g.generate()
        g.plot()
        img_name = str(i+1) + "_test.png"
        g.save_image(file_adr=img_name)

def f11(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result

def f12(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def t04():
    g = GenerativeImage(f11, f12)
    g.generate()
    g.plot()
    plt.show()

def f21(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result


def f22(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def t05():
    g = GenerativeImage(f21, f22)
    g.generate()
    g.plot(projection=Projection.POLAR)
    plt.show()

def f31(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result

def f32(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def test05():
    g = GenerativeImage(f31, f32)
    g.generate(start=-2*math.pi, step=0.01, stop=0)
    g.plot()
    plt.show()

t05()
