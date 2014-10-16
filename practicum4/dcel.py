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
    def from_delaunay_triangulation(cls, xl, yl, triangles, circumcentres):
        """ Construct a DCEL from the output of matplotlib.delaunay.delaunay."""
        def add_containing_face_to_dcel():
            containing_face_edges = [edge for edge in dcel.edges if not edge.nxt]
            edge = containing_face_edges.pop()
            face = Face(outer_component=None, inner_components=[edge])
            dcel.faces.append(face)
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

        def add_triangle_edges(circumcentre):
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

            triangle_face = Face(triangles_edges[0], circumcentre=list(circumcentre))
            dcel.faces.append(triangle_face)
            # Set previous and next of the edges
            for edge_idx, edge in enumerate(triangles_edges):
                edge.nxt = triangles_edges[(edge_idx + 1) % 3]
                edge.prev = triangles_edges[(edge_idx + 3 - 1) % 3]
                edge.incident_face = triangle_face
                triangle_vertices[edge_idx].incident_edge = edge

        dcel = cls()
        for t_idx, t in enumerate(triangles):
            triangle_vertices = [
                dcel.add_vertex(Vertex(x))
                for x in du.get_triangle_vertices(xl, yl, t)
            ]
            add_triangle_edges(circumcentres[t_idx])
        add_containing_face_to_dcel()
        return dcel

    def add_edge(self, edge):
        """Add an edge to DCEL if it doesn't already exists, otherwise return the existing edge."""
        try:
            edge_idx = self.edges.index(edge)
            return self.edges[edge_idx]
        except Exception:
            self.edges.append(edge)
            return edge

    def add_vertex(self, vertex):
        """Add vertex to DCEL if it doesn't already exists, otherwise return the existing vertex."""
        try:
            vertex_idx = self.vertices.index(vertex)
            # print "{} already in {}".format(vertex, self.vertices)
            return self.vertices[vertex_idx]
        except Exception:
            self.vertices.append(vertex)
            # print "adding {} to {}".format(vertex, self.vertices)
            return vertex

    def __init__(self, vertices=None, edges=None, faces=None):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices or []
        self.edges = edges or []
        self.faces = faces or []

    def get_bounded_faces(self):
        """Return all faces where the circumcentre is not infinity."""
        return [face for face in self.faces if face.is_bounded()]

    def add_face(self, face):
        """Add a face to DCEL if it doesn't already exists, otherwise return the existing face."""
        try:
            face_idx = self.faces.index(face)
            return self.faces[face_idx]
        except Exception:
            self.faces.append(face)
            return face

    def dual(self):
        """Return the dual of the current DCEL."""
        def set_twins():
            for edge_idx in range(0, len(dual_dcel.edges), 2):
                dual_dcel.edges[edge_idx].twin = dual_dcel.edges[edge_idx + 1]
                dual_dcel.edges[edge_idx + 1].twin = dual_dcel.edges[edge_idx]

        def set_next_and_previous():
            for face in dual_dcel.faces:
                face_edges = [edge for edge in dual_dcel.edges if edge.incident_face == face]
                for edge in face_edges:
                    pdb.set_trace()
                    if(not edge.get_destination().is_infinity()):
                        edge.nxt = [e for e in face_edges if e.origin == edge.get_destination()][0]
                    if(not edge.origin.is_infinity()):
                        edge.prev = [e for e in face_edges if edge.origin == e.get_destination()][0]
                    pdb.set_trace()

        dual_dcel = DCEL()
        for edge in self.edges:
            incident_face = dual_dcel.add_face(Face(circumcentre=edge.twin.origin.as_points()))
            origin = dual_dcel.add_vertex(Vertex(coordinates=edge.incident_face.circumcentre))
            dual_edge = HalfEdge(
                origin=origin,
                incident_face=incident_face
            )
            incident_face.outer_component = dual_edge
            origin.incident_edge = dual_edge
            dual_dcel.edges.append(dual_edge)

        set_twins()
        set_next_and_previous()
        return dual_dcel

    def __repr__(self):
        """Print-friendly representation of the DCEL object."""
        return (
            '<DCEL ('
            'vertices:\n {obj.vertices},\n'
            'edges:\n {obj.edges},\n'
            'faces:\n {obj.faces}>'.format(obj=self)
        )
