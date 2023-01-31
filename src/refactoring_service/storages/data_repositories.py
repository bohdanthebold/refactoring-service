from abc import ABC


class DataRepository(ABC):
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    def get_all(self):
        return self.items

    def get_by_id(self, id_):
        return self._items[id_]

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)


class BookDataRepository(DataRepository):
    pass


class KeyDataRepository(DataRepository):
    pass


class UserItemsDataRepository(DataRepository):
    def filter(self, is_published=True):
        return [item for item in self.items if item["is_published"] == is_published]


class UserDataRepository(DataRepository):
    pass


class KeyDataRepository(DataRepository):
    pass
