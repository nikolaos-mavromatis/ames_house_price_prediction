import datetime
import locale
from pathlib import Path
import pickle

import pandas as pd
import streamlit as st

from ames_house_price_prediction.config import MODELS_DIR
from ames_house_price_prediction.features.utils import (
    calculate_lot_age,
    calculate_years_since_remodel,
)

locale.setlocale(locale.LC_ALL, "")


@st.cache_resource
def load_model(path: Path):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


@st.cache_resource
def load_preprocessor(path: Path):
    with open(path, "rb") as f:
        preprocessor = pickle.load(f)
    return preprocessor


main, help = st.tabs(["Main", "Help"])

with main:
    st.title("House Price Prediction App")
    st.write(
        "The form below will be used to generate your quote. Fill in as accurately as you can."
    )

    with st.form("house_characteristics", enter_to_submit=False):
        st.header("House Characteristics")

        col1, col2 = st.columns(2, gap="small")

        with col1:
            build_year_val = st.number_input(
                "Build Year",
                value=None,
                step=1,
            )
            qual_val = st.slider(
                "Overall Quality",
                min_value=1,
                max_value=10,
                value=5,
                step=1,
                help="Select the quality of the materials.",
            )
            remodeled_val = st.checkbox("My house has been remodeled.", value=False)

        with col2:
            area_val = st.number_input(
                "Living Area (in Sq.Ft.)",
                value=None,
            )
            cond_val = st.slider(
                "Overall Condition",
                min_value=1,
                max_value=10,
                value=5,
                step=1,
                help="Select the condition of the house.",
            )
            remodeled_year_val = st.number_input(
                "Remodeled Year",
                value=None,
                step=1,
                help="Leave empty if the house has not been remodeled.",
            )

        # Every form must have a submit button.
        _, col, _ = st.columns(3)
        with col:
            submitted = st.form_submit_button("Quote me now!", use_container_width=True)
        if submitted:
            # STEPS:
            # 1. make inference dataframe
            # 2. load preprocessor & preprocess data
            # 3. load model & predict

            # 1. make inference dataframe
            answers = {
                "LotArea": area_val,
                "YearBuilt": build_year_val,
                "YearRemodAdd": remodeled_year_val,
                "YrSold": datetime.datetime.now().year,
                "OverallQual": qual_val,
                "OverallCond": cond_val,
            }
            inference_data = (
                pd.DataFrame(answers, index=[0])
                .pipe(calculate_lot_age)
                .pipe(calculate_years_since_remodel)
            )

            # 2. load preprocessor & preprocess data
            preprocessor = load_preprocessor(MODELS_DIR / "preprocessor.pkl")
            preprocessed_inference_data = preprocessor.transform(inference_data)

            # 3. load model & predict
            model = load_model(MODELS_DIR / "model.pkl")
            quote = model.predict(preprocessed_inference_data)
            quote_in_dollars = locale.currency(quote[0][0], grouping=True)
            print(quote)

            st.divider()

            st.subheader(
                f"The value of your house is estimated at :blue[**{quote_in_dollars}**]. "
            )

with help:
    st.write("WIP - Show how this app is connected to other elements of the project.")
