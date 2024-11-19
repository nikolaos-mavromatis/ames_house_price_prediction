Methodology
===========

## Part I: end-to-end ML pipeline

We can start the analysis using **a minimum set of relevant features** and include/build more later on.

The **advantages** of this approach are:

1. get a baseline model early on and iterate on that,
2. perform a robust initial data analysis as well as for each additional feature,
3. better estimate the importance of adding a feature and its implications,
4. avoid getting overwhelmed by all the possibilities around analysis, feature engineering, etc.

And, the **disadvantages**:

1. might not be possible in case of a large feature space; feature selection methods is the go-to option.

However, the purpose of the trained model is to serve the quoting app and not to provide the best predictions possible.

### Features

The **minimum set of relevant features** includes:

1. `LotArea`
2. `OverallQual`
3. `OverallCond`
4. `LotAge`=`YearSold`-`YearBuilt`
5. `YearsSinceRemod` = `YearRemodAdd` - `YearBuilt`  
   *`-1` indicates a house that has not been remodeled.*

### Model

I used a scikit-learn's `RidgeRegression()` model with the default parameters to train the model. 

### Performance

A **5-fold cross-validation** was used to evaluate the model. The scoring metric used was the default **explained variance** metric and the results that the current model achieved is a dazzling **0.68**.

### Outputs

There are two pickled objects generated from running the pipeline:

1. `preprocessor.pkl`: used to preprocess the data (one-hot encoding, scaling, etc.), and
2. `model.pkl`: used in conjunction with test/inference data to generate predictions.

## Part II: Streamlit UI and serving with FastAPI

::: api.main.quote

## Part III: deployment with Docker containers
In this project two containers need to be created:

* one for the API, and
* one for the UI.

Since the UI makes a call to the API to receive the prediction based on the user's inputs, the two containers need to communicate with each other.

This is not straightforward, because as per Docker's [documentation page](https://docs.docker.com/engine/network/), containers are by default agnostic to the type of network they are attached to. 

I used `docker-compose` to build both containers and the network over which they will communicate from a single file. 

``` bash
docker-compose up -d
```

!!! note
    The last part in `docker-compose.yml`, 

    ``` yaml
    networks:
      housing-app:
        driver: bridge
    ```

    takes care of creating the network where the two containers will be able to communicate with each other.
