#! /usr/bin/env python3

# Mikhail Kolodin, 2021-08-04, 1.0

# revindex.py построение обратного индекса
# пусть дан обычный (прямой) индекс:
# список имён и страниц книги, где каждое имя встречается
# обычно это записывается в файле,
# но мы для примера возьмём просто список строк.
# нужно построить обратный список,
# т.е. указать, какие имена встречаются н акаждой странице.

text = """
Пушкин 5, 11, 128
Иванов 5, 12
Егоров 90
Васильев 11, 90, 125
Трушкин 7
Врушкин 7
"""

def lister(s):
    """ получение прямого и обратного словаря из текста
    """
    dd = {}
    rd = {}
    lines = s.split('\n')
    print(lines)
    for line in lines:
        # ~ print(line)
        if not line: continue
        arr = line.split(maxsplit=1)
        # ~ print(arr)
        if arr and len(arr) == 2:
            name, sol = arr
            lol = sol.split(sep=",")
            lol = [x.strip() for x in lol]
            # ~ print(lol)
            for el in lol:
                if el in rd:
                    rd[el] |= {name}
                else:
                    rd[el] = {name}
            for el in lol:
                if name in dd:
                    dd[name] |= {el}
                else:
                    dd[name] = {el}
    return dd, rd

def humani(d):
    """ печать обратного списка по-человечески
    """
    print("\nИндекс по именам")
    for p in sorted(d):
        print(p, end=" ")
        ds = d[p]
        ds = [int(x, 0) for x in ds]
        for n in sorted(ds):
            print(n, end=", ")
        print()

def humans(d):
    """ печать обратного списка по-человечески
    """
    print("\nИндекс по страницам")
    d = {int(x, 0): y for x, y in d.items()}
    for p in sorted(d):
        print(p, end=" ")
        for n in sorted(d[p]):
            print(n, end=", ")
        print()

# запуск - получили список
dd, rd = lister(text)
print(dd, rd)

# ... и распечатали прямо
humani(dd)
# ... и обратно
humans(rd)


# ~ ['', 'Пушкин 5, 11, 128', 'Иванов 5, 12', 'Егоров 90', 'Васильев 11, 90, 125', 'Трушкин 7', 'Врушкин 7', '']
# ~ {'Пушкин': {'128', '5', '11'}, 'Иванов': {'5', '12'}, 'Егоров': {'90'}, 'Васильев': {'90', '11', '125'}, 'Трушкин': {'7'}, 'Врушкин': {'7'}} {'5': {'Иванов', 'Пушкин'}, '11': {'Пушкин', 'Васильев'}, '128': {'Пушкин'}, '12': {'Иванов'}, '90': {'Васильев', 'Егоров'}, '125': {'Васильев'}, '7': {'Врушкин', 'Трушкин'}}

# ~ Индекс по именам
# ~ Васильев 11, 90, 125,
# ~ Врушкин 7,
# ~ Егоров 90,
# ~ Иванов 5, 12,
# ~ Пушкин 5, 11, 128,
# ~ Трушкин 7,

# ~ Индекс по страницам
# ~ 5 Иванов, Пушкин,
# ~ 7 Врушкин, Трушкин,
# ~ 11 Васильев, Пушкин,
# ~ 12 Иванов,
# ~ 90 Васильев, Егоров,
# ~ 125 Васильев,
# ~ 128 Пушкин,