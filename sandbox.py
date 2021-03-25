#%%
from lib.sketch import Sketch
from lib.interp import lerp
from numpy import linspace, column_stack


class Sandbox(Sketch):
    """
    Samples the incoming texture data and draws waveforms based
    on the luminosity of the underlying pixels.
    """

    def __init__(self, w, h):
        clear_color = [0, 0, 0, 1]
        range = [0, 1]
        super().__init__(w, h, clear_color, range)
        
    def draw(self):
        # constants

        # normalize params
        # step = self.step
        count = lerp(1, 128, self.param_a)
        smoothness = lerp(4, 64, 1.0 - self.param_b)
        amp = lerp(0.05, 2.0, self.param_c)
        weight = lerp(0.5, 20.0, self.param_d)

        # apply params
        self.set_color(self.color_a)
        self.set_line_width(weight)
        
        # generate noise lines
        xs = linspace(self.min_x, self.max_x, int(smoothness), endpoint=True)
        polylines = []
        for y in linspace(0, 1, int(count)):
            # sample xys at low resolution
            f = lambda x: y + amp * (self.luminosity_at((x, y)) - 0.5)
            ys = list(map(f, xs))
            
            # generate function interpolating values
            from scipy.interpolate import interp1d
            fi = interp1d(xs, ys, kind='cubic')
            # fi = interp1d(xs, ys)
            
            # graph using interpolated function (instead of direct reading)
            x = linspace(self.min_x, self.max_x, int(self.w / 2))
            y = fi(x)

            polyline = column_stack((x, y))
            polylines.append(polyline)

        for polyline in polylines:
            self.path(polyline)
            # for pt in polyline:
                # self.circle(pt, 0.001)


# load sample image (once, static)
from helpers.img_samp import Sampler
width, height, depth, view = Sampler("helpers/grad.png").load_image()

sketch = Sandbox(width, height)
sketch.set_layer_in_data(view, width * depth)

# step = 10
# sketch.set_step(step)

count = 0.5
smoothness = 0.65
amp = 0.33
weight = 0.25
sketch.set_params(count, smoothness, amp, weight)

# func_a = True
# func_b = False
# func_c = False
# func_d = False
# sketch.set_options(func_a, func_b, func_c, func_d)

# ARGB
sketch.set_colors(
    [0xFF, 0xFF, 0xFF, 0xFF],
    [0xFF, 0xFF, 0x00, 0xFF],
    [0xFF, 0xFF, 0x00, 0x00],
    [0xFF, 0xFF, 0x00, 0x00],
    )

d = sketch.render()

%load_ext helpers.ipython_cairo
sketch.ctx