#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/equality.html

import re

f = open("3", "r")

for s in re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", f.read()):
    print(s, end='')

print()
