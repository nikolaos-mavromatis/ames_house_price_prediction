import pandas as pd
import numpy as np


def calculate_lot_age(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the difference between the year a house was built and the year it was sold."""
    return df.assign(LotAge=lambda x: x["YrSold"] - x["YearBuilt"])


def calculate_years_since_remodel(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the difference between the year a house was sold and the year it was remodelled.

    -1 when the property has never been remodelled.
    """
    return df.assign(
        YearsSinceRemod=lambda x: np.where(
            x["YearRemodAdd"] > x["YearBuilt"], x["YrSold"] - x["YearRemodAdd"], -1
        ),
    )

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """Method to enhance a dataframe with additional features.

    Parameters
    ----------
    df : pd.DataFrame
        the train, test or inference dataset

    Returns
    -------
    pd.DataFrame
        the enhanced dataframe
    """
    return df.pipe(calculate_lot_age).pipe(calculate_years_since_remodel)
