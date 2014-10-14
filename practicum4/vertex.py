"""The class vertex."""
import pdb


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

    def __repr__(self):
        # TODO Outgoing edge representeren als de origin en destination van die vertex.
        """Print-friendly representation of the Vertex object."""
        incident_edge_points = None
        if(self.incident_edge):
            incident_edge_points = self.incident_edge.as_points()
        return (
            '<Vertex ('
            'coordinates = {obj.coordinates}, '
            'incident_edge = {incident_edge_points}>'
            .format(
                obj=self,
                incident_edge_points=incident_edge_points
            )
        )
