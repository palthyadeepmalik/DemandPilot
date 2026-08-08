from datetime import date

from app.ml.predict import predict_demand

prediction = predict_demand(
    prediction_date=date(2015, 12, 31),
    pizza_id="bbq_ckn_l",
    category="Chicken",
    size="L",
)

print(prediction)