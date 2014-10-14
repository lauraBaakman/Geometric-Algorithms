"""Module with unit tests for the file delaunyUtils.py."""
import unittest
import pdb
import matplotlib.delaunay as triang
import numpy

from delaunyUtils import *


class TestDelaunyUtils(unittest.TestCase):

    """TestDelaunyUtils methods."""

    def setUp(self):
        """."""
        self.xl = [150, 200, 250, 450, 600, 10]
        self.yl = [550, 450, 500, 100, 550, 10]
        xa = numpy.array(self.xl)
        ya = numpy.array(self.yl)
        self.centres, self.edges, self.triangles, self.neighs = triang.delaunay(xa, ya)

    def test_get_triangle_vertices(self):
        """Test the method get_triangle_vertices."""
        triangle_idx = 0
        computed_vertices = get_triangle_vertices(self.xl, self.yl, self.triangles[triangle_idx])
        correct_vertices = [[10, 10], [200, 450], [450, 100]]
        self.assertEqual(computed_vertices[0], correct_vertices[0])
        self.assertEqual(computed_vertices[1], correct_vertices[1])
        self.assertEqual(computed_vertices[2], correct_vertices[2])

    def test_get_edge(self):
        """Test the method get_edge."""
        edge_idx = 0
        computed_edge = get_edge(self.xl, self.yl, self.edges[edge_idx])
        correct_edge = [[10, 10], [450, 100]]
        self.assertEqual(computed_edge[0], correct_edge[0])
        self.assertEqual(computed_edge[1], correct_edge[1])

if __name__ == '__main__':
    unittest.main()
