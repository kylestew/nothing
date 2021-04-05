#%%
#================================
#== SETUP PARAMS ================
#================================
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]

# number of recursions
step = 0.4

# side count
param_a = 0.20

# strut length
param_b = 0.0

# strut noise effect
# (samples incoming noise)
param_c = 0.5

# strut pct (adds rotation)
param_d = 0.75

# strut pct noise effect
# (samples incoming noise)
param_e = 0.5

# line thickness
param_f = 0.2

# line graduation
param_g = 0.5

# dual recursion?
option_a = True
# draw pentagons
option_b = True
# draw struts
option_c = True

%load_ext helpers.ipython_cairo
from cairo import LINE_CAP_ROUND, LINE_JOIN_ROUND
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)
#================================

# ================================
# == MAIN ========================
# ================================
from geom.polygon import Polygon
from geom.line import Line
from lib.interp import lerp, remap
from numpy import array
from numpy.random import rand

# translate params
iter_count = int(lerp(1, 24, step))
sides = int(lerp(3, 24, param_a))
strut_length = param_b
# noise
strut_pct = param_d
# noise
max_thickness = lerp(0.0, 12, param_f)
min_thickness = lerp(max_thickness, max_thickness / 12, param_g)


def penguin(penta, n):
    t = remap(1, iter_count, 0, 1, n)
    thick = lerp(min_thickness, max_thickness, t)
    ctx.set_line_width(thick)

    # find midpoints on edges
    edges = penta.edges()
    count = len(edges)
    pcts = rand(count) * param_e * strut_pct
    midpoints = list(map(lambda e: e[0].point_at(e[1]), zip(edges, pcts)))
    lengths = rand(count) * strut_length

    # project orthogonal lines (struts) inwards from edges
    def make_strut(data):
        edge, midpoint, length = data
        u = edge.unit_vector()
        v = array((u[1], -u[0]))  # orthogonal vector
        return Line.from_vector(-v * length, midpoint)
    struts = list(map(make_strut, zip(edges, midpoints, lengths)))

    # render struts (and connections)
    for line in struts:
        if option_c:
            ctx.set_color(color_b)
            line.draw(ctx)

    # render penta
    if option_b:
        ctx.set_color(color_a)
        ctx.path(penta.points.tolist(), fill=False, closed=True)

    # make new penta
    pts = list(map(lambda s: s.points[-1], struts))

    p1 = Polygon(pts)

    if n == 1:
        # render last
        if option_b:
            ctx.set_color(color_a)
            ctx.path(p1.points.tolist(), fill=False, closed=True)
        return
    else:
        # if option_a:
            # recurse smaller sections
            # pts = 
            # penguin(p...)

        penguin(p1, n - 1)


ctx.clear([0, 0, 0, 1])
ctx.set_range(-1.2, 1.2)
ctx.set_line_cap(1)  # round

p0 = Polygon.ngon(sides)
penguin(p0, iter_count)

ctx._ctx