# 06 - Multiple Linear Regression + Regularization

**Predicting Student Final Scores**

### **Problem**
Can we predict a student's `Final_Score` based on study habits?

### **Dataset**
`Multicollinearity_Dataset.xlsx` - 100 students, 6 features
Features: Study_Hours, Reading_Hours, Practice_H, Total_Study_Time, Attendance
Target: Final_Score

### **Workflow**
1.  **EDA**: Checked correlation matrix. All features positively correlated with Final_Score
2.  **Baseline Model**: Multiple Linear Regression
3.  **Evaluation**: Split 80/20. Compared Train vs Test MSE, RMSE, R²
4.  **Regularization**: Used GridSearchCV to tune Lasso, Ridge, and ElasticNet to handle multicollinearity
5.  **Comparison**: Final table of all 3 models

### **Key Results**
| Model | MSE | RMSE | R² |
| --- | --- | --- | --- |
| Lasso | 12.5379 | 3.5403 | 0.9839 |
| Ridge | 12.9489 | 3.5985 | 0.9834 |
| ElasticNet | 12.4752 | 3.5320 | 0.9846 |

**Insight**: ElasticNet performed best. Regularization helped prevent overfitting on correlated features like Study_Hours and Total_Study_Time.

### **Tech Stack**
`Python` `Pandas` `Scikit-learn` `GridSearchCV` `LinearRegression` `Lasso` `Ridge` `ElasticNet`

### **What I Learned**
- How to detect and handle multicollinearity
- When to use Lasso vs Ridge vs ElasticNet
- Importance of hyperparameter tuning with GridSearchCV