import joblib
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from app.ml.dataset import load_training_dataset
from app.ml.feature_engineering import create_features
from app.ml.preprocessing import preprocess


ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok=True)


def train_model():

    print("Loading dataset...")
    df = load_training_dataset()

    print("Creating features...")
    df = create_features(df)

    print("Preprocessing...")
    X_train, X_test, y_train, y_test, _ = preprocess(df)

    print("Training Random Forest...")

    model = RandomForestRegressor(
        n_estimators=30,
        max_depth=12,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print("\n========== MODEL METRICS ==========")
    print(f"MAE  : {mae:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")

    joblib.dump(
        model,
        ARTIFACTS_DIR / "demand_model.pkl",
        compress=3
    )

    print("\nModel saved successfully!")


if __name__ == "__main__":
    train_model()