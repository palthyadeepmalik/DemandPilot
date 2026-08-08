from sqlalchemy.orm import Session


class AggregationService:

    def __init__(self, db: Session):
        self.db = db

    def generate_dataset(self):
        pass