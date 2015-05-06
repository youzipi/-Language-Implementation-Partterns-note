# -*- coding: utf-8 -*-
# __author__ = 'youzipi'
import numpy as np

def cal_length(route):
    length = 0
    for i in range(POINTS_NUM):
        p1 = points[route[i]]
        p2 = points[route[(i + 1) % POINTS_NUM]]
        length += np.linalg.norm(p1 - p2)
    return length

POINTS_NUM = 10
ROUTES_NUM = 50
routetype = np.dtype({
    'names': ['points', 'length'],
    'formats': ['O', 'f']})
routes = np.zeros([(ROUTES_NUM)], dtype=routetype)
points = np.random.rand(POINTS_NUM, 2) * 10
print "points=", points

for index in range(ROUTES_NUM):
    temp = np.random.permutation(range(POINTS_NUM))
    length = cal_length(temp)
    routes[index] = (temp, length)


print "after sort"
routes.sort(order=('length'))
print routes
frogs = np.zeros([5, 10], dtype=routetype)

for i in range(5):
    t = 0
    for j in range(ROUTES_NUM):
        if j%5 == i:
            frogs[i][j/5]['points'] = routes[j]['points']
            frogs[i][j/5]['length'] = routes[j]['length']

for i in range(5):
    print "frogs", i
    print frogs[i]
p = routes['length']
print p
r_g = routes[0]
print "r_g", r_g
r_b = frogs[:, 0]
print "r_b", r_b
r_w = frogs[:, 9]
print "r_w", r_w


#def update_frogs():
#global r_w, r_b, r_b
for i in range(5):
    for j in range(5):
        cut = int(np.random.rand(1)[0] * 10)
        ran = np.random.permutation(range(POINTS_NUM))
        print 'r_w', r_w[i]
        print 'r_b', r_b[i]
        temp_len = r_w[i]['length']
        r_w[i]['points'] = np.hstack((r_b[i]['points'][:cut], np.linspace(-1, -1, 10)[cut:]))
        for t in ran:
            if t not in r_w[i]['points']:
                r_w[i]['points'][cut] = t
                cut = cut + 1
            if cut >= POINTS_NUM:
                break
        len = cal_length(r_w[i]['points'])
        if len < temp_len:
            r_w[i]['length'] = len
        else:
            r_b[i]['points'] = r_g['points']
            r_b[i]['length'] = r_g['length']
            i -= 1
            continue
        print frogs[i]
        frogs[i].sort(order='length')

        r_w[i]['points'] = frogs[i, 9]['points']
        r_w[i]['length'] = frogs[i, 9]['length']
        print "after"
        print 'f_w', r_w[i]
        print 'f_b', r_b[i]
