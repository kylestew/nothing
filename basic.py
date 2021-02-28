#%%
%load_ext ipython_cairo

#%%
"""
from scipy.interpolate import splprep
from scipy.interpolate import splev

pts = Circle(r=0.3).to_points(12)
pts
xs = pts[:,0]
ys = pts[:,1]
tck, u = splprep([xs, ys], s=0)
coeffs = tck[1]
print("knots:", tck[0])
print("coeffs:", tck[1])
print("degree", tck[2])
u
"""

#%%
from numpy import column_stack, pi
from numpy import linspace
from numpy import ones
from numpy import sin
from numpy import cos
from scipy.interpolate import splprep
from scipy.interpolate import splev
from geom.circle import Circle

TWOPI = 2 * pi
EDGE = 0.2
RAD = 0.5 - EDGE


class Sand:
    def __init__(self, size, inum=200):
        self.size = size
        self.one = 1.0 / size
        self.inum = inum

        self.itt = 0
        
        self.grains = 5

    def init(self, n=10, rad=RAD):
        # sweep _n_ points on a standard circle with radius _rad_
        self.xy = Circle(r=rad).to_points(n)

        # interpolate curve from basic circle points
        self.interpolated_xy = self._interpolate(self.xy, self.inum)
        
        # initialize empty noise array
        self.noise = ones((n, 1), 'float')
        
    def _interpolate(self, xy, num_points):
        """
        Take any input and interpolate it into a b-spline then convert back into points
        Used as a smoothing algo to keep results constant every iteration
        """
        # Find the B-spline representation of an N-D curve.
        # (t,c,k) - tuple containing the vector of knots, the B-spline coefficients, and the degree of the spline.
        # u - An array of the values of the parameter.
        xs = xy[:,0]
        ys = xy[:,1]
        tck, u = splprep([xs, ys], s=0)
        # we are remapping this spline to be _num_points_ output no matter the input
        unew = linspace(0, 1.0, num_points)
        # convert back to x,y coords
        out = splev(unew, tck)
        return column_stack(out)
    
    def draw(self, render):
        xy = self.interpolated_xy
        # chop first - make list, chop last - make list
        points = column_stack((xy[1:,:], xy[:-1,:]))
        return points
        # render.sandstroke(points, self.grains)


#%%
# TODO: Figure out WTF is happining here
def sandstroke(self,xys,grains=10):
    pix = self.pix
    rectangle = self.ctx.rectangle
    fill = self.ctx.fill

    dx = xys[:,2] - xys[:,0]
    dy = xys[:,3] - xys[:,1]

    aa = arctan2(dy,dx)
    directions = column_stack([cos(aa),sin(aa)])

    dd = sqrt(square(dx)+square(dy))

    for i,d in enumerate(dd):
      for x,y in xys[i,:2] + directions[i,:]*random((grains,1))*d:
        rectangle(x,y,pix,pix)
        fill()


#%%
from modules.render import Render

BACK = [1, 1, 1, 1]
FRONT = [1, 0, 0, 1]

size = 600

sand = Sand(size)
sand.init()

render = Render(size, BACK, FRONT)
render.set_line_width(sand.one)

bob = sand.draw(render)
bob[0]


# for pt in Circle(r=RAD).to_points(10):
    # x, y = pt
    # render.circle(x, y, .05, fill=True)
# render.set_front([0, 1, 0, 1])
# for pt in xys:
    # x, y = pt
    # render.circle(x, y, .01, fill=True)
# render.ctx

# %%
