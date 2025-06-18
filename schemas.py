from pydantic import BaseModel
from typing import List, Dict

class RecommendationRequest(BaseModel):
    user_id: int
    n: int = 5  # Quantidade de recomendações

class RecommendationResponse(BaseModel):
    user_id: int
    recommendations: List[int]

class UserPreferences(BaseModel):
    user_id: int
    liked_items: List[int]

class NewItem(BaseModel):
    item_id: int
    features: Dict[str, float]  # Ou o formato que sua feature tiver
