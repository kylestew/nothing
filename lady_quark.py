#%%
# perlin noise -> vector flow field
from perlin import generate_perlin_noise_2d
import numpy as np
np.random.seed(0)
noise_density = 512
noise = generate_perlin_noise_2d((noise_density, noise_density), (16, 8))
noise.shape
xs = np.sin(noise)
ys = np.cos(noise)
# xs.shape
flow_field = np.column_stack((xs, ys)).reshape(noise_density, noise_density, 2)

# 3 x 3 rectangular grid cells
from geom.grid import Grid
grid_size = 5
cells = Grid(1, 1, grid_size, grid_size, padding=0.002).cells()

# shrinking nested rectangles
from numpy import linspace, array

scale = linspace(1, 0.3, 32)
resamp_num = 64
polys = []
for cell in cells:
    # outer rect never mutates
    # polys.append(cell.as_polygon())

    # build inner rects
    for s in scale:
        p = cell.scale(s, s)
        p = p.resample(num=resamp_num)

        # generate vector noise
        idx = (p.points * 255).astype(int)
        samps = array(list(map(lambda i: flow_field[i[0]][i[1]], idx)))
        samps *= 0.0333

        p.points += samps

        polys.append(p)

%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 2400
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#332633")
FOREGROUND = hex_to_rgba("#ee99aa99")
DEBUG = hex_to_rgba("#ff00ee")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(-0.05, 1.05), range=(-0.05, 1.05))
render.set_line_width(4.0 * PIXEL)

for poly in polys:
    render.set_front(FOREGROUND)
    render.path(poly.vertices(), closed=True)

    # render.set_front(BACKGROUND)
    # for v in poly.vertices():
        # render.circle(v, 0.001)

render.ctx