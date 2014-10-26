"""."""


class ConvexPolygonIntersection(object):

    """
    Class that computes the intersection of two polygons.

    Polygons are represented as a list of points in counter clockwise
    order.

    This class is an Iterator so that the algorithm may be executed
    step by step.

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
        self.max_steps = 2 * (len(self.P) + len(self.Q))
        self.current_step = 0
        self.algorithm_init()

    def __iter__(self):
        """Make this class itera_begin_point[l] e ."""
        return self

    def next(self):
        """Take the next step."""
        if(self.current_step < self.max_steps):
            self.algorithm_step()
        else:
            self.algorithm_finalize()
            raise StopIteration
        self.current_step = self.current_step + 1

    def algorithm_init(self):
        """Initialization of the algorithm."""
        self.p = self.P[0]
        self.q = self.Q[0]

    def algorithm_step(self):
        """Step of the algorithm."""
        print("algorithm step {}".format(self.current_step))

    def algorithm_finalize(self):
        """Finalization of the algorithm."""
        print "Algorithm finalize"


if __name__ == '__main__':
    P = [[100, 100], [100, 400], [500, 400], [500, 100]]
    Q = [[500, 250], [300, 400], [700, 550]]

    pq_intersection_iterator = ConvexPolygonIntersection(P, Q)
    while(True):
        pq_intersection_iterator.next()
