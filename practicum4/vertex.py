"""The class vertex."""


class Vertex(object):

    """
    Class to represent a vertex.

    Properties:
        - coordinates: a list with two points, each of which is a list of two points.
        - incident_edge: random half edge that has this vertex as its origin.
    """

    def __init__(self, coordinates, incident_edge=None):
        """Construct a Vertex object."""
        super(Vertex, self).__init__()
        self.coordinates = coordinates
        self.incident_edge = incident_edge

    def __eq__(self, other):
        """Chekc if two objects are equal by comparing only their coordinates."""
        if type(other) is type(self):
            return(
                self.coordinates[0] == other.coordinates[0] and
                self.coordinates[1] == other.coordinates[1]
            )
        return False

    def __neq__(self, other):
        """Check if two objects are not equal."""
        return not self.__eq__(other)

    def as_points(self):
        """Return the vertex as a set of points."""
        return self.coordinates

    def is_infinity(self):
        """Return true if the coordinates of this point are infinity,infinity."""
        infinity = float('inf')
        return self.coordinates[0] == infinity and self.coordinates[1] == infinity

    def __repr__(self):
        """Print-friendly representation of the Vertex object."""
        incident_edge_points = None
        if(self.incident_edge):
            incident_edge_points = self.incident_edge.as_points()
        return (
            '<Vertex ('
            'coordinates = {obj.coordinates},\t'
            'incident_edge = {incident_edge_points}>\n'
            .format(
                obj=self,
                incident_edge_points=incident_edge_points
            )
        )
