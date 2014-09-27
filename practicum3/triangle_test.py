"""Module with unit tests for the triangle module."""
import unittest
from triangle import *


class Test_triangle_point_in_triangle(unittest.TestCase):

    """Unit tests for the method point_in_triangle in the module triangle."""

    def setUp(self):
        """."""
        pass

    def test_point_in_triangle(self):
        """The point lies inside the triangle."""
        triangle = [[2, 1], [7, 2], [4, 6]]
        point = [4, 3]
        self.assertTrue(point_in_triangle(triangle, point))

    def test_point_is_triangle_vertex(self):
        """The point is a vertex of the triangle."""
        triangle = [[2, 1], [7, 2], [4, 6]]
        point = triangle[0]
        self.assertFalse(point_in_triangle(triangle, point))

    def test_point_on_triangle_edge(self):
        """The lies on the edge of the triangle."""
        triangle = [[2, 1], [7, 1], [4, 6]]
        point = [3, 1]
        self.assertFalse(point_in_triangle(triangle, point))

    def test_point_outside_of_triangle(self):
        """The point lies outside the triangle."""
        triangle = [[2, 1], [7, 2], [4, 6]]
        point = [10, 9]
        self.assertFalse(point_in_triangle(triangle, point))


if __name__ == '__main__':
    unittest.main()
