#%%
import ctx
from lib.param import FloatParam, OptionParam

# == SETUP PARAMS ================
STEP = "step"
OPTION_A = "option_a"

params = {
    STEP: FloatParam("Step", min_value=0.0, max_value=2.0, default=1.2),
    OPTION_A: OptionParam("Option A"),
}
# ================================

# == RENDER ======================
def render():
    w, h = ctx.get_canvas_size()
    print("canvas size", w, h)
    ctx.clear([0, 0, 0, 1])
    ctx.set_range(0, 1.0)
    ctx.set_color([1, 0, 1, 1])
    ctx.set_line_width(1.0)
    print(params)
    # y = params[STEP].value
    y = 0.5
    ctx.line(0, 0, 1, y)


# ================================

"""
# == PROTOTYPE ===================
%load_ext helpers.ipython_cairo
# import helpers.ae_context_mock as ctx
ctx._setup(600, 600)

params[STEP].value = 0.7

render()
ctx._ctx
# ================================
"""