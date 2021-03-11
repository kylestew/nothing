#%%
from geom.polygon import Polygon

p = Polygon(n=5, r=1)
p.points

%load_ext helpers.ipython_cairo
from modules.render import Render

CANVAS_SQUARE_SIZE = 400
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = [1, 1, 1, 1]
FOREGROUND = [1, 0, 0, 1]

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(-1, 1), range=(-1, 1))
render.set_line_width(4.0 * PIXEL)

render.path(p.points, closed=True)
        
render.ctx