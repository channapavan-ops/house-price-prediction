import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ------------------------------------------------
# 1. Load dataset
# ------------------------------------------------

data = pd.read_csv("data.csv")


# ------------------------------------------------
# 2. Select input features
# ------------------------------------------------

X = data[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]
]


# ------------------------------------------------
# 3. Select target
# ------------------------------------------------

y = data["price"]


# ------------------------------------------------
# 4. Split dataset
# ------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------------
# 5. Create ML model
# ------------------------------------------------

model = LinearRegression()


# ------------------------------------------------
# 6. Train model
# ------------------------------------------------

model.fit(X_train, y_train)


# ------------------------------------------------
# 7. Make predictions
# ------------------------------------------------

predictions = model.predict(X_test)


# ------------------------------------------------
# 8. Evaluate model
# ------------------------------------------------

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)


print("--------------------------------")
print("MODEL TRAINING COMPLETED")
print("--------------------------------")

print("Mean Absolute Error:", mae)

print("R2 Score:", r2)


# ------------------------------------------------
# 9. Save trained model
# ------------------------------------------------

with open("house_price_model.pkl", "wb") as file:

    pickle.dump(model, file)


print("--------------------------------")
print("Model saved successfully!")
print("File: house_price_model.pkl")
print("--------------------------------")