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

    def __repr__(self):
        """Print-friendly representation of the Vertex object."""
        incident_edge_vertices = None
        if(self.incident_edge):
            incident_edge_vertices = self.incident_edge.get_origin_and_destination()
        return (
            '<Vertex ('
            'coordinates = {obj.coordinates}, '
            'incident_edge = {incident_edge_vertices}>'
            .format(
                obj=self,
                incident_edge_vertices=incident_edge_vertices
            )
        )
