from pydantic import BaseModel
from typing import List, Optional

class RecommendationRequest(BaseModel):
    user_id: int
    n: int = 5

class RecommendationResponse(BaseModel):
    user_id: int
    recommendations: List[int]

class UserPreferences(BaseModel):
    user_id: int
    liked_items: List[int]

class NewItem(BaseModel):
    item_id: int
    features: List[float]
