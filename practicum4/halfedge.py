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

    def __init__(self, origin, twin=None, incident_face=None, nxt=None, prev=None):
        """Construct a HalfEdge object."""
        super(HalfEdge, self).__init__()
        self.origin = origin
        self.twin = twin
        self.incident_face = incident_face
        self.nxt = nxt
        self.prev = prev

    def get_destination(self):
        """Get the destination of this half_edge as a vertex."""
        return self.twin.origin

    def get_origin_and_destination(self):
        """Return the origin and destination of the vertex as a list of coordinates."""
        destination = None
        if(self.twin):
            destination = self.twin.origin.coordinates
        return([self.origin.coordinates, destination])

    def __repr__(self):
        """Print-friendly representation of the HalfEdge object."""
        twin_origin = None
        if(self.twin):
            twin_origin = self.twin.origin.coordinates

        incident_face_edge = getattr(self.incident_face, 'outer_component', None)

        nxt_origin = None
        if(self.nxt):
            nxt_origin = self.nxt.origin.coordinates

        prev_origin = None
        if(self.prev):
            prev_origin = self.prev.origin.coordinates
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
                next=nxt_origin,
                prev=prev_origin,
                face=incident_face_edge
            )
        )
