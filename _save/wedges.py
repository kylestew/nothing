#%%
#================================
#== SETUP PARAMS ================
#================================
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]

# ???
step = 0.4


#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx

count = 4

ctx._setup(600, 600)
ctx.clear([0, 0, 0, 1])
ctx.set_range(0, count)
ctx.set_line_width(2)
ctx.set_color([1, 0, 1, 1])

# from geom.arc import Arc
# from numpy import roll
# from numpy import pi

# triangle to wedge
# from geom.circle import Circle
# circ = Circle()
# tri = circ.as_polygon(n=3)
# tri = tri.rotate(pi / 2)
# tri.draw(ctx)
# x, y = tri.center()
# ctx.circle(x, y, 0.02)

# ptsA = tri.points
# ptsB = roll(ptsA, 1, axis=0)

# arcs = []
# for a, b in zip(ptsA, ptsB):
    # arc = Arc.arcFrom2Points(b, a, 1.8)
    # arc.draw(ctx)

from geom.grid import Grid
grid = Grid(-0.25, -0.25, count, count, count, count)
for pt in grid.centers():
    x, y = pt
    ctx.circle(x, y, 0.01)

grid = Grid(0.25, 0.25, count, count, count, count)
ctx.set_color([1, 1, 1, 1])
for pt in grid.centers():
    x, y = pt
    ctx.circle(x, y, 0.01)

ctx._ctx
