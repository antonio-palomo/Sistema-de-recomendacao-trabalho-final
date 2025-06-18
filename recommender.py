import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from data_store import DataStore

class RecommenderSystem:
    def __init__(self):
        self.store = DataStore()

    def recommend(self, user_id: int, n: int = 5) -> list:
        liked_items = self.store.get_user_likes(user_id)
        if not liked_items:
            return []

        liked_features = np.array([self.store.get_item_features(i) for i in liked_items if self.store.get_item_features(i)])
        if liked_features.size == 0:
            return []

        liked_centroid = liked_features.mean(axis=0).reshape(1, -1)

        candidates = [i for i in self.store.get_all_items() if i not in liked_items and self.store.get_item_features(i)]
        candidate_features = np.array([self.store.get_item_features(i) for i in candidates])

        if candidate_features.size == 0:
            return []

        similarities = cosine_similarity(candidate_features, liked_centroid).flatten()
        ranked = sorted(zip(candidates, similarities), key=lambda x: x[1], reverse=True)

        return [item for item, _ in ranked[:n]]

    def add_user(self, user_id: int):
        self.store.add_user(user_id)

    def add_item(self, item_id: int, features: list):
        self.store.add_item(item_id, features)

    def update_preferences(self, user_id: int, liked_items: list):
        self.store.update_preferences(user_id, liked_items)
