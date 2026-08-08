import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create ML features from the aggregated demand dataset.
    """

    df = df.copy()

    # Ensure datetime
    df["date"] = pd.to_datetime(df["date"])

    # Calendar Features
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    df["week"] = df["date"].dt.isocalendar().week.astype(int)
    df["month"] = df["date"].dt.month
    df["quarter"] = df["date"].dt.quarter
    df["year"] = df["date"].dt.year

    # Weekend
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

    return df