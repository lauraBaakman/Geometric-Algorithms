"""Module with unit tests for the DCEL module."""
import unittest
import numpy
import matplotlib.delaunay as triang
import pdb
from dcel import *


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
        DCEL.from_delaunay_triangulation(
            self.xl, self.yl, self.edges, self.triangles, self.neighs
        )

if __name__ == '__main__':
    unittest.main()
