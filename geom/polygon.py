from numpy import column_stack
from numpy import linspace
from numpy import sin, cos
from numpy import pi
from geom.api.shape import PCLike
from .internal.resample import resample


class Polygon(PCLike):
    def __init__(self, pts):
        super().__init__(pts)

    # regular polygon of n-sides
    @classmethod
    def ngon(cls, n, x=0, y=0, r=1):
        a = linspace(0, pi * 2, n, endpoint=False)
        pts = (x, y) + column_stack((cos(a), sin(a))) * r
        return cls(pts)

    def center(self):
        pass

    def resample(self, dist=None, num=None):
        return Polygon(resample(self.points, dist, num))

    def vertices(self):
        return self.points