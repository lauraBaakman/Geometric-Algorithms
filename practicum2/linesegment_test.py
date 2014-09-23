"""Unit tests for linesegment class."""
import unittest

from linesegment import *


class TestLinesegmentIntersection(unittest.TestCase):

    """Unit test for the method intersection of the class line segment."""

    def setUp(self):
        """."""
        pass

    def test_intersecting_linesegments(self):
        """The line segments intersect."""
        l1 = LineSegment.from_point_list([[0, 0], [4, 0]])
        l2 = LineSegment.from_point_list([[0, -1], [4, 3]])
        self.assertTrue(l1.intersect(l2))
        self.assertTrue(l2.intersect(l1))

    def test_non_intersecting_non_parallel_linesegments(self):
        """The line segments aren't parallel but do not intersect."""
        l1 = LineSegment.from_point_list([[0, 0], [0, 4]])
        l2 = LineSegment.from_point_list([[1, 1], [5, 5]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_parallel_non_colinear_line_segments(self):
        """The line segements are parallel, but not colinear."""
        l1 = LineSegment.from_point_list([[0, 0], [0, 5]])
        l2 = LineSegment.from_point_list([[3, 2], [3, 7]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_non_overlapping(self):
        """The line segements are colinear but do not overlap."""
        l1 = LineSegment.from_point_list([[1, 2], [1, 7]])
        l2 = LineSegment.from_point_list([[1, 9], [1, 10]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_contained(self):
        """One of the line segments is contained in the other."""
        l1 = LineSegment.from_point_list([[1, 1], [5, 1]])
        l2 = LineSegment.from_point_list([[2, 1], [4, 1]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_overlapping(self):
        """One of the line segments partially overlaps the other."""
        l1 = LineSegment.from_point_list([[1, 1], [5, 1]])
        l2 = LineSegment.from_point_list([[0, 1], [3, 1]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_equal(self):
        """A line segment does not intersect with itself."""
        l1 = LineSegment.from_point_list([[1, 1], [5, 1]])
        self.assertFalse(l1.intersect(l1))


if __name__ == '__main__':
    unittest.main()
