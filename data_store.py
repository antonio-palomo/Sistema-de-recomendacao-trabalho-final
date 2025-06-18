class DataStore:
    def __init__(self):
        self.user_likes = {}  # {user_id: set(item_ids)}
        self.item_features = {}  # {item_id: list of features}

    def add_user(self, user_id: int):
        self.user_likes.setdefault(user_id, set())

    def add_item(self, item_id: int, features: list):
        self.item_features[item_id] = features

    def update_preferences(self, user_id: int, liked_items: list):
        self.user_likes[user_id] = set(liked_items)

    def get_user_likes(self, user_id: int):
        return self.user_likes.get(user_id, set())

    def get_all_items(self):
        return self.item_features.keys()

    def get_item_features(self, item_id: int):
        return self.item_features.get(item_id, [])
