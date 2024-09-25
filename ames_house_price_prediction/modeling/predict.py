from pathlib import Path
from pickle import load

import typer
from loguru import logger
from tqdm import tqdm
import pandas as pd

from ames_house_price_prediction.config import MODELS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR, TARGET
from ames_house_price_prediction.features.utils import calculate_lot_age

app = typer.Typer()


@app.command()
def main(
    features_path: Path = RAW_DATA_DIR / "test.csv",
    preprocessor_path: Path = MODELS_DIR / "preprocessor.pkl",
    model_path: Path = MODELS_DIR / "model.pkl",
    predictions_path: Path = PROCESSED_DATA_DIR / "submissions.csv",
):
    logger.info("Performing inference for model...")
    raw_input_df = pd.read_csv(features_path)
    print(raw_input_df.head())
    input_df = raw_input_df.pipe(calculate_lot_age)

    with open(preprocessor_path, "rb") as f:
        preprocessor = load(f)

    transformed_features = preprocessor.transform(input_df)

    with open(model_path, "rb") as f:
        model = load(f)

    predictions = model.predict(transformed_features)

    submissions = pd.concat(
        [raw_input_df[["Id"]], pd.DataFrame(predictions, columns=[TARGET])],
        axis=1,
        ignore_index=True,
    ).rename(columns={0: "Id", 1: "SalePrice"})

    submissions.to_csv(predictions_path, index=False)

    logger.success("Inference complete.")


if __name__ == "__main__":
    app()
