class DB:
    # Fake db
    def __init__(self):
        self._user_items = [
            {"title": "1 item", "is_published": True},
            {"title": "2 item", "is_published": False},
            {"title": "3 item", "is_published": False},
            {"title": "4 item", "is_published": True},
        ]

        self._user_ids = {"John": 12, "Anna": 2, "Jack": 10}

        self._book_ids = []



        self._keys = ["key1", "key2", "key3", "key4"]

    @property
    def user_items(self):
        return self._user_items

    @property
    def user_ids(self):
        return self._user_ids

    @property
    def book_ids(self):
        return self._book_ids

    @property
    def keys(self):
        return self._keys