#!/usr/bin/env python

import pickle

with open("banner.p", "rb") as f:
    data = pickle.load(f)
    for val in data:
        print(val)
        print()
