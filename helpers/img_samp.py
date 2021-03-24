import matplotlib.image as mpimg
import numpy as np


class Sampler:
    cached = None

    def __init__(self, filename):
        self.filename = filename

    def load_image(self):
        if Sampler.cached != None:
            return Sampler.cached

        print("building texture sample...")

        img = mpimg.imread(self.filename)
        img = (img * 255).astype(int)
        height, width, depth = img.shape
        img = img.reshape(width * height, depth)
        out = []
        for row in img:
            # rgba -> argb
            out.append(row[3])
            out.append(row[0])
            out.append(row[1])
            out.append(row[2])

        Sampler.cached = (width, height, depth, memoryview(np.array(out)))
        return Sampler.cached
