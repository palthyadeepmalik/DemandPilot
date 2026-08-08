from app.ml.dataset import load_training_dataset
from app.ml.feature_engineering import create_features
from app.ml.preprocessing import preprocess

df = load_training_dataset()

df = create_features(df)

X_train, X_test, y_train, y_test, preprocessor = preprocess(df)

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)
print("Train Labels   :", y_train.shape)
print("Test Labels    :", y_test.shape)