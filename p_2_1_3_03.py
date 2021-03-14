#%%
from geom.rect import Rect
from geom.resample.resample import Sampler

rect = Rect(-0.5, -0.5, 1, 1)
poly = rect.resample(num=40)
len(poly.vertices())

from geom.line import Line

c = rect.center()
lines = []
for vert in poly.vertices():
    lines.append(Line(c, vert))
len(lines)
lines[0].points
    
# rect.center()

#%%
%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 900
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#EEAA22")
FOREGROUND = hex_to_rgba("#000000")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(-1, 1), range=(-1, 1))
render.set_line_width(4.0 * PIXEL)

for line in lines:
    a, b = line.vertices()
    render.line(a, b)
    # render.circle(pt, 0.01)

render.ctx
