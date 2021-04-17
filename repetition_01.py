# https://www.instagram.com/p/CNpivLFjxUj/


#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(900, 900)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-0.3, 1.3)
ctx.set_line_width(1)

from geom.grid import Grid
cols = 4
grid = Grid(0, 0, 1, 1, rows=15, cols=cols, padding=0, offset=0.5)

ctx.set_color([1, 0, 1, 1])
# grid.draw(ctx, px=4)

from geom.circle import Circle
from numpy import pi
from numpy.random import random

from lib.field import Perlin2DField

field = Perlin2DField((32, 32), (8, 16), seed=126)
fn = field.fn(((0, 1), (0, 1)))

ctx.set_color([1, 1, 1, 1])
for pt in grid.centers():
    x, y = pt
    throw = fn(x, y)
    if throw > 0:
        c = Circle(x, y, 1 / (cols * 2))
        p = c.as_polygon(n=6)
        p = p.rotate(pi / 2.0)
        p.draw(ctx)

ctx._ctx