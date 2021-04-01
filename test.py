"""
print("step:", step)
print("params:", param_a, param_b, param_c, param_d)
print("options:", option_a, option_b, option_c, option_d)
print("colors:", color_a, color_b, color_c, color_d)
print("points:", point_a, point_b)
print("sample:", ctx.sample_point(0, 0))
"""

#%%
# PARAMS
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]


%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(600, 400)

w, h = ctx.get_canvas_size()
print("canvas size", w, h)

ctx.clear([0, 0, 0, 1])

ctx.set_color(color_a)
ctx.set_line_width(1.0)
ctx.line([0, 0], [w, h])

ctx.set_color(color_b)
ctx.circle(w / 2, h / 2, r = h * 0.25, fill=True)

ctx.set_color(color_c)

import numpy as np

xs = np.linspace(100, w - 100, 10)
ys = np.zeros(10) + (h / 2)
xys = np.column_stack((xs, ys))
ctx.path(xys.tolist())

ctx._ctx