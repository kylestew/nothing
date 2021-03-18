#%%
from numpy.random import choice
from numpy import empty, append
from numpy import cumsum
from numpy import column_stack

from geom.grid import Grid

# create grid of center points
size = 400
rows = 4
cells = Grid(size, size, rows, rows).cells()
centers = array(list(map(lambda cell: cell.center(), cells)))
centers = centers.flatten()
centers = centers.reshape(32, 1)
centers.shape

# generate _n_ random walks per center
n = 120000
count = rows * rows * n * 2
choices = choice([-1, 0, +1], count)
choices = choices.reshape((rows * rows * 2, n))
choices.shape

# offset each x, y choice row by center x, y 
choices = centers + choices

# reshape array
from numpy import array, concatenate
xys = []
for cell in list(choices.reshape((rows * rows,2,n))):
    for itm in cell.reshape(n,2):
        xys.append(itm.tolist())

print(len(xys))

%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba
 
CANVAS_SQUARE_SIZE = 800
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#EEAA22")
FOREGROUND = hex_to_rgba("#00000022")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(0, size), range=(0, size))

for xy in xys:
    render.dot(xy)

render.ctx
