"""Module with unit tests for the DCEL module."""
import unittest
import numpy
import matplotlib.delaunay as triang
import pdb
from dcel import *
from vertex import Vertex


class TestDCEL(unittest.TestCase):

    """."""

    def setUp(self):
        """."""
        self.xl = [150, 200, 250, 450, 600, 10]
        self.yl = [550, 450, 500, 100, 550, 10]
        xa = numpy.array(self.xl)
        ya = numpy.array(self.yl)
        self.centres, self.edges, self.triangles, self.neighs = triang.delaunay(xa, ya)

    def test_from_delaunay_triangulation(self):
        """."""
        dc = DCEL.from_delaunay_triangulation(
            self.xl, self.yl, self.edges, self.triangles, self.neighs
        )
        for vertex in dc.vertices:
            print vertex


class TestHalfEdge(unittest.TestCase):

    """."""

    def setUp(self):
        """."""
        self.vertex_a = Vertex([1, 2])
        self.vertex_b = Vertex([3, 4])
        self.edge_a_ = HalfEdge(self.vertex_a)
        self.edge_b_ = HalfEdge(self.vertex_b)
        self.edge_ab = HalfEdge(self.vertex_a, nxt=self.edge_b_)
        self.edge_ba = HalfEdge(self.vertex_b, nxt=self.edge_a_, twin=self.edge_ab)
        self.edge_ab.twin = self.edge_ba
        self.vertex_a.incident_edge = self.edge_a_
        self.vertex_b.incident_edge = self.edge_b_

    def test_get_destination(self):
        """."""
        destination_returned = self.edge_ab.get_destination()
        destination_correct = self.vertex_b
        self.assertEqual(destination_returned, destination_correct)

    def test_as_points(self):
        """."""
        points_returned = self.edge_ab.as_points()
        points_correct = [[1, 2], [3, 4]]
        self.assertEqual(points_returned, points_correct)


if __name__ == '__main__':
    unittest.main()
