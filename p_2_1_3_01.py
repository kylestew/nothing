#%%
from geom.grid import Grid

grid_size = 64
cells = Grid(1, 1, grid_size, grid_size, padding=0.05)
centers = cells.centers()
centers

from modules.perlin import generate_perlin_noise_2d
pnoise = generate_perlin_noise_2d((512, 512), (8, 8))
pnoise

from geom.circle import Circle
from numpy import linspace
from numpy import interp
from math import sin, cos, pi
from numpy.random import rand

large_rad = (1.0 / grid_size / 2.0) * 0.9
small_rad = large_rad * 0.333
circle_count = 9
rads = linspace(large_rad, small_rad, circle_count)
def circle_stack(pos):
    noise = pnoise[int(pos[0] * 255), int(pos[1] * 255)]
    theta = interp(noise, [-1.0, 1.0], [0, 2 * pi])
    scale = rand() * large_rad * 0.666
    
    x_off = linspace(0, sin(theta) * scale, circle_count)
    y_off = linspace(0, cos(theta) * scale, circle_count)
    
    stack = []
    for r, dx, dy in zip(rads, x_off, y_off):
        stack.append(Circle(pos[0] + dx, pos[1] + dy, r))
    return stack

circle_stacks = list(map(circle_stack, centers))
circle_stacks

%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 2400
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
# BACKGROUND = hex_to_rgba("#f9f8f4")
BACKGROUND = hex_to_rgba("#EEAA22")
# FOREGROUND = hex_to_rgba("#ec3636")
FOREGROUND = hex_to_rgba("#000000")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(0, 1), range=(0, 1))
render.set_line_width(1.0 * PIXEL)

for stack in circle_stacks:
    for circle in stack:
        render.circle(circle.x, circle.y, circle.r)

render.ctx