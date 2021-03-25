from geom.api.shape import PCLike
from .internal.resample import resample
from numpy import array


class Line(PCLike):
    def __init__(self, a, b):
        super().__init__([a, b])

    def resample(self, dist=None, num=None):
        # TODO: does this become a polyline?
        return array(resample(self.vertices(), dist, num, closed=False))

    def vertices(self):
        return self.points


"""
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

"""