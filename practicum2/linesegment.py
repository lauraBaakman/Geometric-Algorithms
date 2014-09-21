""" This class stores a line as a vector and a point on the line."""
import vectors


class LineSegment(object):

    """This class stores a line as a vector and a point on the line."""

    def __init__(self, vector, point):
        """Construct a LineSegment object."""
        super(LineSegment, self).__init__()
        self.vector = vector
        self.point = point

    @classmethod
    def from_point_list(cls, points):
        """Return a LineSegment object from p1 to p2."""
        [p1, p2] = points
        vector = vectors.substract(p2, p1)
        return cls(vector, p1)

    def intersect(self, other):
        """
        Find the intersection of this LineSegment with other.

        Inspiration: http://stackoverflow.com/questions/563198/how-do
        -you-detect-where-two-line-segments-intersect
        """
        def intersection():
            """Test if the intersection lies on the segements if so compute it."""
            u_numerator = -(p[0]*r[1]) + q[0]*r[1] + p[1]*s[0] - q[1]*s[0]
            u = u_numerator / rCrossS
            if (u >= 0 and u <= 1):
                t_numerator = p[1]*r[0] - q[1]*r[0] - p[0]*r[1] + q[0]*r[1]
                t = t_numerator / rCrossS
                if (t >= 0 and t <= 1):
                    return ([
                        p[0] + r[0] * t,
                        p[1] + r[1] * t
                    ])
            return None

        def parallel():
            # """Check in which way the lines are parallel."""
            # q_min_p_cross_r = p[1]*r[0] - q[1]*r[0] - p[0]*r[1] + q[0]*r[1]
            # if not q_min_p_cross_r:
            #     # The lines are colinear
            #     p_min_q_cross_s = p[0]*r[0] - q[0]*r[0] - p[0]*s[0] + q[0]*s[0]
            #     if (
            #         q_min_p_cross_r >= 0
            #         and q_min_p_cross_r <= r[0] * r[0] + r[1] * r[1]
            #         and p_min_q_cross_s >= 0
            #         and p_min_q_cross_s <= s[0] * s[0] + s[1] * s[1]
            #     ):
            #         # The lins overlap
            #         None
            # else:
            #     None
            return None

        p = self.point
        r = self.vector
        q = other.point
        s = other.vector

        rCrossS = -(r[1]*s[0]) + r[0]*sr[1]

        if(not rCrossS):
            return intersection()
        else:
            return parallel()




    def __repr__(self):
        """Print-friendly representation of the LineSegment object."""
        return (
            '<LineSegment ('
            'vector = {obj.vector}, '
            'point = {obj.point}>'.format(obj=self)
        )


def test(arg):
    def test2:
        print arg
    test2()