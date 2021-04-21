#%%
import ctx
from lib.param import *

# == SETUP PARAMS ================
SIZE = 0
FILL = 1
COLOR = 2
POINT = 3

params = {
    SIZE: FloatParam("Size", min_value=0.0, max_value=1.0, default=0.5),
    FILL: OptionParam("Fill"),
    COLOR: ColorParam("Color A", default=[1, 0, 1, 1]),
    POINT: PointParam("Coords", default=[0.5, 0.5]),
}
# ================================

# == RENDER ======================
from geom.circle import Circle


def render():
    w, h = ctx.get_canvas_size()
    print("canvas size", w, h)
    ctx.clear([0, 0, 0, 1])
    ctx.set_range(-1, 1.0)
    ctx.set_color(params[COLOR].value)
    ctx.set_line_width(4.0)

    x, y = params[POINT].value
    circ = Circle(x=x, y=y, r=params[SIZE].value)
    circ.draw(ctx, fill=params[FILL].value)


# ================================

"""
# == PROTOTYPE ===================
%load_ext helpers.ipython_cairo
# import helpers.ae_context_mock as ctx
ctx._setup(600, 600)

params[SIZE].value = 0.7
params[COLOR].value = [1, 1, 0, 1]
params[FILL].value = True
params[POINT].value = [0.2, 0.7]

render()
ctx._ctx
# ================================
"""