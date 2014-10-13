"""The class halfEdge."""


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

    def __init__(self, origin, twin=None, incident_face, nxt, prev):
        """Construct a HalfEdge object."""
        super(HalfEdge, self).__init__()
        self.origin = origin
        self.twin = twin
        self.incident_face = incident_face
        self.nxt = nxt
        self.previous = prev

    def get_destination(self):
        """Get the destination of this half_edge."""
        return self.twin.origin

    def get_origin_and_destination(self):
        """Return the origin and destination of the vertex as two points."""
        destination = None
        if(self.twin):
            destination = self.twin.origin.coordinates
        return([self.origin.coordinates, destination])
