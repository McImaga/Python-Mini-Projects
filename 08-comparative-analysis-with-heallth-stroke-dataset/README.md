# Evaluation of Probabilistic and Non-Probabilistic ML models Clinical Stroke Prediction

This project compares different machine learning models to predict the likelihood of stroke based on patient clinical data. The goal is to evaluate which of the model - probabilistic vs non-probabilistic  - performs best for early detection.

## Dateset  
- **Source**: Healthcare Stroke Dataset  
-  **Rows**: 5110 patients  
- **Features**: 12 clinical features including `gender`, `age`, `hypertension`, `avg_glucose_level`, `bmi`, `work_type`, etc.  
- **Target**: `stroke` - Binary Classification: 1 = stroke, 0 = No stroke.  

## Data Preprocessing  
1. Handled mising values in `bmi` using the mean imputation  
2. Dropped `id` because it is not very relevant to our model training.
3. Encoded categorical variables using LabelEncoder 
4. Scaled numerical variables using the StandardScaler
5. Train-Test-Split: using the 80/20  with stratification.

## Models Implemented  
#### Probabilistic Models  
- **Logistic Regression** with GridSearchCV for hyperparameter tuning  
- **Gaussian Naive Bayes**   

#### Non - Probabilistic  Models

- **K - Nearest Neighbors** with GridSearchCV  
- **Support Vector Machine** 

## Evaluation Metrics 
- Accuracy, Precision, Recall, F1-score  
- Confusion Matrix 
- ROC Curve Comparison

## Tech Stack  
`python`, `NumPy`, `Pandas`, `Scikit-learn`, `Matplotlib`

## How to Run  
1. Clone Repo  
2. `pip install pandas numpy scikit-learn matplotlib`
3. Run `stroke_prediction.ipynb` in Jupyter. 
