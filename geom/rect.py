class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def center(self):
        return self.x + self.w / 2.0, self.y + self.h / 2.0

    def bounds(self):
        self

    def to_points(self):
        p = (self.x, self.y)
        q = (p[0] + self.w, p[1] + self.h)
        return [p, (q[0], p[1]), q, (p[0], q[1])]
