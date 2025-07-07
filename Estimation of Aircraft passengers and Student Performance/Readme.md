# 📊 Student Performance Prediction & Time Series Forecasting

This repository contains two core machine learning tasks:

1. **Predicting Student Performance using Multiple Linear Regression**
2. **Forecasting Air Passenger Data using Time Series Analysis (AR Model)**

---

## 🧠 Part A: Student Performance Prediction

### 📁 Dataset
A dataset of 10,000 students containing the following features:
- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced  
**Target Variable**: Performance Index

### 🛠️ Models Built
- **Model 1**: Multiple Linear Regression from scratch using NumPy and Pandas
- **Model 2**: Using scikit-learn’s `LinearRegression` class

### 🧹 Preprocessing
- Z-score standardization for numerical features
- Encoding of categorical variables (One-Hot/Label)

### 📈 Evaluation
- Metrics: Mean Squared Error (MSE) and R² Score
- Visual Comparison: Actual vs Predicted plots

---

## 📉 Part B: Time Series Forecasting – Air Passenger Dataset

### 📁 Dataset
Monthly air passenger data (1949–1960)

### 📊 Tasks Performed
- Visualized data, plotted ACF and PACF
- Determined optimal lag for AR model
- Train-Test Split:
  - Train: 1949–1959
  - Test: 1960

### 🧪 Evaluation
- Predicted values compared with real data from 1960
- Plotted actual vs predicted passenger counts

---

## 📂 Repository Structure

