# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()


N = 50
T = 0
#x,y轴坐标 面积大小在0到15
#x = np.random.rand(N)
#y = np.random.rand(N)
p = np.random.rand(N, 2)

ax = fig.add_subplot(111)
ax.grid(True, linestyle = '-', color = '0.75')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])


colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
area = np.linspace(100, 100, N)
center = np.array([0.5, 0.5])
marker = (3, 1)
#plt.show()
#, c=colors
#points = plt.scatter(p[:, 0], p[:, 1], s=100, marker=marker, alpha=0.5)
points = plt.scatter(p[:, 0], p[:, 1])

def init():
    pass
    #plt.scatter(p[:, 0], p[:, 1], s=area, c=colors, marker=marker, alpha=0.5)
    # return plt.scatter(x, y, s=area, c=colors, alpha=0.5)
def update(points):
    global p
    offsets = np.linspace(0, 0, 2*N).reshape(-1, 2)
    for i in range(0, N):
        cmp = p[i] != center
        if cmp[0] or cmp[1]:
            ran = random.random()
            p[i] += ran*(enter-p[i])

    points.set_offsets(p)
    #points.set_color(1)
    return points,

ani = animation.FuncAnimation(fig, update, fargs = (points),init_func=init, interval=2000)
#, init_func=init
plt.show()