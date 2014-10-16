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
        self.xl = [000, 550, 250, 750]
        self.yl = [700, 500, 200, 000]
        xa = numpy.array(self.xl)
        ya = numpy.array(self.yl)
        self.centres, self.edges, self.triangles, self.neighs = triang.delaunay(xa, ya)

    # def test_from_delaunay_triangulation(self):
    #     """."""
    #     dc = DCEL.from_delaunay_triangulation(
    #         self.xl, self.yl, self.triangles, self.centres
    #     )
    #     # Check if the DCEL doesn't have more vertices than the triangulation
    #     self.assertEqual(len(self.xl), len(dc.vertices))

    #     # Check if the DCEL contains all the vertices of the triangulation
    #     vertices = []
    #     for (x, y) in zip(self.xl, self.yl):
    #         vertex = Vertex([x, y])
    #         vertices.append(vertex)
    #         self.assertIn(vertex, dc.vertices)

    # def test_get_bounded_faces(self):
    #     """."""
    #     dc = DCEL.from_delaunay_triangulation(
    #         self.xl, self.yl, self.triangles, self.centres
    #     )
    #     dc.get_bounded_faces()
    #     print dc.faces
    #     print dc.get_bounded_faces()

    def test_dual(self):
        """."""
        dc = DCEL.from_delaunay_triangulation(
            self.xl, self.yl, self.triangles, self.centres
        )
        print "Original DCEL"
        print dc

        dc_dual = dc.dual()
        print "Original dual DCEL"
        print dc_dual

# class TestHalfEdge(unittest.TestCase):

#     """."""

#     def setUp(self):
#         """."""
#         self.vertex_a = Vertex([1, 2])
#         self.vertex_b = Vertex([3, 4])
#         self.edge_a_ = HalfEdge(self.vertex_a)
#         self.edge_b_ = HalfEdge(self.vertex_b)
#         self.edge_ab = HalfEdge(self.vertex_a, nxt=self.edge_b_)
#         self.edge_ba = HalfEdge(self.vertex_b, nxt=self.edge_a_, twin=self.edge_ab)
#         self.edge_ab.twin = self.edge_ba
#         self.vertex_a.incident_edge = self.edge_a_
#         self.vertex_b.incident_edge = self.edge_b_

#     def test_get_destination(self):
#         """."""
#         destination_returned = self.edge_ab.get_destination()
#         destination_correct = self.vertex_b
#         self.assertEqual(destination_returned, destination_correct)

#     def test_as_points(self):
#         """."""
#         points_returned = self.edge_ab.as_points()
#         points_correct = [[1, 2], [3, 4]]
#         self.assertEqual(points_returned, points_correct)


# class TestFace(unittest.TestCase):

#     """."""

#     def setUp(self):
#         """."""
#         pdb.set_trace()
#         self.xl = [150, 200, 250, 450, 600, 10]
#         self.yl = [550, 450, 500, 100, 550, 10]
#         xa = numpy.array(self.xl)
#         ya = numpy.array(self.yl)
#         self.centres, self.edges, self.triangles, self.neighs = triang.delaunay(xa, ya)
#         self.dc = DCEL.from_delaunay_triangulation(
#             self.xl, self.yl, self.edges, self.triangles, self.neighs
#         )

#     def test_number_of_vertices_triangle(self):
#         """Test the method number_of_vertices on a triangle."""
#         pdb.set_trace()
#         face = self.dc.faces[0]
#         result_returned = face.number_of_vertices()
#         result_correct = 3
#         self.assertEqual(result_returned, result_correct)

#     def test_get_edges_triangle(self):
#         """Test the method get_edges on a triangle."""
#         face = self.dc.faces[0]
#         edges_correct = []
#         edges_correct.append(self.dc.edges[0])
#         edges_correct.append(self.dc.edges[2])
#         edges_correct.append(self.dc.edges[4])
#         edges_returned = face.get_edges()
#         self.assertItemsEqual(edges_returned, edges_correct)

if __name__ == '__main__':
    unittest.main()
