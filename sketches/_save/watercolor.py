#%%
# for each pair of points, find midpoint
from geom.polygon import Polygon
from numpy import array
from numpy import take
from numpy.random import normal

def mutate_poly(poly, std_dev):
    newpts = []
    for i in range(0, len(poly.points) * 2, 2):
        a = list(take(poly.points, [i, i+1]))
        c = list(take(poly.points, [i+2, i+3], mode='wrap'))
        mid_x = (a[0] + c[0]) / 2
        mid_y =(a[1] + c[1]) / 2
        b = [mid_x, mid_y]
        b = normal(b, std_dev)
        # print(b)

        newpts.append(a)
        newpts.append(b)
        newpts.append(c)

    return Polygon(array(newpts))

#%%

polys = []
for j in range(3):
    base = Polygon.ngon(10, r=0.8)
    for k in range(4):
        base = mutate_poly(base, 0.04)
        
    for i in range(30):
        p = base
        for k in range(3):
            p = mutate_poly(p, 0.03)
        polys.append(p)
        print(len(polys))
    
%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 900
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#f9f8f4")
FOREGROUND = hex_to_rgba("#ec363603")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(-1, 1), range=(-1, 1))
# render.set_line_width(4.0 * PIXEL)

# render poly
for poly in polys:
    render.path(poly.points, closed=True, fill=True)

# display vertices
# render.set_front([0, 0, 0, 1])
# for pt in p.points:
    # render.circle(pt[05], pt[1], 0.01, fill=True)
        
# render.set_front([0, 1, 1, 1])
# for pt in mpoints:
    # render.circle(pt[0], pt[1], 0.01, fill=True)

render.ctx