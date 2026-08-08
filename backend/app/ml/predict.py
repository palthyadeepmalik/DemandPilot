import pandas as pd

from app.ml.feature_engineering import create_features
from app.ml.model_loader import ModelLoader


def predict_demand(df: pd.DataFrame):

    model = ModelLoader.get_model()
    preprocessor = ModelLoader.get_preprocessor()

    df = create_features(df)

    prediction_df = df.copy()

    X = prediction_df.drop(
        columns=[
            "date",
            "pizza_type_id"
        ]
    )

    X_processed = preprocessor.transform(X)

    predictions = model.predict(X_processed)

    prediction_df["predicted_quantity"] = (
        predictions
        .round()
        .astype(int)
    )

    return prediction_df