#%%

count = 128
inner_rad = 0.15
outer_rad = 1.5
line_width = 1.5
shatter_count = 36
threshold = 0.5
step = 0.3
center = (0, 0.2)


%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
size = 600
ctx._setup(size, size)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-1, 1)
ctx.set_line_width(line_width)
ctx.set_line_cap(1)
ctx.set_color([1, 1, 1, 1])

from numpy import array, sort
from numpy.random import rand
from lib.field import Perlin3DField
from geom.line import Line
from geom.circle import Circle

field = Perlin3DField((256, 256, 32), (16, 16, 4), seed=8)
fn = field.fn(((-1, 1), (-1, 1), (0, 1)))

def create_rays(a, b, t, splits, threshold=0.5):
    # create line
    line = Line(a, b)
    # break into random segments
    breaks = sort(rand(splits))
    segments = line.shatter(breaks)
    # remove some segments based on sampling perlin field
    rays = []
    for segment in segments:
        x, y = segment.center()
        n = fn(x, y, t) * 0.5 + 0.5
        if n > threshold:
            rays.append(segment)

    return rays
        
# create original rays
rays = []
cx, cy = center
inner = Circle(cx, cy, inner_rad)
outer = Circle(cx, cy, outer_rad)
for endpoints in zip(inner.vertices(n=count), outer.vertices(n=count)):
    a, b = endpoints
    segs = create_rays(a, b, step, shatter_count, threshold=threshold)
    rays += segs

# render!
for ray in rays:
    ctx.set_color([1, 1, 1, 1])
    ray.draw(ctx)
    
ctx._ctx
