"""
clase  Queue cola
"""
class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Inicializa la queue.
        """
        self.lista = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self.lista)

    def __iter__(self):
        """
        Crea un iterador para la queue.
        """
        for item in self.lista:
            yield item

    def __str__(self):
        """
        retorna la lista en formato cadena

        """
        return str(self.lista)
    #encolar
    def agregarAlaCola(self, item):
        '''
        agrega un elem a la queue cola
        '''
        self.lista.append(item)

    def extraerDeLaCola(self):
        '''
        elimina el primer elemento de la queue

        '''
        return self.lista.pop(0)

    def limpiar(self):
        '''
        elimina todos los elem de la queue

        '''
        self.lista=[]
