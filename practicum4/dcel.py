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
        for t in triangles:
            triangle_vertices = [Vertex(x) for x in du.get_triangle_vertices(xl, yl, t)]
            triangle_edges = [HalfEdge(x) for x in triangle_vertices]
            triangle_face = Face(triangle_edges[0])
            for edge_idx, edge in enumerate(triangle_edges):
                edge.nxt = triangle_edges[(edge_idx + 1) % 3]
                edge.prev = triangle_edges[(edge_idx + 3 - 1) % 3]
                edge.incident_face = triangle_face
                triangle_vertices[edge_idx].incident_edge = edge
        return dcel

    def __init__(self, vertices, edges, faces):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
