def hex_to_rgba(hex):
    h = hex.lstrip("#")
    l = len(h)
    r = int(h[0:2], 16) / 255.0
    g = int(h[2:4], 16) / 255.0
    b = int(h[4:6], 16) / 255.0
    a = 1.0
    if l > 6:
        a = int(h[6:8], 16) / 255.0
    return [r, g, b, a]
