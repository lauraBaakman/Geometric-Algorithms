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
        def isTwin(edge, possible_twin):
            return edge.nxt.origin.coordinates == twin.origin.coordinates

        dcel = cls()
        pdb.set_trace()
        for t in triangles:
            triangle_vertices = [Vertex(x) for x in du.get_triangle_vertices(xl, yl, t)]
            triangle_edges = [HalfEdge(x) for x in triangle_vertices]
            triangle_face = Face(triangle_edges[0])
            for edge_idx, edge in enumerate(triangle_edges):
                edge.nxt = triangle_edges[(edge_idx + 1) % 3]
                edge.prev = triangle_edges[(edge_idx + 3 - 1) % 3]
                edge.incident_face = triangle_face
                triangle_vertices[edge_idx].incident_edge = edge
            dcel.add_vertices(triangle_vertices)
            dcel.edges.extend(triangle_edges)
            dcel.faces.append(triangle_face)

        # Add containing face

        # set the twins of edges
        edges_without_twins = list(dcel.edges)
        for edge in edges_without_twins:
            edges_without_twins.remove(edge)
            [twin for twin in edges_without_twins if isTwin(edge, twin)]
            edges_without_twins.remove(twin)
            (edge.twin, twin.twin) = (twin, edge)
        return dcel

    def add_vertex(self, vertex):
        """Add a vertex to the DCEL if the vertex doesn't already exists."""
        if (vertex not in self.vertices):
            self.vertices.append(vertex)

    def add_vertices(self, vertices):
        """Add all vertices to the DCEL, while checking if they exist."""
        [self.add_vertex(vertex) for vertex in vertices]

    def __init__(self, vertices=[], edges=[], faces=[]):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices
        self.edges = edges
        self.faces = faces

    def __repr__(self):
        """Print-friendly representation of the DCEL object."""
        return (
            '<DCEL ('
            'vertices = {obj.vertices},\n'
            'edges = {obj.edges},\n'
            'faces = {obj.faces}>'.format(obj=self)
        )
