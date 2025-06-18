from fastapi import FastAPI, HTTPException
from app.recommender import RecommenderSystem
from app.schemas import (
    RecommendationRequest, RecommendationResponse,
    UserPreferences, NewItem
)

app = FastAPI(title="Sistema de Recomendação")

recommender = RecommenderSystem()

@app.post("/recommend", response_model=RecommendationResponse)
def get_recommendations(request: RecommendationRequest):
    user_id = request.user_id
    recommendations = recommender.recommend(user_id, n=request.n)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Usuário não encontrado ou sem recomendações.")
    return RecommendationResponse(user_id=user_id, recommendations=recommendations)

@app.post("/user/{user_id}")
def add_user(user_id: int):
    recommender.add_user(user_id)
    return {"message": f"Usuário {user_id} adicionado com sucesso."}

@app.post("/item")
def add_item(item: NewItem):
    recommender.add_item(item.item_id, item.features)
    return {"message": f"Item {item.item_id} adicionado com sucesso."}

@app.put("/user/preferences")
def update_preferences(pref: UserPreferences):
    recommender.update_preferences(pref.user_id, pref.liked_items)
    return {"message": f"Preferências do usuário {pref.user_id} atualizadas."}
