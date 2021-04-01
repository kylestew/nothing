#%%
from cairo import LINE_CAP_ROUND
from lib.sketch import Sketch
from lib.interp import lerp
from geom.grid import Grid
from numpy import array, empty
from numpy import linspace
from numpy import sin, cos, pi


class NoiseField(Sketch):
    """
    https://sighack.com/post/getting-creative-with-perlin-noise-fields
    "actively practice creativity using self-imposed constraints"
    """

    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        range = [0, 1]
        super().__init__(w, h, clear_color, range)

    def draw(self):
        steps = int(lerp(1, 1024, self.step))
        x_density = int(lerp(self.w / 256, self.w / 4, self.param_a))
        y_density = int(lerp(self.h / 256, self.h / 4, self.param_a))
        padding = lerp(0, 0.75, self.param_b)
        line_width = lerp(0.1, 8.0, self.param_c)
        conv = lerp(1.0, 8.0, self.param_d)

        # set wanderer starting positions
        grid = Grid(0, 0, 1, 1, 12, 12, padding=padding)
        starts = grid.centers()

        # wander points through field
        speed = 0.0005
        paths = []
        for start in starts:
            path = empty([steps, 2])
            path[0] = start
            for i in range(1, steps):
                # last position
                x, y = path[i - 1]
                vec = self.vector_at((x, y), mult=conv)
                # new position
                nx = x + vec[0] * speed
                ny = y + vec[1] * speed
                path[i] = [nx, ny]
            paths.append(path)

        # DEBUG: display flow field (interpolated points)
        if self.option_d:
            self.set_color(self.color_d)
            rad = (self.max_x - self.min_x) / x_density / 3
            for y in linspace(self.min_y, self.max_y, x_density):
                for x in linspace(self.min_x, self.max_x, y_density):
                    vec = self.vector_at((x, y))
                    a = array((x, y))
                    b = a + vec * 0.1
                    self.set_color(self.sample_layer_in((x, y)))
                    self.circle(a, rad, fill=True)

            self.set_line_width(60 / x_density)
            self.set_color([1, 1, 1, 1])
            for y in linspace(self.min_y, self.max_y, x_density):
                for x in linspace(self.min_x, self.max_x, y_density):
                    vec = self.vector_at((x, y))
                    a = array((x, y))
                    b = a + vec * 0.1
                    self.line(a, b)

        # draw wandering paths
        self.set_color(self.color_a)
        self.ctx.set_line_cap(LINE_CAP_ROUND)
        self.set_line_width(line_width)
        for path in paths:
            self.path(path)


"""
# load sample image (once, static)
from helpers.img_samp import Sampler

width, height, depth, view = Sampler("helpers/perlin-noise.png").load_image()
sketch = NoiseField(width, height)
sketch.set_layer_in_data(view, width * depth)

sketch.set_step(0.3)
# density, padding, line width, ???
sketch.set_params(0.2, 0.3, 0.1, 0.0)
sketch.set_options(False, False, False, False)

sketch.render()
%load_ext helpers.ipython_cairo
sketch.ctx
"""