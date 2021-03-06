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
        """Return the destination of the halfedge as a vertex."""
        return self.twin.origin

    def __eq__(self, other):
        """Check if two half edges are equal."""
        if type(other) is type(self):
            origin_destination_check = (
                self.origin == other.origin and
                self.twin.origin == other.twin.origin
            )
            if self.incident_face and other.incident_face:
                return (
                    origin_destination_check and
                    self.incident_face == other.incident_face
                )
            return origin_destination_check
        return False

    def __neq__(self, other):
        """Check if two objects are not equal."""
        return not self.__eq__(other)

    def as_points(self):
        """Return the edge as the coordinates of the origin and destination."""
        return [self.origin.coordinates, self.twin.origin.coordinates]

    def is_finite(self):
        """Return true if the edge has two defined vertices that are not inf."""
        infinity = float('inf')
        [[x1, y1], [x2, y2]] = self.as_points()
        return (
            x1 != infinity and y1 != infinity and
            x2 != infinity and y2 != infinity
        )

    def get_incident_face(self):
        """Return the edges and vertices of the incident face."""
        def get_incident_face_helper(current_edge, edges, vertices):
            if(self == current_edge):
                return (edges, vertices)
            else:
                edges.append(current_edge)
                vertices.append(current_edge.origin)
                return get_incident_face_helper(current_edge.nxt, edges, vertices)
        return get_incident_face_helper(self.nxt, [self], [self.origin])

    def __repr__(self):
        """Print-friendly representation of the HalfEdge object."""
        twin_origin = None
        coordinates = self.origin
        if(self.twin):
            twin_origin = self.twin.as_points()
            coordinates = self.as_points()

        incident_face_edge = None
        if(self.incident_face):
            if(self.incident_face.circumcentre):
                incident_face_edge = self.incident_face.circumcentre
            elif(self.incident_face.outer_component):
                incident_face_edge = self.incident_face.outer_component.as_points()
            else:
                incident_face_edge = [c.as_points() for c in self.incident_face.inner_components]

        nxt_edge = None
        if(self.nxt):
            nxt_edge = self.nxt.as_points()

        prev_edge = None
        if(self.prev):
            prev_edge = self.prev.as_points()

        return (
            '<HalfEdge ('
            'origin = {coordinates}, \n'
            # 'twin = {twin}, '
            'nxt = {next}, \n'
            'prev = {prev}, \n\n'
            # 'incident_face = {face}>\n'
            .format(
                coordinates=coordinates,
                # twin=twin_origin,
                next=nxt_edge,
                prev=prev_edge,
                face=incident_face_edge
            )
        )
