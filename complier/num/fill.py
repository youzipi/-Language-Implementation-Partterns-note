# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
import numpy as np

cut = int(np.random.rand(1)[0] * 10)
cut1 = int(np.random.rand(1)[0] * 10)
low = min(cut, cut1)
high = max(cut, cut1)
ran = np.random.permutation(range(10))


a = np.array([2,5,9,7,3,1,4,8,6,0])

b = np.hstack((np.linspace(-1, -1, 10)[:low],a[low:high], np.linspace(-1, -1, 10)[high:]))
print "high", high
print "low", low
print b
f = 0
print "ran", ran
for t in ran:
    if t not in b:
        if f < low:
            b[f] = t
            f += 1
        elif f >= low and f < high:
            f = high
            b[f] = t
            f += 1
        else:
            break

print b