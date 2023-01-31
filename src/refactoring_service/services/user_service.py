from storages.data_repositories import UserDataRepository, UserItemsDataRepository, KeyDataRepository
from db.db import DB

class UserService:

    def __init__(self,key_data_repository=None, user_data_repository=None, user_items_data_repository=None):
        self._user_items_data_repository = user_items_data_repository
        self._user_data_repository = user_data_repository
        self._key_data_repository = key_data_repository


    @property
    def user_items_data_repository(self):
        if self._user_items_data_repository is None:
            self._user_items_data_repository = UserItemsDataRepository(DB().user_items)
        return self._user_items_data_repository

    @property
    def user_data_repository(self):
        if self._user_data_repository is None:
            self._user_data_repository = UserDataRepository(DB().user_ids)
        return self._user_data_repository

    @property
    def key_data_repository(self):
        if self._key_data_repository is None:
            self._key_data_repository = KeyDataRepository(DB().keys)
        return self._key_data_repository

    def is_valid_user(self, name, age, job):
        if age >= 30 and name == "Ahmed" and job == "data scientist":
            return True
        return False

    def get_user_items(self):
        self.user_items_data_repository.get_all()

    def filter_items(self, is_published):
        return self.user_items_data_repository.filter(is_published=is_published)

    def get_user_ids(self):
        return self.user_data_repository.get_all()

    def get_key_by_id(self, key_id):
        id_ = key_id - 1
        return self.key_data_repository.get_by_id(id_) if self.key_data_repository.count() > id_ else None

