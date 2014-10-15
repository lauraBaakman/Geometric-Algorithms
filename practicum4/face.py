"""The class face."""
import pdb


class Face(object):

    """
    Class to represent a face.

    Properties:
        - outer_component: half edge on its outer boundary when traversed
        counter clockwise.
        - inner_components: list of half edges, on of each of the holes in the face.
            None if the face does not have any hole.s
    """

    def __init__(self, outer_component, inner_components=[]):
        """Construct a Face object."""
        super(Face, self).__init__()
        self.outer_component = outer_component
        self.inner_components = inner_components

    def number_of_vertices(self):
        """Return the number of vertices that define the face."""
        def number_of_vertices_helper(current_edge):
            if(self.outer_component == current_edge):
                return 1
            else:
                return 1 + number_of_vertices_helper(current_edge.nxt)
        return number_of_vertices_helper(self.outer_component.nxt)

    def get_edges(self):
        """Return all edges of this face in CCW order."""
        def get_edges_helper(current_edge, edges):
            if(self.outer_component == current_edge):
                pdb.set_trace()
                return edges
            else:
                edges.append(current_edge)
                return get_edges_helper(current_edge.nxt, edges)
        return get_edges_helper(self.outer_component.nxt, [self.outer_component])

    def __repr__(self):
        """Print-friendly representation of the Face object."""
        return (
            '<Face ('
            'outer_component = {obj.outer_component},\t '
            'inner_components = {inners}>'
            .format(
                obj=self,
                inners=[c.as_points() for c in self.inner_components]
            )
        )
