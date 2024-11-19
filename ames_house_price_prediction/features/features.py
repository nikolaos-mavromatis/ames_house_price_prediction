from pathlib import Path

from sklearn.impute import SimpleImputer
import typer
from loguru import logger
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    RobustScaler,
    PolynomialFeatures,
)
from pickle import dump

from ames_house_price_prediction.config import (
    CAT_FEATURES,
    MODELS_DIR,
    NUM_FEATURES,
    ORD_FEATURES,
    PROCESSED_DATA_DIR,
    TARGET,
)
from ames_house_price_prediction.features.utils import make_features


app = typer.Typer()


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / "dataset.parquet",
    preprocessor_path: Path = MODELS_DIR / "preprocessor.pkl",
    features_path: Path = PROCESSED_DATA_DIR / "features.parquet",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.parquet",
):
    logger.info("Generating features from dataset...")
    input_df = pd.read_parquet(input_path)

    df = input_df.pipe(make_features)

    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", RobustScaler())]
    )
    ordinal_transformer = Pipeline(
        steps=[
            (
                "ord_encoding",
                OrdinalEncoder(
                    dtype=int,
                    categories=len(ORD_FEATURES) * [["Po", "Fa", "TA", "Gd", "Ex"]],
                    handle_unknown="use_encoded_value",
                    unknown_value=-1,
                ),
            )
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("oh_encoding", OneHotEncoder(drop="first", sparse_output=False)),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUM_FEATURES),
            ("ord", ordinal_transformer, ORD_FEATURES),
            ("cat", categorical_transformer, CAT_FEATURES),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )
    pipe = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("poly", PolynomialFeatures(2, include_bias=True)),
        ]
    )
    transformed_df = pd.DataFrame(pipe.fit_transform(df), columns=pipe.get_feature_names_out())

    with open(preprocessor_path, "wb") as f:
        dump(pipe, f, protocol=5)

    transformed_df.to_parquet(features_path, index=False)
    df[[TARGET]].to_parquet(labels_path, index=False)

    logger.success("Features generation complete.")


if __name__ == "__main__":
    app()
