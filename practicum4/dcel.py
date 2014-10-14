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
        dcel = cls()

        for t in triangles:
            # Add vertices of the triangle
            triangle_vertices = [
                dcel.add_vertex(Vertex(x))
                for x in du.get_triangle_vertices(xl, yl, t)
            ]

            # Add edges of the triangle
            triangle_edges = []
            for vertex_idx, origin in enumerate(triangle_vertices):
                # Destination of the edge in this triangle that has vertex as origin
                destination = triangle_vertices[(vertex_idx + 1) % 3]
                edge = dcel.add_edge(HalfEdge(origin, twin=destination))
                triangle_edges.append(edge)

            triangle_face = Face(triangle_edges[0])
            for edge_idx, edge in enumerate(triangle_edges):
                edge.nxt = triangle_edges[(edge_idx + 1) % 3]
                edge.prev = triangle_edges[(edge_idx + 3 - 1) % 3]
                edge.incident_face = triangle_face
                triangle_vertices[edge_idx].incident_edge = edge
            dcel.faces.append(triangle_face)

            # TODO: Fix the twins

            # TODO: containing face
        return dcel

    # def add_edge(self, edge, destination=None):
    #     """Add an edge to the DCEL if the edge doesn't already exist."""
    #     # To compare an edge we need its origin and its twin
    #     if(edge.twin):
    #         try:
    #             edge_idx = self.edges.index(edge)
    #             return self.edges[edge_idx]
    #         except Exception:
    #             self.edges.append(edge)
    #             return edge
    #     elif(destination):
    #         duplicates = [
    #             x for x in self.edges
    #             if (
    #                 x.origin == edge.origin and
    #                 x.twin.origin == destination
    #             )
    #         ]
    #         if(not duplicates):
    #             self.edges.append(edge)
    #             return edge
    #         else:
    #             assert(len(duplicates) == 1)
    #             return duplicates[0]
    #     else:
    #         raise Exception(
    #             'add_edge expects edges that have a'
    #             'twin or that the parameter destination is set.'
    #         )

    def add_edge(self, edge):
        """Add a edge to the DCEL if the edge doesn't already exists."""
        try:
            edge_idx = self.edges.index(edge)
            return self.edges[edge_idx]
        except Exception:
            self.edges.append(edge)
            return edge

    def add_vertex(self, vertex):
        """Add a vertex to the DCEL if the vertex doesn't already exists."""
        try:
            vertex_idx = self.vertices.index(vertex)
            return self.vertices[vertex_idx]
        except Exception:
            self.vertices.append(vertex)
            return vertex

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
