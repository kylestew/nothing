import cairo


class Sketch:
    def __init__(self, w, h, back, front):
        print("init", w, h, back, front)

        self.w = w
        self.h = h
        self.back = back
        self.front = front

        # size of one pixel
        # self.pix = 1.0

        self.__init_cairo()

    def update_canvas(self, w, h):
        print("update_canvas", w, h)

        if self.w == w and self.h == h:
            return
        self.w = w
        self.h = h
        self.__init_cairo()

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        ctx = cairo.Context(sur)

        self.sur = sur
        self.ctx = ctx

        self.__clear_canvas()

    def __clear_canvas(self):
        ctx = self.ctx

        ctx.set_source_rgba(*self.back)
        ctx.rectangle(0, 0, self.w, self.h)
        ctx.fill()
        ctx.set_source_rgba(*self.front)

    def draw(self):
        # TODO: implement in child
        pass

    def render(self):
        self.__clear_canvas()

        # TODO: scale canvas
        self.ctx.save()
        # self.domain = [0, self.w]
        # self.range = [0, self.h]
        # self.remap([0, 1], [0, 1])

        self.draw()

        # restore
        self.ctx.restore()

        return self.sur.get_data()
