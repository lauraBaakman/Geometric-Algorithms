"""Test methods and classes in the file convexPolygonIntersection."""

import unittest

from lineSegment import *


class TestLinesegmentIntersection(unittest.TestCase):

    """Unit test for the method intersection of the class line segment."""

    def setUp(self):
        """."""
        pass

    def test_intersecting_linesegments(self):
        """The line segments intersect."""
        l1 = LineSegment([[-24.0, 6.0], [4.0, 1.0]])
        l2 = LineSegment([[-10.0, -6.0], [4.0, 3.0]])
        intersection_point = [1.5652173913043477, 1.4347826086956523]
        self.assertEqual(l1.intersect(l2), intersection_point)
        self.assertEqual(l2.intersect(l1), intersection_point)

    def test_non_intersecting_non_parallel_linesegments(self):
        """The line segments aren't parallel but do not intersect."""
        l1 = LineSegment([[0.0, 0.0], [0.0, 4.0]])
        l2 = LineSegment([[1.0, 1.0], [5.0, 5.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_parallel_non_colinear_line_segments(self):
        """The line segements are parallel, but not colinear."""
        l1 = LineSegment([[0.0, 0.0], [0.0, 5.0]])
        l2 = LineSegment([[3.0, 2.0], [3.0, 7.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_non_overlapping(self):
        """The line segements are colinear but do not overlap."""
        l1 = LineSegment([[1.0, 2.0], [1.0, 7.0]])
        l2 = LineSegment([[1.0, 9.0], [1.0, 10.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_contained(self):
        """One of the line segments is contained in the other."""
        l1 = LineSegment([[1.0, 1.0], [5.0, 1.0]])
        l2 = LineSegment([[2.0, 1.0], [4.0, 1.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_overlapping(self):
        """One of the line segments partially overlaps the other."""
        l1 = LineSegment([[1.0, 1.0], [5.0, 1.0]])
        l2 = LineSegment([[0.0, 1.0], [3.0, 1.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_equal(self):
        """A line segment does not intersect with itself."""
        l1 = LineSegment([[1.0, 1.0], [5.0, 1, 0]])
        self.assertFalse(l1.intersect(l1))


if __name__ == '__main__':
    unittest.main()
