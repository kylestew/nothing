from .resample.resample import resample
from .polygon import Polygon


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def as_polygon(self):
        return Polygon(self.vertices())

    def bounds(self):
        self

    def center(self):
        return self.x + self.w / 2.0, self.y + self.h / 2.0

    def edges(self):
        pass

    def resample(self, dist=None, num=None):
        poly = self.as_polygon()
        return Polygon(resample(poly.points, dist, num))

    def transform(self):
        pass

    def vertices(self):
        p = (self.x, self.y)
        q = (p[0] + self.w, p[1] + self.h)
        return [p, (q[0], p[1]), q, (p[0], q[1])]
