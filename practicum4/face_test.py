"""Module with unit tests for the DCEL module."""
import unittest
import numpy
import matplotlib.delaunay as triang
import pdb
from dcel import *


class TestFace(unittest.TestCase):

    """."""

    def setUp(self):
        """."""
        # self.xl = [150, 200, 250, 450, 600, 10]
        # self.yl = [550, 450, 500, 100, 550, 10]
        # xa = numpy.array(self.xl)
        # ya = numpy.array(self.yl)
        # self.centres, self.edges, self.triangles, self.neighs = triang.delaunay(xa, ya)
        pass

    # def test_number_of_vertices_triangle(self):
    #     """Test the method number_of_vertices on a triangle."""
    #     dc = DCEL.from_delaunay_triangulation(
    #         self.xl, self.yl, self.triangles, self.centres
    #     )
    #     face = dc.faces[0]
    #     result_returned = face.number_of_vertices()
    #     result_correct = 3
    #     self.assertEqual(result_returned, result_correct)

    # def test_get_edges_triangle(self):
    #     """Test the method get_edges on a triangle."""
    #     dc = DCEL.from_delaunay_triangulation(
    #         self.xl, self.yl, self.triangles, self.centres
    #     )
    #     face = dc.faces[0]
    #     edges_correct = []
    #     edges_correct.append(dc.edges[0])
    #     edges_correct.append(dc.edges[2])
    #     edges_correct.append(dc.edges[4])
    #     edges_returned = face.get_edges_inner_component()
    #     self.assertItemsEqual(edges_returned, edges_correct)

    def test_is_bounded_test_true(self):
        """Test the method is_bounded."""
        face = Face('outercomponent', circumcentre=[3, 5])
        result_returned = face.is_bounded()
        self.assertTrue(result_returned)

    def test_is_bounded_test_false(self):
        """Test the method is_bounded."""
        face = Face('outercomponent')
        result_returned = face.is_bounded()
        self.assertFalse(result_returned)

if __name__ == '__main__':
    unittest.main()
