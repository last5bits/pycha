#!/usr/bin/env python

#crypted="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
crypted="map"

decrypted=""
for sym in crypted:
    desym=sym
    if str.isalpha(sym):
        desym = chr(ord('a') + (ord(desym) - ord('a') + 2) % 26)
    decrypted += desym

print(decrypted)

