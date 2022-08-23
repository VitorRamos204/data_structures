from node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
    def push(self, elem):
        node = Node()
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = self.node
        if self.first is None:
            self.first = node
        self._size = self._size + 1
    def pop(self):
        if self.first is None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
    raise IndexError('The queue is empty')

    def peek(self):
        if self.first is None:
            elem = self.first.data
            return elem
        raise IndexError('The queue is empty')

    def __len__(self):


    def __repr__(self):


    def __str__(self):



if __name__ == '__main__':
    lista = Queue()

