# https://www.instagram.com/p/CNpivLFjxUj/


#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
size = 900
ctx._setup(size, size)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-1, 1)
ctx.set_line_width(2)

from geom.grid import Grid
cols = 12
grid = Grid(-1, -1, 2, 2, rows=40, cols=cols, padding=0, offset=0.5)
# grid = Grid(-1, -1, 2, 2, rows=int(size/2), cols=int(size/2), padding=0, offset=0.0)

ctx.set_color([1, 0, 1, 1])
# grid.draw(ctx, px=4)

from geom.circle import Circle
from numpy import pi
from numpy.random import random

from lib.field import Perlin2DField
from scipy.spatial import distance
from math import sqrt

field = Perlin2DField((128, 128), (32, 32), seed=21)
fn = field.fn(((-1, 1), (-1, 1)))

# ctx.set_color([1, 1, 1, 1])
for pt in grid.centers():
    x, y = pt
    # sample perlin field
    n = fn(x, y) * 0.5 + 0.5
    # shape perlin field to be less likely at extents
    d = distance.euclidean((x, y), (0, 0))
    z = n * 1.4 - d
    # shape
    # z = n * 2 - sqrt(d) 
    # z = sqrt(d)
    # z = (1 - d ** 1.8)

    # DEBUG: view field
    ctx.set_color([z * 2, z, 1, z * 2])
    # ctx.circle(x, y, 0.04, fill=True)
    
    if z > 0.4:
        c = Circle(x, y, 1 / (cols))
        p = c.as_polygon(n=6)
        p = p.rotate(pi / 2.0)
        p.draw(ctx)

ctx._ctx