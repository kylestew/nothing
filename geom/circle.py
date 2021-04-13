from .polygon import Polygon
from numpy import array, linspace
from numpy import column_stack
from numpy import pi, sin, cos
from .rect import Rect
from .api.samples import DEFAULT_SAMPLES


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.origin = array((x, y))
        self.r = r

    # === Ops ===
    def area(self):
        pass

    def as_polygon(self, n=DEFAULT_SAMPLES):
        return Polygon(self.vertices(n))

    def bounds(self):
        x, y = self.origin
        return Rect(x, y, 2 * self.r, 2 * self.r)

    def center(self):
        return self.origin

    # edges: NO IMPL

    # def resample(self, dist=None, num=None):
    # return Polygon(resample(self.vertices(), dist, num))

    # def tessellate()

    def translate(self, tx, ty):
        pass

    def rotate(self, rad):
        # how do you rotate a circle?
        pass

    def scale(self, sx, sy):
        pass

    def vertices(self, n=DEFAULT_SAMPLES):
        a = linspace(0, pi * 2, n + 1)
        circ = self.origin + column_stack((cos(a), sin(a))) * self.r
        return circ[:-1]

    # === Cairo ===
    def draw(self, ctx, fill=False):
        x, y = self.origin
        ctx.circle(x, y, self.r)
