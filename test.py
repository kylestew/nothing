"""
print("step:", step)
print("params:", param_a, param_b, param_c, param_d)
print("options:", option_a, option_b, option_c, option_d)
print("colors:", color_a, color_b, color_c, color_d)
print("points:", point_a, point_b)
print("sample:", ctx.sample_point(0, 0))
"""

w, h = ctx.get_canvas_size()
print("canvas size", w, h)

ctx.clear([0, 0, 0, 1])
ctx.set_range(0, 1.0)

ctx.set_color(color_a)
ctx.set_line_width(1.0)
ctx.line(0, 0, 1, 1)
