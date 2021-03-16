#%%
# perlin noise -> vector flow field
from perlin import generate_perlin_noise_2d
import numpy as np
np.random.seed(1)
noise_density = 128
noise = generate_perlin_noise_2d((noise_density, noise_density), (8, 8))
theta = noise * 2 * np.pi
xs = np.sin(theta)
ys = np.cos(theta)
flow_field = np.column_stack((xs.flatten(), ys.flatten())).reshape(noise_density, noise_density, 2)
flow_field.shape

%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

from numpy import array, pi, cos, sin, column_stack

CANVAS_MULT = 8
CANVAS_SQUARE_SIZE = noise_density * CANVAS_MULT
BACKGROUND = hex_to_rgba("#332633")
FOREGROUND = hex_to_rgba("#ee99aa")
DEBUG = hex_to_rgba("#ff00ee")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, DEBUG)
# render.remap(domain=(-0.05, 1.05), range=(-0.05, 1.05))
render.remap(domain=(0, noise_density * CANVAS_MULT), range=(0, noise_density * CANVAS_MULT))
render.set_line_width(1.0)

for y in range(noise_density):
    for x in range(noise_density):
        a = array((x, y)) * CANVAS_MULT # space out for display
        b = a + flow_field[x][y] * CANVAS_MULT * 1.2
        render.line(a, b)

render.ctx