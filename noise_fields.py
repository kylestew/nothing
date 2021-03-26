#%%
from numpy.random import sample
from lib.sketch import Sketch
# from numpy import linspace, column_stack
from numpy import array, meshgrid
from scipy import interpolate
from numpy import linspace
from numpy import sin, cos, pi
from numpy import random

class NoiseField(Sketch):
    """
    https://sighack.com/post/getting-creative-with-perlin-noise-fields
    "actively practice creativity using self-imposed constraints"
    """

    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        range = [-1, 1]
        super().__init__(w, h, clear_color, range)

    def draw(self):
        # normalize params
        # step = self.step
        # count = lerp(1, 128, self.param_a)
        # smoothness = lerp(4, 64, 1.0 - self.param_b)
        # amp = lerp(0.01, 1.0, self.param_c)
        # weight = lerp(0.5, 20.0, self.param_d)

        from perlin import generate_perlin_noise_2d
        random.seed(5)
        density = 64
        noise = generate_perlin_noise_2d((density, density), (8, 8))
        field = noise * pi

        domain = [-1.2, 1.2]
        xs = linspace(domain[0], domain[1], density)
        ys = linspace(domain[0], domain[1], density)
        # def f(x, y):
            # return x * 2*y
        # z = 2 * xx * 3 * yy
        f = interpolate.interp2d(xs, ys, field, kind='cubic')
        
        # display field
        self.set_line_width(1.0)
        self.set_color(self.color_a)
        display_density = density * 4
        for y in linspace(-1, 1, display_density):
            for x in linspace(-1, 1, display_density):
                theta = f(x, y)[0]
                a = array((x, y))
                b = a + (sin(theta) * 0.03, cos(theta) * 0.03)
                self.line(a, b)

        # DEBUG: underlying field
        self.set_line_width(1)
        self.set_color(self.color_b)
        for y in ys:
            for x in xs:
                # print(xs, ys)
                theta = f(x, y)[0]
                # print(theta)
                a = array((x, y))
                b = a + (sin(theta) * 0.05, cos(theta) * 0.05)
                # self.circle(a, 0.01)
                # self.line(a, b)

width, height = 1200, 1200
sketch = NoiseField(width, height)

# step = 10
# sketch.set_step(step)

# count = 0.5
# smoothness = 0.65
# amp = 0.33
# weight = 0.250
# sketch.set_params(count, smoothness, amp, weight)

# func_a = True
# func_b = False
# func_c = False
# func_d = False
# sketch.set_options(func_a, func_b, func_c, func_d)

# ARGB
sketch.set_colors(
    [0xAA, 0xFF, 0xCC, 0xCC],
    [0xFF, 0xFF, 0x00, 0xFF],
    [0xFF, 0xFF, 0x00, 0x00],
    [0xFF, 0xFF, 0x00, 0x00],
    )

%load_ext helpers.ipython_cairo
d = sketch.render()
sketch.ctx