"""Module with unit tests for the dcel module."""
import unittest
import pdb
from dcel import *


class Test_queue(unittest.TestCase):

    """Unit tests for the class queue in the module dcel."""

    def setUp(self):
        """."""
        self.p = 0
        self.queue = Queue(self.p)
        pass

    def test_constructor(self):
        """."""
        self.assertItemsEqual(self.queue._queue, [self.p])
        self.assertItemsEqual(self.queue._old_elements, [self.p])

    def test_enqueue(self):
        """Enqueue one previously unseen element."""
        p1 = 7
        self.queue.enqueue(7)
        self.assertItemsEqual(self.queue._queue, [self.p, p1])
        self.assertItemsEqual(self.queue._old_elements, [self.p, p1])

    def test_enqueue_2(self):
        """Enqueue one element that is already in the queue."""
        p1 = 7
        p2 = 0
        self.queue.enqueue(p1)
        self.queue.enqueue(p2)
        self.assertItemsEqual(self.queue._queue, [self.p, p1])
        self.assertItemsEqual(self.queue._old_elements, [self.p, p1])

    def test_dequeue(self):
        """."""
        p1 = 7
        self.queue.enqueue(p1)
        self.assertEqual(self.queue.dequeue(), self.p)
        self.assertItemsEqual(self.queue._queue, [p1])
        self.assertItemsEqual(self.queue._old_elements, [self.p, p1])

    def test_enqueue_3(self):
        """Enqueue one element that was previously in the queue."""
        p1 = 7
        p2 = 0
        self.queue.enqueue(p1)
        self.queue.dequeue()
        self.queue.enqueue(p2)
        self.assertItemsEqual(self.queue._queue, [p1])
        self.assertItemsEqual(self.queue._old_elements, [self.p, p1])

    def test_is_empty_filled_queue(self):
        """."""
        self.assertFalse(self.queue.is_empty())

    def test_is_empty_empty_queue(self):
        """."""
        self.assertEqual(self.queue.dequeue(), self.p)
        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
