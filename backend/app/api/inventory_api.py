from fastapi import APIRouter
from app.services.inventory_service import InventoryService

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.get("/")
def inventory():

    return InventoryService.calculate_inventory()