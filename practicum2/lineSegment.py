""" This class stores a line as a vector and a point on the line."""
from __future__ import division
from fractions import *


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

    def intersect(self, other):
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

    def __repr__(self):
        """Print-friendly representation of the LineSegment object."""
        return (
            '<LineSegment ('
            'vector = {obj.vector}, '
            'point = {obj.point}>'.format(obj=self)
        )
