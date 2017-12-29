class Stack:

    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return not bool(self.__items)

    @classmethod
    def from_iterable(cls, iterable):
        inst = cls()
        for item in iterable:
            inst.push(item)
        return inst
