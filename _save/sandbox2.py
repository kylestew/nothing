#%%
# LOAD sample image
import matplotlib.image as mpimg

img = mpimg.imread("helpers/grad.png")
img = (img * 255).astype(int)
height, width, depth = img.shape
img = img.reshape(width * height, depth)
out = []
for row in img:
    # rgba -> argb
    out.append(row[3])
    out.append(row[0])
    out.append(row[1])
    out.append(row[2])

import numpy as np

view = memoryview(np.array(out))
print(len(view))


#%%
from lib.sketch import Sketch
from numpy import array, linspace, column_stack
from numpy import pi, sin, cos
from lib.interp import lerp


class Sandbox(Sketch):
    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        # range = [-1, 1]
        range = None  # TODO: normalize canvas!
        super().__init__(w, h, clear_color, range)
        
    def gen_circle(self, x, y, rad, n, f):
        a = linspace(0, pi * 2, n + 1)
        rads = rad + f(a)
        circ = (x, y) + column_stack((cos(a) * rads, sin(a) * rads))
        return circ[:-1]

    def draw(self):
        # constants
        resolution = 640
        cx = self.w / 2
        cy = self.h / 2

        # prepare params
        # step = self.step
        size = self.h * self.param_a / 2
        disturbance = lerp(0, 128, self.param_b)
        thickness = lerp(0.5, 8.0, self.param_c)
        # speed = lerp(0.1, 10, self.param_d)

        def fa(theta):
            # xys = column_stack((cx + sin(24 * theta) * disturbance, cy + cos(3 * theta) * disturbance))
            # xys = column_stack((cx + sin(24 * theta) * disturbance, cy + cos(3 * theta) * disturbance))
            xys = (cx, cy) + column_stack((cos(theta) * size, sin(theta) * size))
            vectors = []
            for xy in xys:
                vectors.append(self.luminosity_at(xy.astype(int)) * disturbance)
            return array(vectors)

        # def fa(theta):
            # return (sin(24 * theta) + cos(3 * theta)) * disturbance

        # (opt) render base shape
        if self.option_a:
            circ = self.gen_circle(cx, cy, size, resolution, fa)
            self.set_color(self.color_a)
            self.set_line_width(thickness)
            self.path(circ, closed=True)



%load_ext helpers.ipython_cairo
sketch = Sandbox(width, height)
sketch.set_layer_in_data(view, width * depth)

step = 100
sketch.set_step(step)

shape_size = 0.5
disturbance = 0.5
thickness = 0.5
# speed = 0.05
sketch.set_params(shape_size, disturbance, thickness, 0)

func_a = True
func_b = False
func_c = False
func_d = False
sketch.set_options(func_a, func_b, func_c, func_d)

sketch.set_colors(
    [0xFF, 0xFF, 0xFF, 0xFF],
    [0x04, 0xFF, 0x00, 0xFF],
    [0xFF, 0xFF, 0x00, 0x00],
    [0xFF, 0xFF, 0x00, 0x00],
    )

d = sketch.render()
sketch.ctx