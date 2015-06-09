#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/ocr.html

import fileinput

class Counter(dict):
    def __missing__(self, key):
        return 0

counter = Counter()
f = open("2", "r")
for sym in f.read():
    counter[sym] += 1

for sym in counter.keys():
    print("%c -> %d" % (sym, counter[sym]))
