#%%
%load_ext helpers.ipython_cairo
import helpers.ae_context_mock as ctx

ctx._setup(600, 600)
ctx.clear([0, 0, 0, 1])
ctx.set_range(-1.2, 1.2)
ctx.set_line_width(2)

from geom.circle import Circle
# from geom.polygon import Polygon

# tri = Polygon.ngon(3)
tri = Circle().as_polygon(4)
tri.bounds()
# ctx.set_color([1, 0, 1, 1])
# tri.draw(ctx, fill=False)

# ctx._ctx