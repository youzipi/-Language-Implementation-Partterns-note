# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
"""
Show how to override basic methods so an artist can contain another
artist.  In this case, the line contains a Text instance to label it.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms

class MyLine(lines.Line2D):

   def __init__(self, *args, **kwargs):
      # we'll update the position when the line data is set
      lines.Line2D.__init__(self, *args, **kwargs)

   def set_figure(self, figure):
      lines.Line2D.set_figure(self, figure)

   def set_axes(self, axes):
      lines.Line2D.set_axes(self, axes)

   def set_transform(self, transform):
      # 2 pixel offset
      texttrans = transform + mtransforms.Affine2D().translate(2, 2)
      lines.Line2D.set_transform(self, transform)


   def set_data(self, x, y):
      lines.Line2D.set_data(self, x, y)

   def draw(self, renderer):
      # draw my label at the end of the line with 2 pixel offset
      lines.Line2D.draw(self, renderer)



#x, y = np.random.rand(2, 20)
#print x,y
#line = MyLine(x, y)
points = np.random.rand(10, 2)
print points

scat = plt.scatter(points[:,0], points[:,1], s=60, c='red')
line = MyLine(points[:,0], points[:,1])


fig, ax = plt.subplots()

ax.add_line(line)


plt.show()