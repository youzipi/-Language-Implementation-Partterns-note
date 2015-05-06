#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from line_demo import MyLine

N = 20
center = np.array([0.5, 0.5])
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, xlim=(0, 55), ylim=(0, 100))
ax1 = fig.add_subplot(1, 2, 2, xlim=(-2, 12), ylim=(-2, 12))
ax.grid(True, linestyle='-', color='0.75')
# ax.set_xlim([0, 55])
#ax.set_ylim([0, 100])
point_view, = ax1.plot([], [], lw=2)
line, = ax1.plot([], [], lw=2)
text = ax1.text(-1.5, 11, '')
times_text = ax1.text(-1.5, 11.5, '')
len_text = ax1.text(-1.5, 10.5, '')
a = np.random.rand(5)
t = (a, a, a, a, a, a, a, a, a, a)
colors = np.vstack(t).reshape(1, -1)

POINTS_NUM = 10
ROUTES_NUM = 50
routetype = np.dtype({
    'names': ['points', 'length'],
    'formats': ['O', 'f']})
routes = np.zeros([ROUTES_NUM], dtype=routetype)
points = np.random.rand(POINTS_NUM, 2) * 10
print "points=", points


def cal_length(route):
    length = 0
    for i in range(POINTS_NUM):
        p1 = points[route[i]]
        p2 = points[route[(i + 1) % POINTS_NUM]]
        length += np.linalg.norm(p1 - p2)
    return length


for index in range(ROUTES_NUM):
    temp = np.random.permutation(range(POINTS_NUM))
    length = cal_length(temp)
    routes[index] = (temp, length)

print "after sort"
routes.sort(order='length')
print routes
frogs = np.zeros([5, 10], dtype=routetype)

for i in range(5):
    t = 0
    for j in range(ROUTES_NUM):
        if j % 5 == i:
            frogs[i][j / 5]['points'] = routes[j]['points']
            frogs[i][j / 5]['length'] = routes[j]['length']
            # frogs[i][j/5] = routes[j].copy()

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

scat = ax.scatter(np.linspace(1, 50, 50), p, s=60, c=colors)
scat.set_alpha(0.5)


def upgrade(routee,route_best):
    cut = int(np.random.rand(1)[0] * 10)
    cut1 = int(np.random.rand(1)[0] * 10)
    low = min(cut, cut1)
    high = max(cut, cut1)

    ran = np.random.permutation(range(POINTS_NUM))
    empty = np.linspace(-1, -1, 10)

    routee = np.hstack((empty[:low], route_best[low:high], empty[high:]))
    print "routee",routee
    f = 0
    for t in ran:
        if t not in routee:
            if f < low:
                routee[f] = t
                f += 1
            elif low <= f < high:
                f = high
                routee[f] = t
                f += 1
            elif high <= f < POINTS_NUM:
                routee[f] = t
                f += 1
            else:
                break

    return routee


def update_frogs():
    global r_w, r_b, r_g, routes, frogs
    for i in range(5):
        for j in range(5):
            print 'r_w[{0}]'.format(i), r_w[i]
            print 'r_b[{0}]'.format(i), r_b[i]
            temp_len = r_w[i]['length']

            r_w[i]['points'] = upgrade(r_w[i]['points'],r_b[i]['points'])
            l = cal_length(r_w[i]['points'])
            if l < temp_len:
                print "update to ", l
                r_w[i]['length'] = l
            else:
                 #print type(r_w[i])
                 #print type(r_g)
                 #r_w[group_id] = r_g
                 r_w[i]['points'] = r_g['points']
                 r_w[i]['length'] = r_g['length']
            #r_w[i]['length'] = len
            #if len < temp_len:
             #   r_b[i] = r_g
            try:
                #pass
                frogs[i].sort(order=('length'))
            except ValueError as e:
                print "ValueError({0})".format(e)
            #r_w[i]['points'] = frogs[i, 9]['points']
            #r_w[i]['length'] = frogs[i, 9]['length']
            #r_b[i]['points'] = frogs[i, 0]['points']
            #r_b[i]['length'] = frogs[i, 0]['length']
            print "after"
            print 'r_w[{0}]'.format(i), r_w[i]
            print 'r_b[{0}]'.format(i), r_b[i]
            print "frogs[{0}]".format(i), frogs[i]
    routes = frogs.reshape(1, -1)
    try:
        routes.sort(order='length')
    except ValueError as e:
        print "ValueError({0})".format(e)
    print "routes",routes
    r_g = routes[0][0]
    print "r_g",r_g


def update_plot(i):

    global line, point_view, scat, routes,points
    #if i >= 50:
    print "r_g['points']",r_g['points']
    order = r_g['points'].astype(np.int32)
    p = points[order]
    text.set_text('i = r_g' )
    times_text.set_text('times = %d' % i )
    len_text.set_text('len = %.3f' % r_g['length'])
    print "r_g.length=",r_g['length']
    update_frogs()
    #else:
    #    print "i",i
    #    text.set_text('i = %d' % i)
    #    len_text.set_text('len = %.3f' % routes[i]['length'])
    #    p = points[routes[i]['points']]
    #    print routes[i]['length']
    line.set_data(p[:, 0], p[:, 1])
    #point_view.set_offsets(p)
    #scat.set_offsets(np.array(np.linspace(0, 0, 50), routes['length']))
    scat = ax.scatter(np.linspace(1, 50, 50), routes['length'], s=60, c=colors)
    scat.set_alpha(0.2)
    return line, point_view, scat


def init():
    global line, point_view, scat
    #line.set_data(points[:, 0], points[:, 1])
    point_view = ax1.scatter(points[:, 0], points[:, 1], s=60, c='red')
    return line, point_view, scat


# anim = animation.FuncAnimation(fig, update_plot, init_func=init,fargs = (fig, scat),frames = 100, interval = 500)
anim = animation.FuncAnimation(fig, update_plot, init_func=init, frames=100, interval=500)

plt.show()

#update_frogs()