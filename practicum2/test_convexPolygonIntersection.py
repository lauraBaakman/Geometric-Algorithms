"""Test methods and classes in the file convexPolygonIntersection."""

import unittest

from convexPolygonIntersection import *


class TestNextPrevious(unittest.TestCase):

    """Unit test for the methods plus and min."""

    def setUp(self):
        """."""
        self.P = [[100, 100], [100, 400], [500, 400], [500, 100]]
        self.Q = self.P
        self.cpi = ConvexPolygonIntersection(self.P, self.Q)

    def test_advance(self):
        """."""
        self.cpi.advance_p(None)
        self.assertEqual(self.cpi._p_idx, 1)
        self.cpi.advance_q(None)
        self.assertEqual(self.cpi._q_idx, 1)

        self.cpi.advance_p(None)
        self.assertEqual(self.cpi._p_idx, 2)
        self.cpi.advance_q(None)
        self.assertEqual(self.cpi._q_idx, 2)

        self.cpi.advance_p(None)
        self.assertEqual(self.cpi._p_idx, 3)
        self.cpi.advance_q(None)
        self.assertEqual(self.cpi._q_idx, 3)

        self.cpi.advance_p(None)
        self.assertEqual(self.cpi._p_idx, 0)
        self.cpi.advance_q(None)
        self.assertEqual(self.cpi._q_idx, 0)

    def test_get(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p(), self.P[0])
        self.assertItemsEqual(self.cpi.get_q(), self.Q[0])

    def test_get_min(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[3])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[3])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[0])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[0])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[1])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[1])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[2])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[2])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_min(), self.P[3])
        self.assertItemsEqual(self.cpi.get_q_min(), self.Q[3])

    def test_get_plus(self):
        """."""
        self.assertItemsEqual(self.cpi.get_p_plus(), self.P[1])
        self.assertItemsEqual(self.cpi.get_q_plus(), self.Q[1])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_plus(), self.P[2])
        self.assertItemsEqual(self.cpi.get_q_plus(), self.Q[2])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_plus(), self.P[3])
        self.assertItemsEqual(self.cpi.get_q_plus(), self.Q[3])
        self.cpi.advance_p(None)
        self.cpi.advance_q(None)
        self.assertItemsEqual(self.cpi.get_p_plus(), self.P[0])
        self.assertItemsEqual(self.cpi.get_q_plus(), self.Q[0])

    def test_get_dot(self):
        """."""
        self.assertEqual(self.cpi.get_p_dot()[0][0], self.P[3][0])
        self.assertEqual(self.cpi.get_p_dot()[0][1], self.P[3][1])
        self.assertEqual(self.cpi.get_p_dot()[1][0], self.P[0][0])
        self.assertEqual(self.cpi.get_p_dot()[1][1], self.P[0][1])

        self.assertEqual(self.cpi.get_q_dot()[0][0], self.Q[3][0])
        self.assertEqual(self.cpi.get_q_dot()[0][1], self.Q[3][1])
        self.assertEqual(self.cpi.get_q_dot()[1][0], self.Q[0][0])
        self.assertEqual(self.cpi.get_q_dot()[1][1], self.Q[0][1])

if __name__ == '__main__':
    unittest.main()
