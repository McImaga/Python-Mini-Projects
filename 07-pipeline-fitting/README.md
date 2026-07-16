# KNN Classification with Hyperparameter Tuning

A complete supervised learning project demonstrating how to build, evaluate, and optimize a K-Nearest Neighbors classifier using scikit-learn.

## 📌 Project Overview
This project trains a KNN model to perform binary classification. The key focus is showing why hyperparameter tuning matters: 
We improved model accuracy from **96.6% with default k=3** to **100% with optimal k=1** using 5-Fold Cross-Validation.

## 🎯 Key Objectives
1.  Data preprocessing and train-test split
2.  Build a baseline KNN model with Pipeline + StandardScaler
3.  Evaluate using Confusion Matrix, Accuracy, Precision, Recall, F1
4.  Hyperparameter tuning with GridSearchCV to find optimal `k`
5.  Compare performance of default vs optimized model

## 🛠️ Tech Stack
- **Language**: Python 3.11
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Models**: KNeighborsClassifier, Pipeline
- **Evaluation**: train_test_split, GridSearchCV, classification_report, confusion_matrix

## 📊 Results

| Model | K Value | Accuracy |
| --- | --- | --- |
| **Baseline KNN** | 3 | 96.62% |
| **Optimized KNN** | 1 | 100.00% |

### Key Findings
1.  **Cross-Validation Matters**: Using GridSearchCV we found k=1 was optimal for this dataset
2.  **Preprocessing Impact**: Using `StandardScaler` in a Pipeline improved stability
3.  **No Overfitting**: The optimized model achieved perfect scores on the test set

### Visualizations
- Confusion Matrix for Baseline and Optimized model
- Accuracy vs K-Value plot to select optimal k

