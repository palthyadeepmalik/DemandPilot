from fastapi import APIRouter

from app.services.decision_support_service import DecisionSupportService

router = APIRouter(
    prefix="/decision-support",
    tags=["Decision Support"]
)


@router.get("/")
def get_decision_support():
    return DecisionSupportService.generate_decisions()