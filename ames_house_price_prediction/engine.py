import typer
from loguru import logger

from ames_house_price_prediction.data import prepare_data
from ames_house_price_prediction.features import generate_features
from ames_house_price_prediction.modeling import train_model, make_predictions

app = typer.Typer()


@app.command()
def engine():
    logger.info("Running pipeline...")
    prepare_data()
    generate_features()
    train_model()
    make_predictions()
    logger.success("Pipeline ran successfully.")


if __name__ == "__main__":
    app()
