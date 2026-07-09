# 05 - Model Training & Performance Evaluation

**Linear Regression on SPY Stock Data 2000-2022**

### **Project Overview**
This notebook demonstrates a complete ML workflow: loading financial data, training a Linear Regression model, and evaluating its performance on both training and test sets.

The goal: Predict `Adj Close` price using `High, Low, Open, Volume` features.

### **Dataset**
- **Source**: `SPY_2000_2022.csv` - S&P 500 ETF daily data
- **Rows**: 5536 trading days
- **Features**: High, Low, Open, Volume
- **Target**: Adj Close

### **Workflow**
1.  **Data Loading & EDA**: Loaded 22 years of SPY data with Pandas
2.  **Feature/Target Split**: X = [High, Low, Open, Volume], y = Adj Close
3.  **Train/Test Split**: 80/20 split with `train_test_split`
4.  **Modeling**: Fitted `LinearRegression` from Scikit-learn
5.  **Evaluation**: Calculated MSE, RMSE, and R² for both Train and Test sets
6.  **Comparison**: Built a summary table to check for overfitting

### **Key Results**
| Metric | Train | Test |
| --- | --- | --- |
| MSE | 0.1951 | 1.6843 |
| RMSE | 0.4417 | 1.2978 |
| R² | 0.9999 | 0.9996 |

**Insight**: The model has an R² of ~0.999 on both sets. Very low error, but the gap between Train and Test MSE suggests we should check for data leakage or time-series splitting next.

### **Tech Stack**
`Python` `Pandas` `NumPy` `Matplotlib` `Scikit-learn` `Jupyter Notebook`

### **How to Run**
```bash
pip install pandas numpy matplotlib scikit-learn jupyter
jupyter notebook class_model_training_task.ipynb