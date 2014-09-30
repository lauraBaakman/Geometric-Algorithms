"""Module with unit tests for the plane module."""
import unittest
from plane import *


class Test_project_point_on_plane(unittest.TestCase):

    """Unit tests for the method project_point_on_plane in the module plane."""

    def setUp(self):
        """."""
        pass

    def test_plane_is_xy_plane(self):
        """The plane is the x, y plane."""
        plane = [[2, 1, 0], [7, 2, 0], [4, 6, 0]]
        point = [4, 3]
        correct_answer = [4, 3, 0]
        self.assertAlmostEqual(project_point_on_plane(plane, point), correct_answer)

    def test_plane_is_parallel_to_xy_plane(self):
        """The plane is parallel to the x,y plane."""
        plane = [[2, 1, 3], [7, 2, 3], [4, 6, 3]]
        point = [4, 3]
        correct_answer = [4, 3, 3]
        self.assertAlmostEqual(project_point_on_plane(plane, point), correct_answer)

    def test_plane_is_perpendicular_to_xy_plane(self):
        """The plane is perpenciular to the x,y plane."""
        plane = [[2, 3, 2], [7, 3, 6], [4, 3, 7]]
        point = [4, 3]
        self.assertFalse(project_point_on_plane(plane, point))

    def test_point_can_be_normally_projected_onto_plane(self):
        """The normal case."""
        plane = [[2, 3, 2], [7, 3, 6], [4, 8, 7]]
        point = [4, 3]
        correct_answer = [4, 3, 3.6]
        self.assertAlmostEqual(project_point_on_plane(plane, point), correct_answer)

    def test_the_points_dont_define_a_plane(self):
        """The three points that define the plane are colinear."""
        plane = [[1, 2, 1], [2, 3, 2], [3, 4, 3]]
        point = [4, 3]
        self.assertFalse(project_point_on_plane(plane, point))


if __name__ == '__main__':
    unittest.main()
