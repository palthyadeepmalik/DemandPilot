from fastapi import APIRouter

from app.services.prediction_service import PredictionService

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"],
)


@router.get("/tomorrow")
def predict_tomorrow():
    return PredictionService.predict_tomorrow()