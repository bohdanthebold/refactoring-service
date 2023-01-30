from storages.data_repositories import BookDataRepository


class BookService:
    def __init__(self, data_repository=None):
        self._data_repository = data_repository

    @property
    def data_repository(self):
        if self._data_repository is None:
            self._data_repository = BookDataRepository()
        return self._data_repository

    def add_item_and_get_all(self, book_id):
        self.data_repository.add(book_id)
        return self.data_repository.get_all()
