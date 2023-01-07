#!/usr/bin/env/python

# ~ test module tabulate
# ~ from https://habr.com/ru/post/709282/
# ~ https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/tabulate.html
# ~ https://pypi.org/project/tabulate/
# ~ Mikhail (myke) Kolodin, 2023-01-07 1.2 2023-01-07

import random
import tabulate

print("test 1")

data = [
    ['id', 'name', 'number'],
    [0, 'Jeff', 1234],
    [1, 'Bob', 5678],
    [2, 'Bill', 9123]
]
results = tabulate.tabulate(data)
print(results)

print("test 2")

data = [
    [random.randint(-1_000_000, 1_000_000) for _ in range(10)],
    [random.randint(-1_000_000, 1_000_000) for _ in range(10)],
    [random.randint(-1_000_000, 1_000_000) for _ in range(10)],
    [random.randint(-1_000_000, 1_000_000) for _ in range(10)],
]
results = tabulate.tabulate(data)
print(results)

print("test 3")

voc = "t jtrek tjlerkt jlekrtj klrtj lerkjtl rkjt lekryjltkyjkltjyklrt yklrtjy lktjuykltrjylrtjylktrjykrtjykltr yktrj ylkrtjly jfgklh, gfh,gfmhn,fgnhhjtl khlkjtrlkyhjrt ykjtrklyjtrlkyjtlkyjltkjtyhlk ykrtly ltkrj ylktj ylkrtj ylkrtj ylktjy ltkrjyklrtjlyjtlkyjtrlyjtrlk yjlrtk ylktyjlrtkjy lkrtjylrtkjylrtkjy ltkrjylrtkyj klrtjy lktrjy lktrj yklrtjy kltjylkrtjylktjy lktjy kltrjy lktjylkrtyj ltkrj ykltrj ylktryklrtj yklkltry".split()

data = [
    [random.choice(voc) for _ in range(10)],
    [random.choice(voc) for _ in range(10)],
    [random.choice(voc) for _ in range(10)],
    [random.choice(voc) for _ in range(10)],
    [random.choice(voc) for _ in range(10)],
]
results = tabulate.tabulate(data)
print(results)

print("test 4")

data = [
    ['a' * random.randint(1, 20) + '\n' +
    'b' * random.randint(1, 20)  + '\n' +
    'c' * random.randint(1, 20) for _ in range(10)],
    ['d' * random.randint(1, 20) + '\n' +
    'e' * random.randint(1, 20)  + '\n' +
    'f' * random.randint(1, 20) for _ in range(10)],
    ['g' * random.randint(1, 20) + '\n' +
    'h' * random.randint(1, 20)  + '\n'
    for _ in range(10)],
]

results = tabulate.tabulate(data)
print(results)
