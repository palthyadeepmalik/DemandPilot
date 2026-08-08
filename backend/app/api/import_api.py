from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.csv_import_service import CSVImportService

router = APIRouter(prefix="/import", tags=["Import"])


@router.post("/")
def import_dataset(db: Session = Depends(get_db)):
    service = CSVImportService(db)
    return service.import_data()