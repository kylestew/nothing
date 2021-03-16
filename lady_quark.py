#%%
from geom.rect import Rect
from geom.polygon import Polygon

rect = Rect(0, 0, 1, 2)
poly = rect.as_polygon()
poly.vertices()


#%%
from geom.rect import Rect
from geom.grid import Grid

grid_size = 3
cells = Grid(1, 1, grid_size, grid_size, padding=0.008).cells()

#%%

from modules.perlin import generate_perlin_noise_2d
pnoise = generate_perlin_noise_2d((512, 512), (8, 8))
pnoise

# %%
from geom.rect import Rect
from numpy import linspace

scale = linspace(1, 0.4, 16)
polys = []
for rect in cells:
    polys.append(rect.as_polygon())
    for s in scale:
        p = rect.scale(s, s)
        p = p.resample(num=8)
        print(p)
        polys.append(p)
polys[1].points

#%%
%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 800
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#332633")
FOREGROUND = hex_to_rgba("#eeaaee")
DEBUG = hex_to_rgba("#ff00ee")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(0, 1), range=(0, 1))
render.set_line_width(1.5 * PIXEL)

for poly in polys:
    render.set_front(FOREGROUND)
    render.path(poly.vertices(), closed=True)

    render.set_front(DEBUG)
    for v in poly.vertices():
        render.circle(v, 0.002)

render.ctx