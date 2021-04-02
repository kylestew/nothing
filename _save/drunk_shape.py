"""
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
"""


#%%
from lib.sketch import Sketch
from numpy import array
from lib.interp import lerp
from geom.rect import Rect
from geom.circle import Circle


class Sandbox(Sketch):
    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        # range = [-1, 1]
        range = None  # TODO: normalize canvas!
        super().__init__(w, h, clear_color, range)

    def walk_drunkly(self, pts, iterations, speed):
        paths = []
        for i in range(iterations):
            xy = pts.astype(int)
            samps = []
            for x, y in xy:
                if x < 0:
                    x += self.w
                if x >= self.w:
                    x -= self.w
                if y < 0:
                    y += self.h
                if y >= self.h:
                    y -= self.h
                samps.append(self.vector_at((x, y)))
            pts += array(samps) * speed
            paths.append(pts.copy())
        return paths

    def draw(self):
        # prepare params
        step = self.step

        size = self.h * self.param_a
        thickness = lerp(0.5, 4.0, self.param_b)
        resamp_count = int(lerp(4, 400, self.param_c))
        speed = lerp(0.1, 10, self.param_d)

        # create base shape
        circ = Circle(self.w / 2, self.h / 2, size / 2)

        # calculate drunk walk
        poly = circ.as_polygon(n=resamp_count)
        paths = self.walk_drunkly(poly.points, step, speed)

        # (opt) render base shape
        if self.option_a:
            self.set_color(self.color_a)
            self.set_line_width(thickness * 4.0)
            self.path(circ.vertices(64), closed=True)

        # (opt) draw connectors
        if self.option_b:
            self.set_color(self.color_b)
            self.set_line_width(thickness)
            for path in paths:
                self.path(path, closed=True)

        # (opt) draw walkers
        if self.option_c:
            self.set_color(self.color_c)
            for path in paths:
                for pt in path:
                    self.circle(pt, 2.0 * thickness, fill=True)


"""
%load_ext helpers.ipython_cairo
sketch = Sandbox(width, height)
sketch.set_layer_in_data(view, width * depth)

step = 500
sketch.set_step(step)

shape_size = 0.2
thickness = 0.05
complexity = 0.2
speed = 0.05
sketch.set_params(shape_size, thickness, complexity, speed)

shape = True
connectors = False
walkers = True
sketch.set_options(shape, connectors, walkers, False)

sketch.set_colors(
    # shape
    [0xFF, 0xFF, 0xFF, 0xFF],
    # connectors
    [0x04, 0xFF, 0x00, 0xFF],
    # walkers
    [0xFF, 0xFF, 0x00, 0x00],
    [0xFF, 0xFF, 0x00, 0x00],
    )

d = sketch.render()
sketch.ctx
"""