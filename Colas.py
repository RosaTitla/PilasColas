"""
Queue class
"""
class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        '''
        agrega un elem a la queue
        '''
        self._items.append(item)

    def dequeue(self):
        '''
        elimina un elem de la queue

        '''
        return self._items.pop(0)

    def limpiar(self):
        '''
        elimina todos los elem de la queue

        '''
        self._items=[]
