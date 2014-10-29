""" Some computations that are necessary for the polygon intersection algorithm."""
from __future__ import division
from fractions import *


def point_in_polygon(point, polygon):
    """
    Return true if the point point is contained in the polygon polygon.

    Input:
        point: a 2D point as [x,y]
        polygon: a list of n points in CCW order: [[x1, y1], ..., [xn, yn]]
    """
    polygon_translated = [[vertex[0] - point[0], vertex[1] - point[1]] for vertex in polygon]
    polygon_shift = polygon_translated[1:]
    polygon_shift.append(polygon_translated[0])
    area = [
        1
        for (a, b)
        in zip(polygon_translated, polygon_shift)
        if (b[0] * a[1] - a[0] * b[1]) < 0
    ]
    return sum(area) in [0, len(polygon)]


def vertex_in_half_plane(vertex, half_plane):
    """
    Return true if the vertex vertex lies in the half plane half_plane.

    Input:
        vertex: a 2D vertex as [x,y]
        half-plane: a vector as its begin point (bx, by) and its endpoint
            (ex, ey) in a list: [[bx, by], [ex, ey]].
    """
    [p_min, p] = half_plane
    return (
        (p[1] * p_min[0] - p[0] * p_min[1] - p[1] * vertex[0] +
            p_min[1] * vertex[0] + p[0] * vertex[1] - p_min[0] * vertex[1]) <= 0
    )


class LineSegment(object):

    """This class stores a line as a vector and a point on the line."""

    def __init__(self, points):
        """
        Construct a LineSegment object.

        Input:
            points: list of two points of the form [[x1, y1], [x2, y2]].
        """
        super(LineSegment, self).__init__()
        [p1, p2] = points
        self.vector = [-p1[0] + p2[0], -p1[1] + p2[1]]
        self.point = p1

    def intersect_line_segment(self, other):
        """Find the intersection of this LineSegment with other."""
        p = self.point
        r = self.vector
        q = other.point
        s = other.vector

        r_cross_s = -(r[1]*s[0]) + r[0]*s[1]

        if(r_cross_s):
            u_numerator = p[1]*r[0] - q[1]*r[0] - p[0]*r[1] + q[0]*r[1]

            u = u_numerator / r_cross_s
            if (u >= 0 and u <= 1):
                t_numerator = p[1]*s[0] - q[1]*s[0] - p[0]*s[1] + q[0]*s[1]
                t = t_numerator / r_cross_s
                if (t >= 0 and t <= 1):
                    x = p[0] + r[0] * t
                    y = p[1] + r[1] * t
                    return [x, y]
        return None
