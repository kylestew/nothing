#%%

from numpy import linspace
from numpy import ones, zeros
from numpy import column_stack


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

            # self._walkers[:, 1] = 0.5 + ()
            yield self._walkers


#%%
from numpy import array

SIZE = 1000
ONE = 1.0 / SIZE
EDGE = 0.05

SCALE = array((0, 1), "float") * 0.4
NUM = 100

w = BadWalkers(SIZE, EDGE, SCALE, NUM)
next(w.run())

#%%
from modules.render import Render
%load_ext ipython_cairo

BACK = [1, 1, 1, 1]
FRONT = [1, 0, 0, 1]

size = 600

render = Render(size, BACK, FRONT)
render.remap(domain=(0, 1), range=(0.5, -0.5))
# render.remap(domain=(-1, 1), range=(1, -1))
render.set_line_width(ONE)

for pt in next(w.run()):
    x, y = pt
    render.circle(x, y, .002, fill=True)

# render.circle(0, 0, 0.05, fill=True)
# render.circle(0.5, 0.5, 0.05, fill=True)
# render.circle(1, -0.5, 0.05, fill=True)

render.ctx