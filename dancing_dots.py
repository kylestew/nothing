"""
#%%
#================================
#== SETUP PARAMS ================
#================================
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]

# ???
step = 0.0

# grid A count
param_a = 0.2

# grid A offset
point_a = [0.5, 0.5]


%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)
#================================
"""

# ================================
# == MAIN ========================
# ================================
from lib.interp import lerp, remap
from geom.grid import Grid

count_a = int(lerp(1, 128, param_a))

x_off, y_off = point_a
grid_a = Grid(x_off - 1, y_off - 1, 2, 2, count_a, count_a)


ctx.clear([0, 0, 0, 1])
ctx.set_range(0, 1)
ctx.set_line_width(2)


def draw_grid(grid):
    for pt in grid.centers():
        x, y = pt
        ctx.circle(x, y, 0.002)


ctx.set_color(color_a)
draw_grid(grid_a)

# ctx.set_color(color_b)
# draw_grid(grid_b)

# ctx._ctx
