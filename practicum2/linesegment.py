""" This class stores a line as a vector and a point on the line."""
from __future__ import division
from fractions import *
import pdb


class LineSegment(object):

    """
    This class stores a line as a vector and a point on the line.
    """

    def __init__(self, vector, point, **kwargs):
        """Construct a LineSegment object."""
        super(LineSegment, self).__init__()
        self.vector = vector
        self.point = point

    @classmethod
    def from_point_list(cls, points):
        """Return a LineSegment object from p1 to p2."""
        [p1, p2] = points
        vector = [-p1[0] + p2[0], -p1[1] + p2[1]]
        return cls(vector, p1)

    def intersect(self, other):
        """
        Find the intersection of this LineSegment with other.
        """
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
        return False

    def intersect_with_ray(self, ray):
        """Test if this line segments intersects with a line represented as a vector."""
        p = self.point
        r = self.vector
        q = ray

        denominator = -(q[1] * r[0]) + q[0] * r[1]
        if(denominator):
            t_numerator = -(p[1] * q[0]) + p[0] * q[1]
            t = t_numerator / denominator
            # < i.p.v. <= om dubbel tellen te voorkomen.
            if(t <= 0 and t < 1):
                u_numerator = p[1] * r[0] - q[1] * r[0] - p[0] * r[1] + q[0] * r[1]
                u = u_numerator / denominator
                # > i.p.v. >= want eeen punt op een vertex ligt niet in de polygon
                return u > 0
        return False

    def __repr__(self):
        """Print-friendly representation of the LineSegment object."""
        return (
            '<LineSegment ('
            'vector = {obj.vector}, '
            'point = {obj.point}>'.format(obj=self)
        )
