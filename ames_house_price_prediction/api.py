import datetime
import pickle
from pathlib import Path

from fastapi import FastAPI
import pandas as pd

from ames_house_price_prediction.config import MODELS_DIR
from ames_house_price_prediction.features.utils import (
    calculate_lot_age,
    calculate_years_since_remodel,
)


app = FastAPI(
    title="House Price Quoting Service",
    description="A simple API to get a quote based on house characteristics.",
    version="0.1.0",
)


def load_pickle_file(path: Path):
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj


@app.get("/")
def root():
    return "All good here!"


@app.get("/quote/")
async def quote(
    LotArea: float,
    YearBuilt: int,
    YearRemodAdd: int,
    OverallQual: int,
    OverallCond: int,
):
    answers = {
        "LotArea": LotArea,
        "YearBuilt": YearBuilt,
        "YearRemodAdd": YearRemodAdd,
        "YrSold": datetime.datetime.now().year,
        "OverallQual": OverallQual,
        "OverallCond": OverallCond,
    }
    inference_data = (
        pd.DataFrame(answers, index=[0])
        .pipe(calculate_lot_age)
        .pipe(calculate_years_since_remodel)
    )
    preprocessor = load_pickle_file(MODELS_DIR / "preprocessor.pkl")
    preprocessed_inference_data = preprocessor.transform(inference_data)
    model = load_pickle_file(MODELS_DIR / "model.pkl")
    quote = model.predict(preprocessed_inference_data)

    return quote[0][0]
