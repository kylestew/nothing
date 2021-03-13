def random_points_in_circle(n, xx, yy, rr):
    """
    get n random points in a circle.
    """
    from numpy import pi
    from numpy import array
    from numpy import zeros, logical_not
    from numpy import column_stack
    from numpy import sin, cos
    from numpy.random import random

    theta = 2.0 * pi * random(n)
    u = random(n) + random(n)
    rad = zeros(n, "float")
    mask = u > 1.0
    xmask = logical_not(mask)
    rad[mask] = 2.0 - u[mask]
    rad[xmask] = u[xmask]
    xyp = column_stack((rr * rad * cos(theta), rr * rad * sin(theta)))
    return xyp + array([xx, yy])


def darts(n, xx, yy, rr, dst):
    """
    get at most n random, uniformly distributed, points in a circle.
    centered at (xx, yy), with radius rr. points are no closer to
    each other than dst.
    """
    from scipy.spatial import distance
    from numpy import array

    cdist = distance.cdist

    dartsxy = random_points_in_circle(n, xx, yy, rr)

    jj = []

    # collect indices that are too close to other indices
    dists = cdist(dartsxy, dartsxy, "euclidean")
    for j in range(n - 1):
        if all(dists[j, j + 1 :] > dst):
            jj.append(j)

    return dartsxy[array(jj, "int"), :]


import cairo

from numpy import column_stack, pi
from numpy import sin
from numpy import cos
from numpy.random import random


class Render:
    """
    Creates a standardized drawing canvas with domain and range of [0,1]
    """

    def __init__(self, n, back, front):
        self.n = n
        self.front = front
        self.back = back
        # size of one pixel
        self.pix = 1.0 / float(n)

        self.__init_cairo()

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.n, self.n)
        ctx = cairo.Context(sur)

        self.sur = sur
        self.ctx = ctx

        self.domain = [0, self.n]
        self.range = [0, self.n]

        self.remap([0, 1], [0, 1])
        self.clear_canvas()

    def remap(self, domain=(0, 1), range=(0, 1)):
        ctx = self.ctx
        d0, d1 = self.domain
        r0, r1 = self.range

        td0, td1 = domain
        tr0, tr1 = range

        xscale = (d1 - d0) / (td1 - td0)
        yscale = (r1 - r0) / (tr1 - tr0)

        ctx.scale(xscale, yscale)
        ctx.translate(-td0, -tr0)  # TODO: only works once

        self.domain = domain
        self.range = range

    def clear_canvas(self):
        ctx = self.ctx

        ctx.set_source_rgba(*self.back)
        ctx.rectangle(0, 0, 1, 1)
        ctx.fill()
        ctx.set_source_rgba(*self.front)

    def write_to_png(self, fn):
        self.sur.write_to_png("output.png")

    def set_front(self, c):
        self.front = c
        self.ctx.set_source_rgba(*c)

    def set_back(self, c):
        self.back = c

    def set_operator(self, op):
        self.ctx.set_operator(op)

    def set_line_width(self, w):
        self.line_width = w
        self.ctx.set_line_width(w)

    def line(self, x1, y1, x2, y2):
        ctx = self.ctx
        ctx.move_to(x1, y1)
        ctx.line_to(x2, y2)
        ctx.stroke()

    def path(self, xy, closed=False, fill=False):
        ctx = self.ctx
        ctx.move_to(*xy[0, :])
        for p in xy:
            ctx.line_to(*p)
        if closed:
            ctx.close_path()
        if fill:
            ctx.fill()
        else:
            ctx.stroke()

    def circle(self, x, y, r, fill=False):
        ctx = self.ctx
        ctx.arc(x, y, r, 0, pi * 2)
        if fill:
            ctx.fill()
        else:
            ctx.stroke()

    def rect(self, x, y, w, h, fill=False):
        ctx = self.ctx
        ctx.rectangle(x, y, w, h)
        if fill:
            ctx.fill()
        else:
            ctx.stroke()

    def random_circle(self, x, y, r, grains):
        """
        random points in circle. nonuniform distribution.
        """
        pix = self.pix
        rectangle = self.ctx.rectangle
        fill = self.ctx.fill

        # random angles and radii
        theta = random(grains) * pi * 2
        radius = random(grains) * r

        xx = x + cos(theta) * radius
        yy = y + sin(theta) * radius

        for x, y in zip(xx, yy):
            rectangle(x, y, pix, pix)
            fill()

    def random_uniform_circle(self, x, y, r, grains, dst=0):
        """
        random points in circle. uniform distribution.
        """
        pix = self.pix
        rectangle = self.ctx.rectangle
        fill = self.ctx.fill

        for x, y in darts(grains, x, y, r, dst):
            rectangle(x, y, pix, pix)
            fill()

    def dot(self, x, y):
        ctx = self.ctx
        pix = self.pix
        ctx.rectangle(x, y, pix, pix)
        ctx.fill()

    def sandstroke(self, xys, grains=10):
        # TODO: does this work?
        pix = self.pix
        rectangle = self.ctx.rectangle
        fill = self.ctx.fill

        dx = xys[:, 2] - xys[:, 0]
        dy = xys[:, 3] - xys[:, 1]

        return dx
