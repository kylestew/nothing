#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx

ctx._setup(600, 600)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-1.2, 1.2)
ctx.set_line_width(2)
ctx.set_color([1, 0, 1, 1])

from geom.arc import Arc
from numpy import linspace, roll, column_stack
from numpy import pi

# make a list of theta sweeps
# thetas = linspace(0, 2*pi, 6)
# thetas = column_stack((thetas, roll(thetas, 1)))
# thetas

# triangle to wedge
from geom.circle import Circle
circ = Circle()
tri = circ.as_polygon(n=3)
tri = tri.rotate(pi / 2)
tri.draw(ctx)
x, y = tri.center()
ctx.circle(x, y, 0.02)



ctx._ctx



#%%

arc = Arc(start=pi, end=pi + pi / 2.0)
arc.draw(ctx)

ctx.set_line_width(4.0)
ctx.set_color([1, 1, 1, 1])

a = arc.point_at(0.3)
b = arc.point_at(0.9)
arc2 = Arc.arcFrom2Points(a, b, 1.0)
arc2.draw(ctx)

ctx._ctx