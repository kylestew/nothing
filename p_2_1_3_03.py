#%%
from geom.grid import Grid
from geom.line import Line
from numpy.random import random

count = 16
grid = Grid(1, 1, count, count, padding=-0.001)
lines = []
for rect in grid.cells():
    poly = rect.resample(num=40)
    c = rect.center() + ((random(2) - 0.5) * 0.03)
    for vert in poly.vertices():
        lines.append(Line(c, vert))

# len(lines)
    
%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 2400
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#EEAA22")
FOREGROUND = hex_to_rgba("#000000")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(0, 1), range=(0, 1))
render.set_line_width(1.6 * PIXEL)

for line in lines:
    a, b = line.vertices()
    render.line(a, b)
    # render.circle(pt, 0.01)

render.ctx
