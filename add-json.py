# python, Mikhail Kolodin
# add-json.py 2022-06-20 2022-06-20 1.2
# add-json.py j1.json j2.json j3.json
# means: add j2.json to j1.json giving j3.json

import json, sys

if len(sys.argv) < 4:
    print("not enough arguments:")
    exit(1)

file1n, file2n, file3n = sys.argv[1:4]

with open(file1n, 'r') as file1, \
    open(file2n, 'r') as file2, \
    open(file3n, 'w') as file3:

    j1 = json.load(file1)
    print(f"{j1=}")
    j2 = json.load(file2)
    print(f"{j2=}")

    j1 = dict(j1)
    j2 = dict(j2)
    j1.update(j2)
    print(f"{j1=}")

    json.dump(j1, file3, indent=2)
