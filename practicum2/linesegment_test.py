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
        l1 = LineSegment.from_point_list([[-24.0, 6.0], [4.0, 1.0]])
        l2 = LineSegment.from_point_list([[-10.0, -6.0], [4.0, 3.0]])
        intersection_point = [1.5652173913043477, 1.4347826086956523]
        self.assertEqual(l1.intersect(l2), intersection_point)
        self.assertEqual(l2.intersect(l1), intersection_point)

    def test_non_intersecting_non_parallel_linesegments(self):
        """The line segments aren't parallel but do not intersect."""
        l1 = LineSegment.from_point_list([[0.0, 0.0], [0.0, 4.0]])
        l2 = LineSegment.from_point_list([[1.0, 1.0], [5.0, 5.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_parallel_non_colinear_line_segments(self):
        """The line segements are parallel, but not colinear."""
        l1 = LineSegment.from_point_list([[0.0, 0.0], [0.0, 5.0]])
        l2 = LineSegment.from_point_list([[3.0, 2.0], [3.0, 7.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_non_overlapping(self):
        """The line segements are colinear but do not overlap."""
        l1 = LineSegment.from_point_list([[1.0, 2.0], [1.0, 7.0]])
        l2 = LineSegment.from_point_list([[1.0, 9.0], [1.0, 10.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_contained(self):
        """One of the line segments is contained in the other."""
        l1 = LineSegment.from_point_list([[1.0, 1.0], [5.0, 1.0]])
        l2 = LineSegment.from_point_list([[2.0, 1.0], [4.0, 1.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_overlapping(self):
        """One of the line segments partially overlaps the other."""
        l1 = LineSegment.from_point_list([[1.0, 1.0], [5.0, 1.0]])
        l2 = LineSegment.from_point_list([[0.0, 1.0], [3.0, 1.0]])
        self.assertFalse(l1.intersect(l2))
        self.assertFalse(l2.intersect(l1))

    def test_colinear_equal(self):
        """A line segment does not intersect with itself."""
        l1 = LineSegment.from_point_list([[1.0, 1.0], [5.0, 1, 0]])
        self.assertFalse(l1.intersect(l1))


class TestLinesegmentIntersectionWithLine(unittest.TestCase):

    """Unit test for the method intersection_with_line of the class line segment."""
    def setUp(self):
        """."""
        pass

    def test_intersecting_lines(self):
        """The line and LineSegment intersect."""
        l1 = LineSegment.from_point_list([[-2, 0], [6, 0]])
        l2 = [3, 1]
        self.assertTrue(l1.intersect_with_line(l2))

    def test_non_intersecting_lines(self):
        """The line intersects the line of the LineSegment, but not the LineSegment."""
        l1 = LineSegment.from_point_list([[1, 0], [6, 0]])
        l2 = [3, 1]
        self.assertFalse(l1.intersect_with_line(l2))

    def test_parallel_lines(self):
        """The line and the line segment are parallel."""
        l1 = LineSegment.from_point_list([[0, 2], [5, 2]])
        l2 = [1, 0]
        self.assertFalse(l1.intersect_with_line(l2))


if __name__ == '__main__':
    unittest.main()
