from app.ml.model_loader import get_model, get_preprocessor

model = get_model()
preprocessor = get_preprocessor()

print(type(model))
print(type(preprocessor))