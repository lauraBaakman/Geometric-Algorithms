"""Classes to represent a DCEL."""
import pdb

from delaunyUtils import *
# from face import Face
# from halfedge import HalfEdge
# from vertex import Vertex


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
        dcl_vertices, dcl_edges, dcl_faces = [], [], []

        # Call the actual DCL constructor
        return cls(dcl_vertices, dcl_edges, dcl_faces)

    def __init__(self, vertices, edges, faces):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices
        self.edges = edges
        self.faces = faces

if __name__ == '__main__':
    xl = [0, 2, 2, 1]
    yl = [4, 4, 2, 1]
    edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 0]]
    triangles = [[0, 2, 1], [0, 3, 2]]
    neighs = [[1, -1, -1], [0, -1, -1]]
