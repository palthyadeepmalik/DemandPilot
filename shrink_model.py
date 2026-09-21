import joblib

m = joblib.load("backend/app/artifacts/demand_model.pkl")
print(type(m))
print("n_estimators:", getattr(m, "n_estimators", "n/a"))

joblib.dump(m, "backend/app/artifacts/demand_model_small.pkl", compress=3)