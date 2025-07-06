# Logistic Regression for Heart Disease Prediction 

This project demonstrates the implementation of Logistic Regression using Python's `scikit-learn` library to predict whether a patient is diabetic or not based on various health metrics.

## 🚀 Project Overview

- **Goal**: To build a binary classification model using Logistic Regression.
- **Dataset**: The Pima Indians Diabetes Dataset (or similar), which includes features such as:
  - Number of pregnancies
  - Glucose concentration
  - Blood pressure
  - Skin thickness
  - Insulin levels
  - BMI
  - Diabetes pedigree function
  - Age

## 📊 Steps Involved

1. **Data Loading**:
   - Import the dataset into a Pandas DataFrame.
   - Preview the data and check for missing values.

2. **Data Preprocessing**:
   - Handle missing values by replacing zeros with the mean of respective columns.
   - Scale the features using `StandardScaler` for better model performance.

3. **Model Building**:
   - Apply Logistic Regression using `sklearn.linear_model.LogisticRegression`.
   - Split the data into training and testing sets.

4. **Model Evaluation**:
   - Calculate accuracy score on test data.
   - Generate confusion matrix and classification report.
   - Plot ROC curve and compute AUC score.

5. **Prediction**:
   - Use the trained model to predict the class (diabetic or not) for new patient data.

## 📈 Results

- Achieved a test accuracy of approximately **78%** (replace with actual value if different).
- ROC Curve visualized to assess classifier performance.

## 📦 Libraries Used

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## 🏁 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diabetes-logistic-regression.git
   cd diabetes-logistic-regression
