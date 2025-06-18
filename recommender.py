import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from data_store import DataStore
import zipfile
import urllib.request

MOVIELENS_URL = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
DATA_DIR = "ml-100k"

GENRES = [
    "Unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime",
    "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
    "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

class RecommenderSystem:
    def __init__(self):
        self.store = DataStore()
        self.load_movielens()

    def download_and_extract(self):
        if not os.path.exists(DATA_DIR):
            zip_path = "ml-100k.zip"
            print("Baixando MovieLens 100k...")
            urllib.request.urlretrieve(MOVIELENS_URL, zip_path)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(".")
            os.rename("ml-100k", DATA_DIR)
            os.remove(zip_path)
            print("Download e extração concluídos.")

    def load_movielens(self):
        self.download_and_extract()

        # Carregar usuários
        with open(f"{DATA_DIR}/u.user", encoding="latin-1") as f:
            for line in f:
                parts = line.strip().split("|")
                user_id = int(parts[0])
                self.store.add_user(user_id)

        # Carregar itens (filmes) e features de gêneros (binário)
        item_features = {}
        with open(f"{DATA_DIR}/u.item", encoding="latin-1") as f:
            for line in f:
                parts = line.strip().split("|")
                item_id = int(parts[0])
                genre_flags = list(map(int, parts[5:24]))  # 19 gêneros
                item_features[item_id] = genre_flags
                self.store.add_item(item_id, genre_flags)

        # Carregar preferências (likes) com base nas avaliações >=4 (bom rating)
        user_likes = {}
        with open(f"{DATA_DIR}/u.data", encoding="latin-1") as f:
            for line in f:
                user_id, item_id, rating, _ = line.strip().split("\t")
                user_id = int(user_id)
                item_id = int(item_id)
                rating = int(rating)
                if rating >= 4:
                    user_likes.setdefault(user_id, set()).add(item_id)

        for user_id, liked_items in user_likes.items():
            self.store.update_preferences(user_id, list(liked_items))

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
