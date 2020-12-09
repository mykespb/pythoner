#!/usr/bin/env python3

# генератор uuid'ов (uuid4) in hex form
# Mikhail (myke) Kolodin, 2020
# 2020-12-09 0.1

import uuid

for i in range(100):
    print(uuid.uuid4().hex)

