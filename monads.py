#%%
#================================
#== SETUP PARAMS ================
#================================
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]

# TODO: spit out rays
# ???
# step = 0.05

# ray count
param_a = 0.5

# inner_rad
param_b = 0.15
# outer_rad
param_c = 1.0

# line_width
param_d = 0.2

# shatter count
param_e = 0.9
# threshold
param_f = 0.5

# inner rotation
param_g = 0
# outer rotation
param_h = 0

point_a = [0.0, 0.0]

%load_ext helpers.ipython_cairo
from cairo import LINE_CAP_ROUND, LINE_JOIN_ROUND
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)
#================================

# ================================
# == MAIN ========================
# ================================
from lib.interp import lerp
from numpy import sort, array, pi, linspace
from geom.line import Line
from geom.circle import Circle
from lib.field import Perlin2DField

count = int(lerp(3, 256, param_a))
inner_rad = param_b
outer_rad = lerp(inner_rad, inner_rad + 2, param_c)
line_width = lerp(0.1, 8.0, param_d)
shatter_count = int(lerp(12, 128, param_e))
threshold = param_f
center = point_a
inner_theta = lerp(-pi, pi, param_g)
outer_theta = lerp(-pi, pi, param_h)

field = Perlin2DField((256, 256), (4, 4), seed=0)
fn =field.fn(((-1, 1), (-1, 1)))

def create_rays(a, b, splits, threshold=0.5):
    # create line
    line = Line(a, b)
    # break into n segments
    breaks = linspace(0, 1, splits)
    segments = line.shatter(breaks)
    # remove some segments based on sampling perlin field
    rays = []
    for segment in segments:
        x, y = segment.center()
TODO: make rays travel outwards
        # n = array(ctx.sample_point(x, y))
        n = fn(x, y)
        # convert to grayscale luminosity
        # n = (n[0:3] * array([0.21, 0.72, 0.07])).sum()
        if n > threshold:
            rays.append(segment)
    return rays


# shape arrays around void circle
rays = []
cx, cy = center
inner = Circle(cx, cy, inner_rad)
outer = Circle(cx, cy, outer_rad)
inner = inner.rotate(inner_theta)
outer = outer.rotate(outer_theta)

for endpoints in zip(inner.vertices(n=count), outer.vertices(n=count)):
    a, b = endpoints
    segs = create_rays(a, b, shatter_count, threshold=threshold)
    rays += segs

ctx.clear([0, 0, 0, 1])
ctx.set_range(-1, 1)
ctx.set_line_width(line_width)
ctx.set_line_cap(1)
ctx.set_color(color_a)

for ray in rays:
    ray.draw(ctx)

ctx._ctx