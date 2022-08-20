from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        # Inserção quando a lista já possui elementos
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            # Primeira inserção
            self.head = Node(element)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista."""
        return self._size

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o índice do elemento na lista."""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')


lista = LinkedList()
