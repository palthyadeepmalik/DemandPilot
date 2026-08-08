from app.ml.dataset import load_training_dataset

df = load_training_dataset()

print(df.head())

print()

print(df.shape)

print()

print(df.info())