"""Test methods and classes in the file convexPolygonIntersection."""

import unittest
import pdb

from convexPolygonIntersection import *


class TestNextPrevious(unittest.TestCase):

    """Unit test for the methods plus and min."""

    def setUp(self):
        """."""
        self.P = [[100, 100], [100, 400], [500, 400], [500, 100]]
        self.Q = self.P
        self.cpi = ConvexPolygonIntersection(self.P, self.Q)

    def test_get(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p(), self.P[0])
        self.assertItemsEqual(self.cpi.get_q(), self.Q[0])

    def test_get_min(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[3])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[3])

    def test_get_plus(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p_plus(), self.P[1])
        self.assertItemsEqual(self.cpi.get_q_plus(), self.Q[1])

    def test_get_dot(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p_dot(), [self.P[3], self.P[0]])
        self.assertItemsEqual(self.cpi.get_q_dot(), [self.Q[3], self.Q[0]])

    def test_advance(self):
        """."""
        pdb.set_trace()
        self.cpi.advance_p(None)
        self.assertEqual(self.cpi._p_idx, 1)
        self.cpi.advance_q(None)
        self.assertEqual(self.cpi._q_idx, 1)

if __name__ == '__main__':
    unittest.main()
