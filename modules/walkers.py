#%%
from numpy import linspace
from numpy import zeros
from numpy import column_stack
from numpy.random import random

from .perlin import generate_perlin_noise_2d

# from perlin import generate_perlin_noise_2d


class Walkers:
    def __init__(
        self,
        agent_count,
        xy_scale,
        pnoise_size=512,
        pnoise_res=4,
        pnoise_evol_rate=0.25,
    ):
        self.n = agent_count
        self.scale = xy_scale

        res = 2 ** pnoise_res
        self._pnoise = generate_perlin_noise_2d((pnoise_size, pnoise_size), (res, res))
        self._pnoise_size = pnoise_size
        self._pnoise_evolution = 0.0
        self._pnoise_evol_rate = pnoise_evol_rate

        x = linspace(0.0, 1.0, self.n)
        y = zeros(self.n, "float")
        self._walkers = column_stack((x, y))
        self._velocities = zeros((self.n, 2), "float")

    def report(self):
        for (walker, vel) in zip(self._walkers, self._velocities):
            print(walker, vel)

    def random(self):
        while True:
            # generate stack of X, Y random throws
            delta = (
                column_stack(
                    (
                        1.0 - 2.0 * random(self.n),
                        1.0 - 2.0 * random(self.n),
                    )
                )
                * self.scale
            )
            # add random throws to walker velocities
            self._velocities += delta
            # velocities update positions
            self._walkers += self._velocities
            # OPTION: cumulative sum adds x to y for ever agent - giving larger values at end of range
            # self._walkers += cumsum(self._velocities, axis=0)
            yield self._walkers

    def perlin(self):
        while True:
            x_noise = self._pnoise[
                linspace(0, self._pnoise_size - 1, self.n, dtype="int"),
                int(self._pnoise_evolution) % self._pnoise_size,
            ]
            y_noise = self._pnoise[int(self._pnoise_evolution) % self._pnoise_size][
                linspace(0, self._pnoise_size - 1, self.n, dtype="int")
            ]
            self._pnoise_evolution += self._pnoise_evolution
            # generate stack of X, Y random throws
            delta = (
                column_stack(
                    (
                        x_noise,
                        y_noise,
                    )
                )
                * self.scale
            )
            # add random throws to walker velocities
            self._velocities += delta
            # velocities update positions
            self._walkers += self._velocities
            # OPTION: cumulative sum adds x to y for ever agent - giving larger values at end of range
            # self._walkers += cumsum(self._velocities, axis=0)
            yield self._walkers


walker = Walkers(10, [0, -0.01])
walker.report()
print("running...")
w = walker.perlin()
print(next(w))
walker.report()