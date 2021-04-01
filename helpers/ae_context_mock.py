import cairo
from numpy import pi


def _setup(w, h):
    global _w, _h, _sur, _ctx
    _w = w
    _h = h
    _sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, _w, _h)
    _ctx = cairo.Context(_sur)


def clear(c):
    _ctx.set_source_rgba(*c)
    _ctx.rectangle(0, 0, _w, _h)
    _ctx.fill()


def get_canvas_size():
    return (_w, _h)


def sample_point(x, y):
    pass


def set_color(c):
    _ctx.set_source_rgba(*c)


def set_operator(op):
    _ctx.set_operator(op)


def set_line_width(width):
    _ctx.set_line_width(width)


def set_line_cap(opt):
    # TODO: may need to convert int to symbol
    _ctx.set_line_cap(opt)


def line(a, b):
    _ctx.move_to(a[0], a[1])
    _ctx.line_to(b[0], b[1])
    _ctx.stroke()


def rect(x, y, w, h, fill=False):
    _ctx.rectangle(x, y, w, h)
    if fill:
        _ctx.fill()
    else:
        _ctx.stroke()


def circle(x, y, r, fill=False):
    _ctx.arc(x, y, r, 0, 2 * pi)
    if fill:
        _ctx.fill()
    else:
        _ctx.stroke()


def path(xy, closed=False, fill=False):
    from numpy import array

    xys = array(xy)
    _ctx.move_to(*xys[0, :])
    for p in xys:
        _ctx.line_to(*p)
    if fill:
        _ctx.fill()
    else:
        _ctx.stroke()


_setup(256, 256)