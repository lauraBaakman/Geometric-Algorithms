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
    def from_delaunay_triangulation(xl, yl, edgs, triPts, neighs):
        """ Construct a DCEL from the output of matplotlib.delaunay.delaunay. """
        triangle_queue = Queue(0)
        while not(triangle_queue.is_empty()):

            triangle_queue.enqueue(p)

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
