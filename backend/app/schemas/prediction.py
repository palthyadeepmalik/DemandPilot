from datetime import date

from pydantic import BaseModel


class PredictionRequest(BaseModel):

    pizza_id: str
    prediction_date: date


class PredictionResponse(BaseModel):

    pizza_id: str
    prediction_date: date
    predicted_quantity: float