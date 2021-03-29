import cairo
from numpy import array
from numpy import pi, sin, cos
from .interp import remap


class Sketch:
    def __init__(self, w, h, clear_color, range):
        self.w = w
        self.h = h
        self.clear_color = clear_color
        self.range = range
        self.__setup_defaults()
        self.__init_cairo()

    def __setup_defaults(self):
        # layer texture: [[rgba]]
        self.layer_in = None
        self.layer_in_stride = -1

        # step: Int [0 - 1024]
        self.step = 0

        # general params: [0, 1]
        self.param_a = 0
        self.param_b = 0
        self.param_c = 0
        self.param_d = 0

        # option toggles: Bool
        self.option_a = False
        self.option_b = False
        self.option_c = False
        self.option_d = False

        # colors: rgba
        self.color_a = [1, 1, 1, 1]
        self.color_b = [1, 0, 1, 1]
        self.color_c = [1, 1, 0, 1]
        self.color_d = [0, 1, 1, 1]

        # random seed: Int
        # TODO: import from AE
        self.random_seed = 0

        # TODO: AE can pass in points

    def randomize_params(self):
        import random

        self.param_a = random.uniform(0, 1)
        self.param_b = random.uniform(0, 1)
        self.param_c = random.uniform(0, 1)
        self.param_d = random.uniform(0, 1)

        print("Params:", self.param_a, self.param_b, self.param_c, self.param_d)

    def set_layer_in_data(self, memview, stride):
        """
        stored as flat array [[rgba]]
        stride allows array to be indexed by (x, y) coords
        """
        self.layer_in = memview
        self.layer_in_stride = stride

    def set_step(self, step):
        """
        Used for algorithms that require feedback
        """
        self.step = step

    def set_params(self, a, b, c, d):
        """
        AE Float sliders are in range [0, 1]
        """
        self.param_a = a
        self.param_b = b
        self.param_c = c
        self.param_d = d

    def set_options(self, a, b, c, d):
        """
        option toggles
        """
        self.option_a = a
        self.option_b = b
        self.option_c = c
        self.option_d = d

    def set_colors(self, a, b, c, d):
        """
        AE passes us a PF_Pixel struct (ARGB)
        """
        self.color_a = [a[1] / 255, a[2] / 255, a[3] / 255, a[0] / 255]
        self.color_b = [b[1] / 255, b[2] / 255, b[3] / 255, b[0] / 255]
        self.color_c = [c[1] / 255, c[2] / 255, c[3] / 255, c[0] / 255]
        self.color_d = [d[1] / 255, d[2] / 255, d[3] / 255, d[0] / 255]

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        ctx = cairo.Context(sur)

        self.sur = sur
        self.ctx = ctx

        self.__clear_canvas()

        if self.range != None:
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

            # print("scale w", self.w, "h", self.h, "small_size", small_side)

            xscale = small_side / (d1 - d0)
            yscale = small_side / (d1 - d0)

            # print("xscale", xscale, "yscale", yscale)

            ctx.translate(xoff, -yoff)
            ctx.scale(xscale, -yscale)
            ctx.translate(-d0, -d1)

            # print("xoff", xoff, "yoff", yoff, "d0", d0, "d1", d1)
            self.min_x = ((0 - xoff) / xscale) + d0
            self.max_x = ((self.w - xoff) / xscale) + d0
            self.min_y = ((0 - yoff) / yscale) + d0
            self.max_y = ((self.h - yoff) / yscale) + d0

            # update line width
            self.one = 1.0 / xscale
            ctx.set_line_width(self.one)
        else:
            self.one = 1.0

    def __clear_canvas(self):
        ctx = self.ctx
        ctx.set_source_rgba(*self.clear_color)
        ctx.rectangle(0, 0, self.w, self.h)
        ctx.fill()

    def update_canvas(self, w, h):
        if self.w == w and self.h == h:
            return
        self.w = w
        self.h = h
        self.__init_cairo()

    def sample_layer_in(self, xy):
        """
        returns color data in RGBA format
        """
        x, y = xy
        nx = remap(self.min_x, self.max_x, 0, self.w, x)
        ny = remap(self.min_y, self.max_y, 0, self.h, y)
        nx = int(min(max(nx, 0), self.w - 1))
        ny = int(min(max(ny, 0), self.h - 1))
        idx = ny * self.layer_in_stride + nx * 4
        return [
            self.layer_in[idx + 1] / 255.0,
            self.layer_in[idx + 2] / 255.0,
            self.layer_in[idx + 3] / 255.0,
            self.layer_in[idx] / 255.0,
        ]

    def luminosity_at(self, xy):
        samp = self.sample_layer_in(xy)
        # convert to grayscale luminosity
        return (samp[0:3] * array([0.21, 0.72, 0.07])).sum()

    def vector_at(self, xy, mult=2):
        """
        Samples incoming layer data and converts to vector
        """
        samp = self.sample_layer_in(xy)
        # convert to grayscale luminosity
        val = mult * pi * (samp[0:3] * array([0.21, 0.72, 0.07])).sum()
        # use val as angle for vector
        return array((sin(val), cos(val)))

    def draw(self):
        # TODO: implement in child
        pass

    def render(self):
        self.__clear_canvas()
        self.ctx.save()
        self.draw()
        self.ctx.restore()
        return self.sur.get_data()

    def set_color(self, c):
        self.ctx.set_source_rgba(*c)

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