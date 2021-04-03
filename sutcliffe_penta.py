#%%
#================================
#== SETUP PARAMS ================
#================================
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]

# number of recursions
step = 0.25

# side count
param_a = 0.1

# strut length
param_b = 0.15

# strut noise effect
# (samples incoming noise)
param_c = 0.0

# strut pct (adds rotation)
param_d = 0.5

# strut pct noise effect
# (samples incoming noise)
param_e = 0.0

# connection relative size
param_f = 0.01

# draw pentagons
option_a = True
# draw struts
option_b = True
# draw connections
option_c = True

%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)
#================================

#================================
#== MAIN ========================
#================================
from geom.polygon import Polygon
from geom.line import Line
from lib.interp import lerp
from numpy import roll, column_stack

# translate params
iter_count = int(lerp(1, 12, step))
sides = int(lerp(3, 24, param_a))
strut_length = param_b
# noise
strut_pct = param_d
# noise
conn_rel_size = lerp(0.01, 0.5, param_f)

def penguin(penta):
    # find midpoints on edges
    edges = penta.edges()
    midpoints = list(map(lambda e: e.point_at(strut_pct), edges))

    # render penta
    if option_a:
        ctx.set_color(color_a)
        ctx.path(penta.points.tolist(), fill=False, closed=True)

    # create struts from midpoints towards opposite points
    def make_strut(line):
        x0, y0, x1, y1 = line
        l = Line((x0, y0), (x1, y1))
        return l.split_at(strut_length)[0]

    midpoints = roll(midpoints, len(midpoints) + 1)
    lines = column_stack((midpoints, penta.points))
    struts = list(map(make_strut, lines))

    # render struts (and connections)
    for line in struts:
        if option_b:
            ctx.set_color(color_b)
            line.draw(ctx)

        if option_c:
            ctx.set_color(color_c)
            for pt in line.points:
                # TODO: scale connection with area of penta
                ctx.circle(pt[0], pt[1], conn_rel_size, fill=False)

    # make new penta
    pts = list(map(lambda s: s.points[-1], struts))
    return Polygon(pts)


ctx.clear([0, 0, 0, 1])
ctx.set_range(-1.2, 1.2)
ctx.set_line_width(1.0)

# create largest pentagon
# TODO: how to recurse?
p0 = Polygon.ngon(sides)
p1 = penguin(p0)

# p2 = penguin(p1)
# p3 = penguin(p2)
# p4 = penguin(p3)
# p5 = penguin(p4)

# render last
if option_a:
    ctx.set_color(color_a)
    ctx.path(p1.points.tolist(), fill=False, closed=True)

ctx._ctx