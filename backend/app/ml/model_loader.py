import joblib
from pathlib import Path

ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "demand_model.pkl"
PREPROCESSOR_PATH = ARTIFACTS_DIR / "preprocessor.pkl"


class ModelLoader:

    _model = None
    _preprocessor = None

    @classmethod
    def get_model(cls):

        if cls._model is None:
            cls._model = joblib.load(MODEL_PATH)

        return cls._model

    @classmethod
    def get_preprocessor(cls):

        if cls._preprocessor is None:
            cls._preprocessor = joblib.load(PREPROCESSOR_PATH)

        return cls._preprocessor