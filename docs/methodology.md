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
1. might not be possible in case of a large feature space; feature selection might be more suitable.

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

A **5-fold cross-validation** was used to evaluate the model. The scoring metric used was the default **explained variance** metric and the results that the current model achieved is a dashing **0.60**.
