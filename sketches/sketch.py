import cairo
from numpy import pi


class Sketch:
    def __init__(self, w, h, range, back, front):
        self.w = w
        self.h = h
        self.back = back
        self.front = front
        self.range = range

        self.__init_cairo()

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        ctx = cairo.Context(sur)

        self.sur = sur
        self.ctx = ctx

        # scale cairo to fit range
        # crop to fit (not fill)
        d0, d1 = self.range
        small_side = 0
        xoff = 0
        yoff = 0
        if self.w > self.h:
            small_side = self.h
            xoff = (self.w - self.h) / 2
        else:
            small_side = self.w
            yoff = (self.h - self.w) / 2

        xscale = small_side / (d1 - d0)
        yscale = small_side / (d1 - d0)
        print(self.w, self.h, xscale, yscale, xoff, yoff)

        # ctx.translate(-d0 * xscale - xoff, -d0 * yscale - yoff)
        ctx.translate(xoff, -yoff)
        ctx.scale(xscale, -yscale)
        ctx.translate(-d0, -d1)

        # update line width
        self.one = 1.0 / xscale
        ctx.set_line_width(self.one)

        self.__clear_canvas()

    def __clear_canvas(self):
        ctx = self.ctx

        ctx.set_source_rgba(*self.back)
        ctx.rectangle(0, 0, self.w, self.h)
        ctx.fill()
        ctx.set_source_rgba(*self.front)

    def update_canvas(self, w, h):
        if self.w == w and self.h == h:
            return
        self.w = w
        self.h = h
        self.__init_cairo()

    def set_params(self, parmA, parmB):
        self.parmA = parmA
        self.parmB = parmB

    def draw(self):
        # TODO: implement in child
        pass

    def render(self):
        self.__clear_canvas()
        self.ctx.save()
        self.draw()
        self.ctx.restore()
        return self.sur.get_data()

    def set_front(self, c):
        self.front = c
        self.ctx.set_source_rgba(*c)

    def set_back(self, c):
        self.back = c

    def set_operator(self, op):
        self.ctx.set_operator(op)

    def set_line_width(self, width):
        self.ctx.set_line_width(self.one * width)

    def line(self, a, b):
        ctx = self.ctx
        ctx.move_to(a[0], a[1])
        ctx.line_to(b[0], b[1])
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

    def circle(self, xy, r, fill=False):
        """
        xy : (float, float)
            point (x, y)
        r : float
            radius of circle
        fill : bool, optional
            stroke or fill circle (default stroke)
        """
        ctx = self.ctx
        x, y = xy
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