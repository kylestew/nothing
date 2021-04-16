#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-2, 2)
ctx.set_line_width(1)


ctx.set_color([1, 1, 1, 1])
ctx.rect(-1, -1, 2, 2)

from geom.grid import Grid
grid = Grid(-1, -1, 2, 2, rows=8, cols=8, offset=0.5)

ctx.set_color([1, 0, 1, 1])
grid.draw(ctx, px=4)

ctx.set_color([1, 1, 1, 1])
for pt in grid.centers():
    x, y = pt
    ctx.circle(x, y, 0.05)

ctx._ctx