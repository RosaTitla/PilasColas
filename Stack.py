class Stack:
    def __init__(self):
        """
        Initialize the stack.
        """
        self.lista = []

    def __len__(self):
        """
        Return the number of items in the stack.
        """
        return len(self.lista)

    def __iter__(self):
        """
        Create an iterator for the stack.
        """
        for item in self.lista:
            yield item

            """ yield se usa para regresar un valor desde una función
                sin destruir los estados de su variable local
                y cuando se llama a la función,
                la ejecución comienza desde la última declaración 
                de yield. Cualquier función que contenga yield
                se denomina generador.
            """

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        return str(self.lista)

    def apilar(self, item):
        '''
        agrega un elem a la stack
        '''
        self.lista.append(item)

    def desapilar(self):
        '''
        elimina el elem de la pila stack
        '''
        return self.lista.pop()

    def limpiarPila(self):
        '''
        elimina todos los elem de la stack

        '''
        self.lista=[]
