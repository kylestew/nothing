#%%
# PARAMS
color_a = [1, 0, 1, 1]
color_b = [0, 1, 1, 1]
color_c = [1, 1, 0, 1]
color_d = [1, 0, 0, 1]

%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx
ctx._setup(600, 600)

w, h = ctx.get_canvas_size()
ctx.clear([0, 0, 0, 1])
ctx.set_range(-1.2, 1.2)
ctx.set_line_width(1.0)
ctx.set_color(color_a)

# create base pentagram
from geom.polygon import Polygon
penta = Polygon.ngon(5)
ctx.path(penta.points.tolist(), fill=False, closed=True)

# find midpoints on all 5 edges
edges = penta.edges()
midpoints = map(lambda e: e.point_at(0.5), edges)
# for line in edges:
    # print(line.point_at(0.5))

# DEBUG: display midpoints
ctx.set_color(color_b)
for pt in midpoints:
    ctx.circle(pt[0], pt[1], 0.02, fill=True)
    
ctx._ctx

#%%

"""
# find midpoints
# from numpy import array
def midpoint(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)
points = penta.points
midpoints = []
for i0, pt in enumerate(penta.points):
    i1 = i0 + 1
    if i1 >= len(points):
        i1 = 0
    p0 = points[i0]
    p1 = points[i1]
    mpt = midpoint(p0[0], p0[1], p1[0], p1[1])
    midpoints.append(mpt)
midpoints = array(midpoints)
    
# create lines between midpoints and opposite points
from numpy import roll, column_stack
midpoints = roll(midpoints, len(midpoints) + 1)
lines = column_stack((points, midpoints))

ctx.set_color(color_c)
for line in lines:
    # print(line)
    x0, y0, x1, y1 = line
    ctx.line(x0, y0, x1, y1)



# DEBUG: display them

# TODO: find midpoint for each point
# move towards opposite point
"""

