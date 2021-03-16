from shapely.geometry import Polygon as SPolygon
from shapely import affinity


def translate_points(pts, xoff, yoff):
    poly = SPolygon(pts)
    poly = affinity.translate(poly, xoff, yoff)
    return list(poly.exterior.coords)


def rotate_points(pts, rad):
    poly = SPolygon(pts)
    poly = affinity.rotate(poly, rad, use_radians=True)
    return list(poly.exterior.coords)


def scale_points(pts, xscale, yscale):
    poly = SPolygon(pts)
    poly = affinity.scale(poly, xscale, yscale)
    return list(poly.exterior.coords)