"""."""
from utilities import *


class ConvexPolygonIntersection(object):

    """
    Class that computes the intersection of two polygons.

    Polygons are represented as a list of points in counter clockwise
    order.

    This class is an Iterator so that the algorithm may be executed
    step by step.

    Properties
        Public:
        - P: Set of points n in the form [[x1, y1], [x2, y2], ..., [xn, yn]]
        - Q: Set of points m in the form [[x1, y1], [x2, y2], ..., [xm, ym]]
        - intersections: A list of the currently found intersections in the form [[x1, y1], ...]

        Private:
        - max_steps: maximum number of steps
        - current_step: number of steps already taken
        - first_intersection: the first intersection the algorithm found
        - p_idx: current vertex in the polygon P as an index in P
        - q_idx: current vertex in the polygon Q as an index in Q
    """

    def __init__(self, set_P, set_Q):
        """Constructor of the class convexPolygonIntersection.

        Input:
            set_P: vertices of a convex polygon in CCW order.
            set_Q: vertices of a convex polygon in CCW order.
        """
        super(ConvexPolygonIntersection, self).__init__()
        self.P = set_P
        self.Q = set_Q
        self._max_steps = 2 * (len(self.P) + len(self.Q))
        self._current_step = 0
        self._first_intersection = None
        self.intersections = []
        self.algorithm_init()

    def __iter__(self):
        """Make this class iterable ."""
        return self

    def next(self):
        """Take the next step."""
        if(self._current_step <= self._max_steps):
            self.algorithm_step()
        else:
            self.algorithm_finalize()
            raise StopIteration('Executed the maximum number of steps.')
        self._current_step = self._current_step + 1

    def advance_q(self, inside):
        """Advance q."""
        self._q_idx = (self._q_idx + 1) % len(self.Q)
        if inside == 'Q':
            return self.get_q_min()

    def advance_p(self, inside):
        """Advance p."""
        self._p_idx = (self._p_idx + 1) % len(self.P)
        if inside == 'P':
            return self.get_p_min()

    def get_p_min(self):
        """Return p min."""
        card_p = len(self.P)
        return self.P[(self._p_idx - 1 + card_p) % card_p]

    def get_q_min(self):
        """Return q min."""
        card_q = len(self.Q)
        return self.Q[(self._q_idx - 1 + card_q) % card_q]

    def get_p_plus(self):
        """Return p plus."""
        return self.P[(self._p_idx + 1) % len(self.P)]

    def get_q_plus(self):
        """Return p plus."""
        return self.Q[(self._q_idx + 1) % len(self.Q)]

    def get_p(self):
        """return p."""
        return self.P[self._p_idx]

    def get_q(self):
        """return q."""
        return self.Q[self._q_idx]

    def get_p_dot(self):
        """Return the begin and endpoints of the vector pdot."""
        return [self.get_p_min(), self.P[self._p_idx]]

    def get_q_dot(self):
        """Return the begin and endpoints of the vector qdot."""
        return [self.get_q_min(), self.Q[self._q_idx]]

    def algorithm_init(self):
        """Initialization of the algorithm."""
        self._p_idx = 0
        self._q_idx = 0

    def algorithm_step(self):
        """
        Step of the algorithm.

        Returns the intersection(s) or none is no intersection was found.
        """
        def q_dot_cross_p_dot():
            """Compute the dot product of q_dot and p_dot."""
            p = self.get_p()
            q = self.get_q()
            p_min = self.get_p_min()
            q_min = self.get_q_min()
            return (
                p[1] * q[0] - p_min[1] * q[0] - p[0] * q[1] + p_min[0] * q[1] -
                p[1] * q_min[0] + p_min[1] * q_min[0] + p[0] * q_min[1] - p_min[0] * q_min[1]
            )

        intersection = LineSegment(self.get_p_dot()).intersect_line_segment(
            LineSegment(self.get_q_dot()))
        inside = None
        if(intersection):
            if(not self._first_intersection):
                self._first_intersection = intersection
            else:
                if(self._first_intersection == intersection):
                    raise StopIteration(
                        'The current intersection is equal to the first intersection.'
                    )
            if(vertex_in_half_plane(self.get_p(), self.get_q_dot())):
                inside = 'P'
            else:
                inside = 'Q'
            self.intersections.append(intersection)
        if(q_dot_cross_p_dot() >= 0):
            if(vertex_in_half_plane(self.get_p(), self.get_q_dot())):
                intersection2 = self.advance_q(inside)
            else:
                intersection2 = self.advance_p(inside)
        else:
            if(vertex_in_half_plane(self.get_q(), self.get_p_dot())):
                intersection2 = self.advance_p(inside)
            else:
                intersection2 = self.advance_q(inside)

        if(intersection2):
            self.intersections.append(intersection2)

    def algorithm_finalize(self):
        """
        Finalization of the algorithm.

        Test if one polygon is contained in the other.
        """
        if(point_in_polygon(self.get_p(), self.Q)):
            self.intersections = self.P
        elif(point_in_polygon(self.get_q(), self.P)):
            self.intersections = self.Q


if __name__ == '__main__':
    P = [[5, 20], [25, 20], [25, 50]]
    Q = [[15, 10], [50, 30], [15, 30]]
    A = [[50, 200], [250, 200], [250, 500]]
    D = [[300, 100], [500, 200], [350, 400]]

    pq_intersection_iterator = ConvexPolygonIntersection(A, D)
    while(True):
        pq_intersection_iterator.next()
