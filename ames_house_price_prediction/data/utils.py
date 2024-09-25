"""
This file contains useful functions to clean the datasets required.
In this project there is only one dataset but it would be good practice to keep all 
transformation function in a single place and use in separate files accordingly. 
"""

import pandas as pd

from ames_house_price_prediction.config import FEATURES, TARGET


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs all cleaning tasks.

    Parameters
    ----------
    df : pd.DataFrame
        The raw Ames housing dataset.

    Returns
    -------
    pd.DataFrame
        The clean dataframe ready for feature engineering and
        preprocessing.
    """
    output = df.loc[:, FEATURES + [TARGET]]
    return output
