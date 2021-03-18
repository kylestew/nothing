from .rect import Rect
from numpy import linspace


class Grid:
    def __init__(self, w, h, rows, cols, padding=0):
        self._w = w
        self._h = h
        self._rows = rows
        self._cols = cols

        # store the grid cells as rects
        cw = (w - padding * (cols + 1)) / cols
        ch = (h - padding * (rows + 1)) / rows
        xs = linspace(0 + padding, w, cols, endpoint=False)
        ys = linspace(0 + padding, h, rows, endpoint=False)

        rects = []
        for y in ys:
            for x in xs:
                r = Rect(x, y, cw, ch)
                rects.append(r)

        self._cells = rects

    def area(self):
        return self._w * self._h

    def centers(self):
        return list(map(lambda rect: rect.center(), self._cells))

    def cells(self):
        return self._cells
