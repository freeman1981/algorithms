from lib.node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def _compare(item, current_item):
        return item < current_item

    def is_empty(self):
        return self.head is None

    def add(self, item):
        current = self.head
        new_node = Node(item)
        if current is None:
            self.head = new_node
            return
        previous = None
        while current is not None:
            if self._compare(item, current.get_data()):
                new_node.set_next(current)
                if previous is not None:
                    previous.set_next(new_node)
                else:
                    self.head = new_node
                return
            previous = current
            next_ = current.get_next()
            if next_ is None:
                current.set_next(new_node)
                return
            current = next_

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if not self._compare(item, current.get_data()):
                return False
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while True:
            if current is None:
                raise ValueError('No {} in list'.format(item))
            if current.get_data() == item:
                break
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    @classmethod
    def from_iterable(cls, iterable):
        inst = cls()
        for item in iterable:
            inst.add(item)
        return inst
