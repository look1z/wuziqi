# -*- coding:utf-8 -*-
# by look1z
import hashlib
a = 'RgYDMllaKzGC'
bbb = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ccc = []
for i in range(52):
    ccc.append(i)

mydict = dict(zip(bbb, ccc))
mydict2 = dict(zip(ccc, bbb))
b = []
c = []
d = []
for i in a:
    b.append(i)

for j in range(12):
    # t = ord(b[j])-ord('a')

    t = (21*mydict[b[j]]+8)%52
    t = mydict2[t]
    c.append(t)
print (c)

pwd = 'BEsTAFFiKney'
checkcode = hashlib.md5(pwd).hexdigest()
print (checkcode)
