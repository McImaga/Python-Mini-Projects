# Effect of Target Variable Transformations on House Price Prediction

This project explores how applying different mathematical transformations to the target variable affects the performance of a Linear Regression model on the Carlifornia Housing dataset.

Most ML tutorials focus on feature-scaling. This one focuses on the target.

## Problem Statement  
The `MedHouseVal` target in the Carlifornia Housing dataset is highly right-skewed.  
This violates the assumption of the Linear  Regression and leads poor predictions, especially for high-value house.  

## Methodoly   
1. **Load Data**: Carlifornia Housing dataset from `sklearn.datasets` 
2. **EDA**: Visualised the skewed distribution of `MedHouseVal`
3. **Target Transformation Applied**:
- `Original`
- `Log(1 + x)`
- `Square Root`
- `Box - Cox`
- `Yeo-Johnson` - Handle zero and negative values
- `Quantile` - forces a normal distribution
4. **Model**: `LinearRegression` trained on each transformed target.
5. **Evaluation**: MAE, MSE, RMSE on the test set. Predictions were inverse-transformed back to original scale for fair comparison.

## Results
| Target Variable | MAE | MSE | RMSE |  
| --- | --- | --- | --- |
|Original | 0.5331 | 0.5559 | 0.7456|
|Logarithmic | 0.4367 | 0.3172 | 0.5631| 
| square Root | 0.2010 | 0.5080 | 0.7127|
| Box-Cox | 0.4378 | 0.3190 | 0.5648 |
| Yeo-Johnson | 0.4369 | 0.3180 | 0.5639|
| Quantile | 0.5287 | 0.5851 | 0.7650|

**Conclusion**: Log and Yeo-Johnson transformations reduced RMSE by -24%. They made the target distribution more Gaussian, which Linear Regression prefers.

## Tech Stack
`Python` `Pandas` `Numpy` `Scikit-learn` `Matplotlib`

## How to Run
1. `git clone repo`
2. `pip install pandas numpy matplotlib sckit-learn`
3. Open `morning_exercise_IV.ipynb` in Jupyter

## Key Learning
Do not ignore your target variable. If it is skewed, transform it. It is one of the fastest wins in regression problems.