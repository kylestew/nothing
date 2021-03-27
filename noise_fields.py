#%%
from lib.sketch import Sketch
from lib.interp import remap, lerp
from lib.field import Perlin3DField
from numpy import array
from numpy import linspace
from numpy import sin, cos


class NoiseField(Sketch):
    """
    https://sighack.com/post/getting-creative-with-perlin-noise-fields
    "actively practice creativity using self-imposed constraints"
    """

    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        range = [-1, 1]
        super().__init__(w, h, clear_color, range)
        self.setup_field()

    def setup_field(self):
        # setup perlin field sampling function
        # TODO:
        # - types of noise
        # - noise settings
        shape = (12, 12, 12)
        res = (3, 3, 3)
        self.field = Perlin3DField(shape, res)
        self.dims = [(-1.2, 1.2), (-1.2, 1.2), (-1.2, 1.2)]
        self.fn = self.field.fn(self.dims)

    def draw(self):
        z = remap(0, 1, -1, 1, self.step)
        # print("step - z", z)

        def marker(x, y, theta, base=False):
            a = array((x, y))
            b = a + (sin(theta) * 0.04, cos(theta) * 0.04)
            if base:
                self.circle(a, 0.01)
            self.line(a, b)

        # DEBUG: underlying field points (not interpolated)
        self.set_line_width(1)
        self.set_color(self.color_b)
        d0, d1, _ = self.dims
        r0, r1, r2 = self.field.shape
        k = round(self.step * (r2 - 1))
        # print("k", k)
        j = 0
        for y in linspace(d1[0], d1[1], r1):
            i = 0
            for x in linspace(d0[0], d0[1], r0):
                theta = self.field.field[i, j, k]
                marker(x, y, theta, base=True)
                i += 1
            j += 1

        # DEBUG: display flow field (interpolated points)
        self.set_line_width(1.0)
        self.set_color(self.color_a)
        display_density = r0 * 4
        for y in linspace(self.min_y, self.max_y, display_density):
            for x in linspace(self.min_x, self.max_x, display_density):
                theta = self.fn(x, y, z)
                marker(x, y, theta)


"""

width, height = 900, 900
sketch = NoiseField(width, height)

step = 0
sketch.set_step(step)

# sketch.set_params(count, smoothness, amp, weight)
# ARGB
sketch.set_colors(
    [0xFF, 0xFF, 0xFF, 0xFF],
    [0xFF, 0xFF, 0x00, 0xFF],
    [0xFF, 0xFF, 0x00, 0x00],
    [0xFF, 0xFF, 0x00, 0x00],
)

# drop point on field and let it wander
# steps = 0
# speed = 0.025
# path = empty([steps, 2])
# path[0] = [0, 0]
# for i in range(1, steps):
# last position
# x, y = path[i - 1]
# theta = sketch.f(x, y)
# new position
# nx = x + sin(theta) * speed
# ny = y + cos(theta) * speed
# path[i] = [nx, ny]

sketch.render()
# sketch.set_color([0, 1, 1, 1])
# sketch.path(path)

%load_ext helpers.ipython_cairo
sketch.ctx
"""