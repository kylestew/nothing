#%%
from .sketch import Sketch

# from sketch import Sketch


class Sandbox(Sketch):
    def __init__(self, w, h):
        back = [0, 0, 0, 0]
        front = [1, 0, 1]
        range = [-1, 1]
        super().__init__(w, h, range, back, front)

    def draw(self):
        # self.set_front([1, 0, 1])
        self.circle((0, 0), self.parmA, fill=True)
        # self.circle((-1., -1.), 0.25, fill=True)
        # self.circle((1., 1.), 0.25, fill=True)
        # self.line((-1, 1), (1, -1))
        # self.set_line_width(4)
        # self.line((0, -1), (-1, 1))


# %load_ext ipython_cairo
# sketch = Sandbox(1920, 1080)
# sketch.set_params(0.85, 0.25)
# d = sketch.render()
# sketch.ctx