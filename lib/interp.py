def lerp(start, end, pct):
    return start + (end - start) * pct


def remap(in_min, in_max, out_min, out_max, x):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
