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
        def add_containing_face_to_dcel():
            containing_face_edges = [edge for edge in dcel.edges if not edge.nxt]
            edge = containing_face_edges.pop()
            face = Face(edge)
            dcel.faces.append(face)
            pdb.set_trace()
            first_edge = edge
            previous_edge = [
                e for e in containing_face_edges if e.get_destination() == edge.origin
            ]
            edge.prev = previous_edge[0]
            while len(containing_face_edges) > 1:
                edge.incident_face = face
                next_edge = [
                    e for e in containing_face_edges if e.origin == edge.get_destination()
                ]
                edge.nxt = next_edge[0]
                next_edge[0].prev = edge
                edge = next_edge[0]
                containing_face_edges.remove(next_edge[0])
            edge_2 = containing_face_edges.pop()
            edge.incident_face = face
            edge_2.incident_face = face
            edge_2.prev = edge
            edge_2.nxt = first_edge
            edge.nxt = edge_2
            pdb.set_trace()

        def add_triangle_edges():
            triangles_edges = []
            for vertex_idx, origin in enumerate(triangle_vertices):
                # Destination of the edge in this triangle that has vertex as origin
                destination = triangle_vertices[(vertex_idx + 1) % 3]
                edge_1 = HalfEdge(origin)
                edge_2 = HalfEdge(destination, twin=edge_1)
                edge_1.twin = edge_2
                edge_1 = dcel.add_edge(edge_1)
                edge_2.twin = edge_1
                edge_2 = dcel.add_edge(edge_2)
                edge_1.twin = edge_2
                triangles_edges.append(edge_1)

            triangle_face = Face(triangles_edges[0])
            dcel.faces.append(triangle_face)
            # Set previous and next of the edges
            for edge_idx, edge in enumerate(triangles_edges):
                edge.nxt = triangles_edges[(edge_idx + 1) % 3]
                edge.prev = triangles_edges[(edge_idx + 3 - 1) % 3]
                edge.incident_face = triangle_face
                triangle_vertices[edge_idx].incident_edge = edge

        dcel = cls()
        for t in triangles:
            triangle_vertices = [
                dcel.add_vertex(Vertex(x))
                for x in du.get_triangle_vertices(xl, yl, t)
            ]
            add_triangle_edges()
        add_containing_face_to_dcel()
        return dcel

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
            'vertices:\n {obj.vertices},\n'
            'edges:\n {obj.edges},\n'
            'faces:\n {obj.faces}>'.format(obj=self)
        )
