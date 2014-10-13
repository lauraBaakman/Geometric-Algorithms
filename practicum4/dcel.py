"""Classes to represent a DCEL."""
import pdb

import delaunyUtils as du
from face import Face
from halfedge import HalfEdge
from vertex import Vertex


class DCEL(object):

    """
    Class to represent a doubly connected edge list.

    Properties:
        - vertices: List of vertices
        - edges: List of edges
        - faces: List of faces
    """

    @classmethod
    def from_delaunay_triangulation(cls, xl, yl, edges, triangles, neighs):
        """ Construct a DCEL from the output of matplotlib.delaunay.delaunay."""
        dcel = cls([], [], [])
        pdb.set_trace()

        for t in triangles:
            triangle_vertices = [Vertex(x) for x in du.get_triangle_vertices(xl, yl, t)]
            triangle_edges = [HalfEdge(x) for x in triangle_vertices]
            triangle_face = Face(triangle_edges[0])
            print triangle_face
            # for edge_idx, edge in enumerate(triangle_edges):
            #     pass

        return dcel

    def __init__(self, vertices, edges, faces):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
