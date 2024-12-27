#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-28 2024-12-28 0.1
# topics-order.py

# ~ Дан набор тем, причём указано, какие темы зависят от каких и должны изучаться после них.
# ~ Составить план обучения (порядок изучения тем).
# ~ Если это невозможно, явно сказать об этом, лучше - указав причину.
# ~ Рабочий пример дан ниже.

topics = """
intro conditions loops functions exceptions
intro types constants variables operators
intro operators conditions
generators iterators
exceptions with files
files networks
loops generators
generators networks conclusion
"""

from pprint import pp

DEBUG = True


def ppp(*what):
    """условная притти-печать
    """

    if DEBUG: pp(*what)
    

def prepare():
    """предварительно подготовить данные,
    собрав всё в нормальные списки
    """

    global data

    data = []
    for line in topics.strip().lower().split("\n"):
        data.append(line.split())

    ppp(data)


def process():
    """обработка
    """
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

