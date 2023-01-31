from storages.data_repositories import BookDataRepository
from db.db import DB


class BookService:
    def __init__(self, data_repository=None):
        self._data_repository = data_repository

    @property
    def data_repository(self):
        if self._data_repository is None:
            self._data_repository = BookDataRepository(DB().book_ids)
        return self._data_repository

    def add_item_and_get_all(self, book_id):
        self.data_repository.add(book_id)
        return self.data_repository.get_all()
