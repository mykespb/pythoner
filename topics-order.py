#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-28 2024-12-28 0.6
# topics-order.py

# ~ Дан набор тем, причём указано, какие темы зависят от каких и должны изучаться после них.
# ~ Составить план обучения (порядок изучения тем).
# ~ Если это невозможно, явно сказать об этом, лучше - указав причину.
# ~ Рабочий пример дан ниже.

# -------------------------------
# initial data
# -------------------------------

topics1 = """
start finish
process finish
start process
"""

topics2 = """
intro conditions loops functions exceptions
intro types constants variables operators
intro operators conditions
generators iterators
exceptions with files
files networks
loops generators
generators networks conclusion
"""

topics = topics1

# ~ print(id(topics), id(topics1), id(topics2))

# -------------------------------
# imports
# -------------------------------

from pprint import pp

# -------------------------------
# setup
# -------------------------------

DEBUG = True

# -------------------------------
# functions
# -------------------------------

def ppp(*what):
    """условная притти-печать (кортеж!)
    """

    if DEBUG: pp(what)
    

def prepare():
    """предварительно подготовить данные,
    собрав всё в нормальные списки
    """

    global data
    data = []
    
    for line in topics.strip().lower().split("\n"):
        data.append(line.strip().split())

    ppp("source data", data)


def process():
    """обработка
    """

    global para
    para = []

    for line in data:
        for first in range(len(line) - 1):
            for second in range(first+1, len(line)):
                para.append((line[first], line[second]))

    ppp("preprocessed data", para, prelen := len(para))

    para = list(set(para))
    
    ppp("postrocessed data", list(enumerate(para)), postlen := len(para),
        "shortened" if prelen > postlen else "not changed"
        )

    ...


def output():
    """красивая печать результата
    """
    ...


def main():
    """запуск
    """

    prepare()
    process()
    output()


main()


# -------------------------------
# output
# -------------------------------

# ~ topics1

# ~ [['start', 'finish'], ['process', 'finish'], ['start', 'process']]
# ~ [('start', 'finish'), ('process', 'finish'), ('start', 'process')]

# ~ topics2

# ~ [['intro', 'conditions', 'loops', 'functions', 'exceptions'],
 # ~ ['intro', 'types', 'constants', 'variables', 'operators'],
 # ~ ['intro', 'operators', 'conditions'],
 # ~ ['generators', 'iterators'],
 # ~ ['exceptions', 'with', 'files'],
 # ~ ['files', 'networks'],
 # ~ ['loops', 'generators'],
 # ~ ['generators', 'networks', 'conclusion']]
# ~ [('intro', 'conditions'),
 # ~ ('intro', 'loops'),
 # ~ ('intro', 'functions'),
 # ~ ('intro', 'exceptions'),
 # ~ ('conditions', 'loops'),
 # ~ ('conditions', 'functions'),
 # ~ ('conditions', 'exceptions'),
 # ~ ('loops', 'functions'),
 # ~ ('loops', 'exceptions'),
 # ~ ('functions', 'exceptions'),
 # ~ ('intro', 'types'),
 # ~ ('intro', 'constants'),
 # ~ ('intro', 'variables'),
 # ~ ('intro', 'operators'),
 # ~ ('types', 'constants'),
 # ~ ('types', 'variables'),
 # ~ ('types', 'operators'),
 # ~ ('constants', 'variables'),
 # ~ ('constants', 'operators'),
 # ~ ('variables', 'operators'),
 # ~ ('intro', 'operators'),
 # ~ ('intro', 'conditions'),
 # ~ ('operators', 'conditions'),
 # ~ ('generators', 'iterators'),
 # ~ ('exceptions', 'with'),
 # ~ ('exceptions', 'files'),
 # ~ ('with', 'files'),
 # ~ ('files', 'networks'),
 # ~ ('loops', 'generators'),
 # ~ ('generators', 'networks'),
 # ~ ('generators', 'conclusion'),
 # ~ ('networks', 'conclusion')]
