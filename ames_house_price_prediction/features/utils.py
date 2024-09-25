import pandas as pd


def calculate_lot_age(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the difference between the year a house was built and the year it was sold."""
    return df.assign(LotAge=lambda x: x["YrSold"] - x["YearBuilt"])
