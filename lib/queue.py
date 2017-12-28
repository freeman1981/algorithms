class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return not bool(self.__items)

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    @classmethod
    def from_iterable(cls, iterable):
        inst = cls()
        for item in iterable:
            inst.enqueue(item)
        return inst
