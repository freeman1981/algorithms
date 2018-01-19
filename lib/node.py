class Node:
    def __init__(self, init_data):
        self._data = init_data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self._data = new_data

    def set_next(self, new_next):
        self._next = new_next
