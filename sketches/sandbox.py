#%%
# from .sketch import Sketch
from sketch import Sketch


class Sandbox(Sketch):
    def __init__(self, w, h):
        back = [0, 0, 0, 0]
        front = [1, 0, 1]
        super().__init__(w, h, back, front)

    def draw(self):
        # self.ctx.set_front([0, 1, 1])
        self.ctx.rectangle(0, 0, 200, 200)
        self.ctx.fill()
        # self.ctx.set_front([0, 1, 0, 1])
        # render.circle((0.5, 0.5), 0.25, fill=True)


%load_ext ipython_cairo

sketch = Sandbox(1920, 1080)
d = sketch.render()

sketch.ctx