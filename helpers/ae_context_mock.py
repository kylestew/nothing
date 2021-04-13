import cairo
from numpy import pi


def _setup(w, h):
    global _w, _h, _sur, _ctx
    _w = w
    _h = h
    _one = 1.0
    _sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, _w, _h)
    _ctx = cairo.Context(_sur)


def set_range(r0, r1):
    global _min_x, _max_x, _min_y, _max_y, _one

    small_side = 0
    xoff = 0
    yoff = 0
    if _w > _h:
        small_side = _h
        xoff = (_w - _h) / 2
    else:
        small_side = _w
        yoff = (_h - _w) / 2

    xscale = small_side / (r1 - r0)
    yscale = small_side / (r1 - r0)

    _ctx.translate(xoff, -yoff)
    _ctx.scale(xscale, -yscale)
    _ctx.translate(-r0, -r1)

    _min_x = ((0 - xoff) / xscale) + r0
    _max_x = ((_w - xoff) / xscale) + r0
    _min_y = ((0 - yoff) / yscale) + r0
    _max_y = ((_h - yoff) / yscale) + r0

    _one = 1.0 / xscale


def clear(c):
    _ctx.set_source_rgba(*c)
    _ctx.rectangle(0, 0, _w, _h)
    _ctx.fill()


def get_canvas_size():
    return (_w, _h)


def sample_point(x, y):
    # TODO: actual image sampling
    from numpy.random import rand

    return rand(4)


def set_color(c):
    _ctx.set_source_rgba(*c)


def set_operator(op):
    _ctx.set_operator(op)


def set_line_width(width):
    _ctx.set_line_width(_one * width)


def set_line_cap(opt):
    # TODO: may need to convert int to symbol
    _ctx.set_line_cap(opt)
    _ctx.set_line_join(opt)


def line(x0, y0, x1, y1):
    _ctx.move_to(x0, y0)
    _ctx.line_to(x1, y1)
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

    if closed:
        _ctx.close_path()
    if fill:
        _ctx.fill()
    else:
        _ctx.stroke()


def arc(cx, cy, r, start, end, fill=False, closed=False):
    _ctx.arc(cx, cy, r, start, end)

    if closed:
        _ctx.close_path()
    if fill:
        _ctx.fill()
    else:
        _ctx.stroke()


_setup(256, 256)