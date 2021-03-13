#%%

from numpy import column_stack
from numpy import linspace
from numpy import sin, cos
from numpy import pi
from geom.api.shape import PCLike


class Polygon(PCLike):
    def __init__(self, pts):
        super().__init__(pts)

    # regular polygon of n-sides
    @classmethod
    def ngon(cls, n, x=0, y=0, r=1):
        a = linspace(0, pi * 2, n, endpoint=False)
        pts = (x, y) + column_stack((cos(a), sin(a))) * r
        return cls(pts)

    # def area(self):
    # pass


# def bounds(self):
# return Rect(self.x, self.y, 2 * self.r, 2 * self.r)

p = Polygon(5)
p.points
