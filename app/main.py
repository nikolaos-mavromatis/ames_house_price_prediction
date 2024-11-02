import locale
import requests

import streamlit as st


locale.setlocale(locale.LC_ALL, "")


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
            remodeled_year_val = st.number_input(
                "Remodeled Year",
                value=None,
                step=1,
                help="Leave empty if the house has not been remodeled.",
            )

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

        # Every form must have a submit button.
        _, col, _ = st.columns(3)
        with col:
            submitted = st.form_submit_button("Quote me now!", use_container_width=True)
        if submitted:
            # collect all form inputs to pass into the api call
            params = {
                "LotArea": area_val,
                "YearBuilt": build_year_val,
                "YearRemodAdd": remodeled_year_val if remodeled_year_val else -1,
                "OverallQual": qual_val,
                "OverallCond": cond_val,
            }
            quote = requests.get(
                # FIXME: replace local host+port with cloud details
                url="http://localhost:8000/quote/",
                params=params,
            ).json()
            quote_in_dollars = locale.currency(quote, grouping=True)

            st.divider()
            st.subheader(
                f"The value of your house is estimated at :blue[**{quote_in_dollars}**]. "
            )

with help:
    st.write("WIP - Show how this app is connected to other elements of the project.")
