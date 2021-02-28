#%%
import numpy as np
from numpy import column_stack, pi
from numpy.random import random
from numpy.random import randint

TWOPI = 2.0 * pi

INUM = 1000
STP = 0.00000003

# pick random count of angles to sweep (become points on circle)
pnum = randint(15, 100)

# sweep circle by defining _pnum_ regularly spaced angles (with random starting angle)
start = random() * TWOPI
theta = start + np.linspace(0, TWOPI, pnum)

# convert angles to points randomizing distance from center
offset = (0.1 + random() * 0.4)
path = np.column_stack((np.cos(theta), np.sin(theta))) * offset

path

#%%
# scale up noise more towards end of angle sweep
scale = np.arange(pnum).astype('float') * STP

#%%
def f(x, y):
    while True:
        yield np.array([[x, y]])
    
guide = f(0.5, 0.5)

#%%
# guide
# path
# scale = ???

noise = np.zeros(pnum, 'float')

# g = next(guide)

# disturb noise each iteration
r = 1.0 - 2.0 * random(pnum)
noise[:] += r * scale

# random angles?
a = random(pnum) * TWOPI
rnd = np.column_stack((np.cos(a), np.sin(a)))

# path += rnd
# rnd



#%%
%load_ext ipython_cairo
import cairo

WIDTH, HEIGHT = 600, 600

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
# ctx.set_antialias(cairo.Antialias.NONE)

# canvas: [-1, 1] origin at center
ctx.scale(WIDTH / 2.0, -HEIGHT / 2.0)
ctx.translate(1, -1)
line_width = 2
ctx.set_line_width(line_width / (WIDTH / 2.0))

for p in path:
    ctx.move_to(0, 0)
    ctx.line_to(p[0], p[1])
    ctx.stroke()

surface