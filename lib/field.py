from perlin_numpy.perlin2d import generate_fractal_noise_2d
from scipy import interpolate
from numpy import linspace
from numpy import pi
from numpy import random
from perlin_numpy import generate_perlin_noise_2d, generate_perlin_noise_3d
from scipy.interpolate.interpolate import RegularGridInterpolator


class Field:
    def __init__(self, field):
        self.field = field

    def fn(self, dims):
        """
        Creates an interpolation function on the field (treated as a regular grid in 2 or 3 dimensions)
        The grid is defined by the _dims_ parameter and effectively remaps the field
        dims - ([x_min, x_max], [y_min, y_max])
        """
        n = len(dims)
        if n == 2:
            d0, d1 = dims
            r0 = self.field.shape[0]
            r1 = self.field.shape[1]
            xs = linspace(d0[0], d0[1], r0)
            ys = linspace(d1[0], d1[1], r1)
            f = interpolate.interp2d(xs, ys, self.field, kind="cubic")

            def ret_fn(x, y):
                return f(x, y)[0]

            return ret_fn

        elif n == 3:
            d0, d1, d2 = dims
            r0, r1, r2 = self.field.shape
            xs = linspace(d0[0], d0[1], r0)
            ys = linspace(d1[0], d1[1], r1)
            zs = linspace(d2[0], d2[1], r2)
            f = RegularGridInterpolator(
                (xs, ys, zs), self.field, bounds_error=False, fill_value=0
            )

            def ret_fn(x, y, z):
                return f((x, y, z)).reshape(1)[0]

            return ret_fn

        raise ValueError("invalid dimensions")


class Perlin2DField(Field):
    def __init__(self, shape, res, seed=0):
        """
        + shape: shape of the generated array (tuple of 2 ints)
        + res: number of periods of noise to generate along each axis (tuple of 2 ints)
        + seed: rng seed (numpy)
        Note: shape must be a multiple of res
        """
        random.seed(seed)
        noise = generate_perlin_noise_2d(shape, res, (True, True))
        # [-1, 1] -> [-pi, pi]
        # field = noise * 2 * pi
        field = noise
        super().__init__(field)

        self.shape = shape
        self.res = res


class FractalNoise2DField(Field):
    def __init__(self, shape, res, seed=0):
        """
        + shape: shape of the generated array (tuple of 2 ints)
        + res: number of periods of noise to generate along each axis (tuple of 2 ints)
        + seed: rng seed (numpy)
        Note: shape must be a multiple of res
        """
        random.seed(seed)
        noise = generate_fractal_noise_2d(shape, res, 5)
        # , (True, True))
        # [-1, 1] -> [-pi, pi]
        # field = noise * 2 * pi
        field = noise
        super().__init__(field)

        self.shape = shape
        self.res = res


class Perlin3DField(Field):
    def __init__(self, shape, res, seed=0):
        """
        + shape: shape of the generated array (tuple of 3 ints)
        + res: number of periods of noise to generate along each axis (tuple of 3 ints)
        + seed: rng seed (numpy)
        Note: shape must be a multiple of res
        """
        random.seed(seed)
        field = generate_perlin_noise_3d(shape, res)
        super().__init__(field)

        self.shape = shape
        self.res = res
