"""Classes to represent a DCEL."""
import pdb
# from face import Face
# from halfedge import HalfEdge
# from vertex import Vertex


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
        """ Construct a DCEL from the output of matplotlib.delaunay.delaunay. """
        def first_triangle():
            return None

        def get_CCW_edges():
            return None

        triangle_queue = Queue(0)
        while not(triangle_queue.is_empty()):
            current_triangle = triangle_queue.dequeue()

            # Add the neighbours to the queue
            triangle_queue.enqueue(
                [x for x in neighs[current_triangle] if not(x == -1)]
            )

            if(not current_triangle):
                edges = first_triangle()
            else:
                # Find neighbouring edge that is in triangulation
                edges = get_CCW_edges()
            print edges

    def __init__(self, vertices, edges, faces):
        """Construct a DCEL object."""
        super(DCEL, self).__init__()
        self.vertices = vertices
        self.edges = edges
        self.faces = faces


class Queue(object):

    """
    Quick and dirty queue that contains elements only once.

    That last requirement made using deque from collections
    impossible.
    """

    def __init__(self, p):
        """Construct a DCEL object."""
        super(Queue, self).__init__()
        self._queue = list()
        self._queue.append(p)
        self._old_elements = list()
        self._old_elements.append(p)

    def dequeue(self):
        """Dequeue the next object, returns none if the queue is empty."""
        try:
            p = self._queue.pop(0)
        except IndexError:
            return None
        return p

    def enqueue(self, p):
        """Enqueue the next object(s)."""
        if(isinstance(p, list)):
            for element in p:
                self.enqueue(element)
        else:
            if(not (p in self._old_elements)):
                self._queue.append(p)
                self._old_elements.append(p)

    def is_empty(self):
        """Return true if the queue is empty."""
        return (len(self._queue) == 0)

    def __repr__(self):
        """Print-friendly representation of the Queue object."""
        return (
            '<Queue : {obj._queue}>'.format(obj=self)
        )

if __name__ == '__main__':
    xl = [0, 2, 2, 1]
    yl = [4, 4, 2, 2, 1]
    edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 0]]
    triangles = [[0, 1, 2], [0, 2, 3]]
    neighs = [[1, -1, -1], [0, -1, -1]]
    d = DCEL.from_delaunay_triangulation(xl, yl, edges, triangles, neighs)
