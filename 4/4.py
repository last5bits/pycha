#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request as req
import re

#num = 12345
num = 8022
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
while True:
    content = req.urlopen(url + '%d' % num).readall()
    print(content)

    match = re.search('next nothing is ([0-9]+)', '%s' % content)
    if match != None:
        num = int(match.group(1))
    else:
        print('Emergency!')
        break
