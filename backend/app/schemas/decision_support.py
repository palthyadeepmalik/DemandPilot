from pydantic import BaseModel, Field


class DecisionSupportRequest(BaseModel):
    pizza_type_id: str
    hour: int = Field(..., ge=0, le=23)
    day_of_week: str
    month: int = Field(..., ge=1, le=12)
    weekend: bool
    category: str
    size: str


class IngredientRecommendation(BaseModel):
    ingredient: str
    required: float
    available: float
    purchase: float
    unit: str


class DecisionSupportResponse(BaseModel):
    predicted_quantity: float
    ingredients: list[IngredientRecommendation]