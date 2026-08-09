from fastapi import FastAPI
from sqlalchemy import text

from app.database.session import engine

from app.database.init_db import create_tables

from app.api.import_api import router as import_router

from app.api.analytics_api import router as analytics_router

from app.api.prediction_api import router as prediction_router

from app.api.decision_support_api import router as decision_support_router

from app.api.inventory_api import router as inventory_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "https://demand-pilot-eight.vercel.app",
    ],
    allow_origin_regex=r"https://demand-pilot-.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
create_tables()

app.include_router(import_router)
app.include_router(analytics_router)
app.include_router(prediction_router)
app.include_router(decision_support_router)
app.include_router(inventory_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to DemandPilot 🚀"
    }


@app.get("/db-test")
def test_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "success",
            "message": "Connected to PostgreSQL successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


