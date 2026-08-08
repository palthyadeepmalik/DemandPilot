import joblib
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok=True)


def preprocess(df):

    target = "quantity"

    X = df.drop(columns=["quantity", "date"])
    y = df[target]

    categorical_features = [
        "pizza_id",
        "category",
        "size"
    ]

    numerical_features = [
        "day",
        "day_of_week",
        "week",
        "month",
        "quarter",
        "year",
        "is_weekend"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "num",
                "passthrough",
                numerical_features
            )
        ]
    )

    X_processed = preprocessor.fit_transform(X)

    print("Artifacts directory:", ARTIFACTS_DIR)
    print("Saving preprocessor...")

    joblib.dump(
        preprocessor,
        ARTIFACTS_DIR / "preprocessor.pkl"
    )

    print("Preprocessor saved successfully!")

    X_train, X_test, y_train, y_test = train_test_split(
        X_processed,
        y,
        test_size=0.2,
        random_state=42
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )