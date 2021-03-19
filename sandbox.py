#%%
from lib.sketch import Sketch
from numpy import sin, cos, array, pi
from lib.interp import lerp


class Sandbox(Sketch):
    def __init__(self, w, h):
        back = [0, 0, 0, 0]
        front = [1, 0, 1]
        # range = [-1, 1]
        range = None  # TODO: how to deal with this?
        super().__init__(w, h, range, back, front)

    def vector_at(self, xy):
        samp = self.sample_layer_in(xy)
        # convert to grayscale luminosity
        val = 2 * pi * (samp[0:3] * array([0.21, 0.72, 0.07])).sum()
        # use val as angle for vector
        return array((sin(val), cos(val)))

    def draw(self):
        from numpy import linspace

        # parmA -> size of cell
        cell_size = lerp(8, 120, self.parmA)
        mult = lerp(0.1, 2, self.parmB)

        for y in linspace(0, self.h - 1, int(self.h / cell_size)):
            for x in linspace(0, self.w - 1, int(self.w / cell_size)):
                vec = self.vector_at((int(x), int(y)))
                a = array((x, y))
                b = a + vec * mult * cell_size
                self.line(a, b)


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

#%%
%load_ext helpers.ipython_cairo
sketch = Sandbox(width, height)
sketch.set_layer_in_data(view, width * depth)
sketch.set_params(0.5, 0.5)
d = sketch.render()
sketch.ctx
"""