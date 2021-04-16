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

# grid A
option_a = True
# grid A filled
option_b = True
# grid A offset
point_a = [0.5, 0.5]
# grid A count
param_a = 0.2
# size A
param_b = 0.1
# line width A
param_c = 0.5

# grid B
option_c = True
# grid B filled
option_d = False
# grid B offset
point_b = [0.5, 0.5]
# grid B count
param_d = 0.5
# size B
param_e = 0.5
# line width B
param_f = 0.5


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

ctx.clear([0, 0, 0, 1])
ctx.set_range(0, 1)
ctx.set_line_width(1)

print(option_a, option_b)

show_grid_a = option_a
count_a = int(lerp(1, 128, param_a))
size_a = lerp(0.0005, 0.05, param_b)
line_width_a = lerp(0.0005, 0.05, param_c)
fill_a = option_b

show_grid_b = option_c
count_b = int(lerp(1, 128, param_d))
size_b = lerp(0.0005, 0.05, param_e)
line_width_b = lerp(0.0005, 0.05, param_f)
fill_b = option_d


def draw_grid(grid, r, fill):
    print(grid, r, fill)
    for pt in grid.centers():
        x, y = pt
        ctx.circle(x, y, r, fill=fill)


if show_grid_a:
    x_off, y_off = point_a
    grid = Grid(x_off - 1, y_off - 1, 2, 2, count_a, count_a)
    ctx.set_color(color_a)
    draw_grid(grid, size_a, fill_a)

if show_grid_b:
    x_off, y_off = point_b
    grid = Grid(x_off - 1, y_off - 1, 2, 2, count_b, count_b)
    ctx.set_color(color_b)
    draw_grid(grid, size_b, fill_b)


# ctx._ctx
