#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

N = 20
center = np.array([0.5, 0.5])


fig =  plt.figure()                


p = np.random.rand(N, 2)
#p = np.array([[5,5],[70,100],[160,180]])

ax = fig.add_subplot(111)
ax.grid(True, linestyle = '-', color = '0.75')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

colors = np.random.rand(N)
scat = plt.scatter(p[:, 0], p[:, 1], s = 100, c=colors)
scat.set_alpha(0.5)


def update_plot(i,fig, scat):
    global p
    for i in range(0, N):
        cmp = p[i] != center
        if cmp[0] or cmp[1]:
            ran = random.random()
            p[i] += ran*(center-p[i])

    scat.set_offsets(p)
    #print('Frames: %d' %i)
    print(p)
    return scat,

anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat),frames = 100, interval = 500)
              
plt.show()