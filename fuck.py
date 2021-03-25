#%%
from lib.sketch import Sketch
from geom.circle import Circle
from numpy import array


class FuckYou(Sketch):
    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        range = None
        super().__init__(w, h, clear_color, range)

    def draw(self):
        circ = Circle(self.w/2, self.h/2, self.w * 0.4)
        
        verts = circ.vertices(35)
        
        lines = []
        for v0 in verts[1::3]:
            for v1 in verts[1::2]:
                lines.append([v0, v1])

        self.set_color([1, 1, 1, 0.6])
        self.set_line_width(1.5)
        for line in lines:
            self.line(line[0], line[1])

%load_ext helpers.ipython_cairo
sketch = FuckYou(640, 640)
# sketch.set_layer_in_data(view, width * depth)
sketch.render()
sketch.ctx