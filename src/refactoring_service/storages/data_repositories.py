from abc import ABC


class DataRepository(ABC):
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def get_all(self):
        return self.items

    def get_by_id(self, id_):
        return self._items[id_]

    def add(self, item):
        self.items.append(item)


class BookDataRepository(DataRepository):
    pass
