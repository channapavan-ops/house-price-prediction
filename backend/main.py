from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import pickle
import pandas as pd


# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices",
    version="1.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

with open("house_price_model.pkl", "rb") as file:

    model = pickle.load(file)


# ==========================================
# REQUEST DATA MODEL
# ==========================================

class HouseData(BaseModel):

    area: float

    bedrooms: int

    bathrooms: int

    stories: int

    parking: int


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "House Price Prediction API is running"
    }


# ==========================================
# PREDICTION ROUTE
# ==========================================

@app.post("/predict")
def predict_price(house: HouseData):

    # Create input dataframe

    input_data = pd.DataFrame(
        [[
            house.area,
            house.bedrooms,
            house.bathrooms,
            house.stories,
            house.parking
        ]],

        columns=[
            "area",
            "bedrooms",
            "bathrooms",
            "stories",
            "parking"
        ]
    )


    # Make prediction

    prediction = model.predict(input_data)


    # Get predicted price

    predicted_price = prediction[0]


    return {
        "predicted_price": round(
            float(predicted_price),
            2
        )
    }