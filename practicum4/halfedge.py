"""The class halfEdge."""
import pdb
from vertex import Vertex


class HalfEdge(object):

    """
    Class to represent an half edge.

    Properties:
        - origin: origin of the edge.
        - twin: half-edge between the same vertices but in the other direction.
        - incident_face: face to the left of this edge when it is travelled
            from its origin to its destination.
        - nxt: next edge on the boundary of this.incident_face
        - prev: previous edge on the boundary of this.incident_face



    """

    def __init__(self, origin, twin=None, incident_face=None, nxt=None, prev=None):
        """Construct a HalfEdge object."""
        super(HalfEdge, self).__init__()
        self.origin = origin
        self.twin = twin
        self.incident_face = incident_face
        self.nxt = nxt
        self.prev = prev

    def as_points(self):
        """Return the edge as the coordinates of the origin and destination."""
        return [self.origin.coordinates, self.twin.origin.coordinates]

    def get_destination(self):
        """Return the destination of the halfedge as a vertex."""
        return self.twin.origin

    def __repr__(self):
        """Print-friendly representation of the HalfEdge object."""
        # pdb.set_trace()
        twin_origin = self.twin.as_points()

        incident_face_edge = None
        if(self.incident_face):
            incident_face_edge = self.incident_face.outer_component.as_points()

        nxt_edge = None
        if(self.nxt):
            nxt_edge = self.nxt.as_points()

        prev_edge = None
        if(self.prev):
            prev_edge = self.prev.as_points()

        return (
            '<HalfEdge ('
            'origin = {obj.origin.coordinates}, '
            'twin = {twin}, '
            'nxt = {next}, '
            'prev = {prev}, '
            'incident_face = {face}>'
            .format(
                obj=self,
                twin=twin_origin,
                next=nxt_edge,
                prev=prev_edge,
                face=incident_face_edge
            )
        )

    def __eq__(self, other):
        """Check if two half edges are equal."""
        if type(other) is type(self):
                return (
                    self.origin == other.origin and
                    self.twin.origin == other.twin.origin
                )
        return False

    def __neq__(self, other):
        """Check if two objects are not equal."""
        return not self.__eq__(other)
