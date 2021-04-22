#%%
import ctx
from lib.param import *

# == SETUP PARAMS ================
SIZE = 9
FILL = 3
COLOR = 12
POINT = 4

params = {
    SIZE: FloatParam("Size", min_value=0.0, max_value=1.0, default=0.5),
    FILL: OptionParam("Fill"),
    COLOR: ColorParam("Color A", default=[1, 0, 1, 1]),
    POINT: PointParam("Coords", default=[0.5, 0.5]),
}
# ================================

# == RENDER ======================
# from geom.circle import Circle
from geom.grid import Grid

# from numpy import linspace, meshgrid, column_stack


def render():
    # size = 120
    size = 8
    grid = Grid(-1, -1, 2, 2, rows=size, cols=size)

    ctx.clear([0, 0, 0, 1])
    ctx.set_range(-1, 1)

    for xy in grid.centers():
        x, y = xy

        print(x, y)
        color = ctx.sample_point(x, y)
        ctx.set_color(color)

        ctx.circle(x, y, 0.1, fill=True)


# ================================

# == PROTOTYPE ===================
%load_ext helpers.ipython_cairo
ctx._setup(600, 400)
ctx.set_range(-1, 1)
ctx._prep_sampler("helpers/perlin-noise.png")

# params[SIZE].value = 0.7
# params[COLOR].value = [1, 1, 0, 1]
# params[FILL].value = True
# params[POINT].value = [0.2, 0.7]

render()
ctx._ctx
# ================================