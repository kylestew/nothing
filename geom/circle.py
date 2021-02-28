from numpy import linspace
from numpy import column_stack
from numpy import pi
from numpy import sin, cos
from .rect import Rect


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        pass

    def bounds(self):
        return Rect(self.x, self.y, 2 * self.r, 2 * self.r)

    def to_points(self, n):
        a = linspace(0, pi * 2, n + 1)
        circ = (self.x, self.y) + column_stack((cos(a), sin(a))) * self.r
        return circ[:-1]
