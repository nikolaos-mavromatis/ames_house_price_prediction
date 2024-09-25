from pathlib import Path

import typer
from loguru import logger
import pandas as pd

from ames_house_price_prediction.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from ames_house_price_prediction.data.utils import clean_dataset

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "train.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.parquet",
):
    logger.info("Processing dataset...")
    # load
    raw_df = pd.read_csv(input_path, index_col="Id")
    # clean
    df = clean_dataset(raw_df)
    # validate
    ...
    # write dataset
    df.to_parquet(output_path, index=False)
    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
