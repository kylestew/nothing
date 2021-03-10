#%%
%load_ext ipython_cairo
from cairo import CairoError
from cairo import Operator
from numpy import array
from numpy.random import random
from modules.color import hex_to_rgba

# BACKGROUND = hex_to_rgba("#353647")
BACKGROUND = hex_to_rgba("#FFFFFFFF")
COLORS = list(map(hex_to_rgba, [
        "#fcd1d1",
        "#ece2e1",
        "#d3e0dc",
        "#aee1e1",
]))
# draw each line with transparency
ALPHA = 0.04

WALKER_COUNT = int(random(1)[0] * 6) + 2
CANVAS_SQUARE_SIZE = 1200
ONE_PIXEL = 1.0 / CANVAS_SQUARE_SIZE
EDGE_PADDING_PERC = 0.05
# each walker has X agents all starting on a horizontal line - vertically centered
AGENT_COUNT = 256 * 1
# how should random walks scale in the X and Y direction
SCALE = array((0.2, 1), dtype="float") * 0.02 * ONE_PIXEL

from modules.render import Render
from modules.walkers import Walkers

walkers = []
for i in range(WALKER_COUNT):
    scale = random(2) * SCALE
    res = int(random(1)[0] * 4) + 2
    w = Walkers(AGENT_COUNT, scale, pnoise_res=res).perlin()
    walkers.append(w)
    
render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, COLORS[0])
render.remap(domain=(0 - EDGE_PADDING_PERC, 1 + EDGE_PADDING_PERC), range=(0.5, -0.5))
render.set_line_width(4 * ONE_PIXEL)

ITER = 256
render.set_operator(Operator.ADD)
# render.set_operator(Operator.SCREEN)
# render.set_operator(Operator.COLOR_DODGE)
for _ in range(ITER):
    for k, w in enumerate(walkers):
        col = COLORS[k % len(COLORS)]
        col[3] = ALPHA
        render.set_front(col)

        dots = next(w)
        render.path(dots)
        
render.ctx

#%%