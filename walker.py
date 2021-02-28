#%%

from numpy import linspace
from numpy import zeros
from numpy import column_stack
from numpy.random import random


class BadWalkers:
    def __init__(self, size, edge, scale, num):
        self.size = size
        self.edge = edge
        self.n = num
        self.one = 1.0 / size

        self.scale = scale

        x = linspace(edge, 1.0 - edge, self.n)
        y = zeros(self.n, "float")
        self._walkers = column_stack((x, y))
        self._speed = zeros((self.n, 2), "float")

    def run(self):
        while True:
            random(self.n)
            rand = (1.0 - 2.0 * random(self.n)) * self.scale
            self._walkers[:, 1] += rand
            yield self._walkers

#%%
from numpy import array

SIZE = 1000
ONE = 1.0 / SIZE
DOT = ONE * 4
EDGE = 0.05

SCALE = 0.003
NUM = 128

# ITER = 1900
ITER = 19

w = BadWalkers(SIZE, EDGE, SCALE, NUM).run()

from modules.render import Render
%load_ext ipython_cairo

BACK = [235/255, 172/255, 162/255, 1] # ebaca2
PRIMARY = [74/255, 145/255, 158/255, 0.01] # 4a919e
SECONDARY = [33/255, 46/255, 83/255, 0.01] # 212e53

size = 1200

render = Render(size, BACK, PRIMARY)
render.remap(domain=(0, 1), range=(0.5, -0.5))
# render.remap(domain=(-1, 1), range=(1, -1))
render.set_line_width(ONE)

render.ctx.translate(0.5, 0)
render.ctx.rotate(-0.25)
render.ctx.translate(-0.5, 0)

for _ in range(ITER):
    dots = next(w)

    # render.path(dots)

    for pt in dots:
        x, y = pt
        render.circle(x, y, DOT, fill=True)
        
render.ctx.translate(0.5, 0)
render.ctx.rotate(0.5)
render.ctx.translate(-0.5, 0)
render.set_front(SECONDARY)

for _ in range(ITER):
    dots = next(w)
    for pt in dots:
        x, y = pt
        render.circle(x, y, DOT, fill=True)

render.ctx