"""Module with unit tests for the linesegment module."""
import unittest
from linesegment import *
import pdb


class Test_triangle_point_in_triangle(unittest.TestCase):

    """Unit tests for the method line_segments_intersect in the module linesegment."""

    def setUp(self):
        """."""
        pass

    def test_parallel_line_segments(self):
        """The line segments are parallel."""
        p1 = [2, 1]
        p2 = [4, 1]
        p3 = [5, 3]
        p4 = [9, 3]
        result = line_segments_intersect([p1, p2], [p3, p4])
        self.assertIsNone(result)

    def test_intersecting_line_segments(self):
        """The line segments intersect on a non vertex."""
        p1 = [1, 2]
        p2 = [6, 2]
        p3 = [0, -1]
        p4 = [9, 8]
        result = line_segments_intersect([p1, p2], [p3, p4])
        answer = [3, 2]
        self.assertEqual(result, answer)

    def test_intersecting_line_segments_on_end_point(self):
        """The line segments intersect on the first endpoint of a vertex."""
        p1 = [1, 2]
        p2 = [6, 2]
        p3 = [1, 0]
        p4 = [1, 7]
        result = line_segments_intersect([p1, p2], [p3, p4])
        answer = p1
        self.assertEqual(result, answer)

    def test_intersecting_line_segments_on_end_point_2(self):
        """The line segments intersect on the last endpoint of a vertex."""
        p1 = [1, 2]
        p2 = [6, 2]
        p3 = [6, 0]
        p4 = [6, 7]
        result = line_segments_intersect([p1, p2], [p3, p4])
        answer = p2
        self.assertEqual(result, answer)

    def test_intersecting_line_segments_that_dont_intersect(self):
        """The line segments would intersect if they were lines."""
        p1 = [1, 2]
        p2 = [6, 2]
        p3 = [4, 3]
        p4 = [9, 8]
        result = line_segments_intersect([p1, p2], [p3, p4])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
