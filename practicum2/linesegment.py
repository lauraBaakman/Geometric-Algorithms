""" This class stores a line as a vector and a point on the line."""
from __future__ import division
from fractions import *
import pdb


class LineSegment(object):

    """
    This class stores a line as a vector and a point on the line.

    The intersection method switches to a fraction representation
    when the differences are smaller than a certain epsilon that is
    set to 0.05 by default.
    """

    def __init__(self, vector, point, **kwargs):
        """Construct a LineSegment object."""
        super(LineSegment, self).__init__()
        self.vector = vector
        self.point = point
        self._epsilon = kwargs.get('epsilon', 0.05)

    @classmethod
    def from_point_list(cls, points):
        """Return a LineSegment object from p1 to p2."""
        [p1, p2] = points
        vector = [-p1[0] + p2[0], -p1[1] + p2[1]]
        return cls(vector, p1)

    def intersect(self, other):
        """
        Find the intersection of this LineSegment with other.

        Inspiration: http://stackoverflow.com/questions/563198/how-do
        -you-detect-where-two-line-segments-intersect
        """
        def intersection():
            """Test if the intersection lies on the segments if so compute it."""
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

        # def parallel():
        #     """Check in which way the lines are parallel."""
        #     q_min_p_cross_r = p[1]*r[0] - q[1]*r[0first, second] - p[0]*r[1] + q[0]*r[1]
        #     if not q_min_p_cross_r:
        #         # The lines are colinear
        #         p_min_q_cross_s = p[0]*r[0] - q[0]*r[0] - p[0]*s[0] + q[0]*s[0]
        #         if (
        #             q_min_p_cross_r >= 0
        #             and q_min_p_cross_r <= r[0] * r[0] + r[1] * r[1]
        #             and p_min_q_cross_s >= 0
        #             and p_min_q_cross_s <= s[0] * s[0] + s[1] * s[1]
        #         ):
        #             # The lins overlap
        #             print("linesegment.py:parallel:\t Overlap".format())
        #     print("linesegment.py:parallel:\t Geen Overlap".format())
        #     return None

        p = self.point
        r = self.vector
        q = other.point
        s = other.vector

        r_cross_s = -(r[1]*s[0]) + r[0]*s[1]

        if(r_cross_s):
            return intersection()
        else:
            return False

    def intersect_with_ray(self, other):
        """Test if this line segments intersects with a line represented as a vector."""
        q = self.point
        s = self.vector
        r = other

        r_cross_s = -(r[1]*s[0]) + r[0]*s[1]
        if(r_cross_s):
            u_numerator = -(q[1]*r[0]) + q[0]*r[1]
            u = u_numerator / r_cross_s
            if (u >= 0 and u <= 1):
                t_numerator = -(q[1] * s[0]) + q[0]*s[1]
                t = t_numerator / r_cross_s
                return (t >= 0)
        return False

    def __repr__(self):
        """Print-friendly representation of the LineSegment object."""
        return (
            '<LineSegment ('
            'vector = {obj.vector}, '
            'point = {obj.point}>'.format(obj=self)
        )
