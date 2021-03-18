#%%
# perlin noise -> vector flow field
from perlin import generate_perlin_noise_2d
from numpy import array
import numpy as np
np.random.seed(5)
noise_density = 1024
noise = generate_perlin_noise_2d((noise_density, noise_density), (8, 8))
theta = noise * 2 * np.pi
xs = np.sin(theta)
ys = np.cos(theta)
flow_field = np.column_stack((xs.flatten(), ys.flatten())).reshape(noise_density, noise_density, 2)
flow_field.shape
flow_field[0][1]

iterations = 512
mult = 0.001

from geom.rect import Rect
rect = Rect(0.3, 0.3, 0.4, 0.4)
poly = rect.resample(dist=0.0005)
paths = [ poly.points ]
for i in range(iterations):
    xy = (poly.points * noise_density).astype(int)
    samps = []
    for x, y in xy:
        if x < 0:
            x += noise_density
        if x >= noise_density:
            x -= noise_density
        if y < 0:
            y += noise_density
        if y >= noise_density:
            y -= noise_density
        samps.append(flow_field[x][y])
    poly.points += array(samps) * mult
    paths.append(poly.points.copy())

    
%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

from numpy import array, pi, cos, sin, column_stack

CANVAS_SQUARE_SIZE = noise_density * 2
BACKGROUND = hex_to_rgba("#332633")
FOREGROUND = hex_to_rgba("#ee99aa12")
DEBUG = hex_to_rgba("#00FFFF24")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
# render.remap(domain=(-0.05, 1.05), range=(-0.05, 1.05))

render.set_line_width(9.0)
render.set_front(hex_to_rgba("FFFFFFee"))
render.path(rect.vertices(), closed=True)

render.set_line_width(2.0)

for path in paths:
    render.set_front(FOREGROUND)
    render.path(path, closed=True)

for path in paths:
    for pt in path:
        render.set_front(DEBUG)
        render.circle(pt, 0.0001)

render.ctx