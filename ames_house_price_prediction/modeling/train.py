from pathlib import Path
from pickle import dump

from sklearn.preprocessing import QuantileTransformer
import typer
from loguru import logger
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.compose import TransformedTargetRegressor
from sklearn.model_selection import cross_val_score, ShuffleSplit

from ames_house_price_prediction.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.parquet",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.parquet",
    model_path: Path = MODELS_DIR / "model.pkl",
):
    logger.info("Training some model...")
    X = pd.read_parquet(features_path)
    y = pd.read_parquet(labels_path)

    # transform target and create model pipeline
    transformer = QuantileTransformer(output_distribution="normal")
    regressor = Ridge()
    ml_pipe = TransformedTargetRegressor(regressor=regressor, transformer=transformer)

    # perform a 5-fold cross-validation to assess model fit
    cv = ShuffleSplit(n_splits=5, test_size=0.3)
    scores = cross_val_score(ml_pipe, X, y, cv=cv)
    logger.info(
        "%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std())
    )

    # train using all available data
    model = ml_pipe.fit(X.values, y.values)

    with open(model_path, "wb") as f:
        dump(model, f, protocol=5)

    logger.success("Modeling training complete.")


if __name__ == "__main__":
    app()
