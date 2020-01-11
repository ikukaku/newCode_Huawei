# -*- coding: utf-8 -*-

N = int(raw_input())
input_raw = {}
for i in xrange(N):
    x = raw_input()
    _a = int(x.split(' ')[0])
    _b = int(x.split(' ')[-1])
    if input_raw.has_key(_a):
        input_raw[_a] = input_raw[_a]+_b
    else:
        input_raw.setdefault(_a, _b)
for i in sorted(input_raw.keys()):
    print str(i)+' '+str(input_raw[i])
