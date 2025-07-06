# Decision Tree Classifier from Scratch 🌳

This project implements a **Decision Tree Classifier** from scratch in Python using the **Gini impurity** metric.

It is designed for educational purposes to help understand how decision trees work under the hood — without relying on libraries like `scikit-learn`.

---

## 📂 Dataset

The model uses the **Car Evaluation dataset** from the UCI Machine Learning Repository.

- CSV file is expected at:  
  `/content/drive/MyDrive/DataScience_Fundamentals_Assignment-3/car_evaluation.csv`

---

## 📊 Features

- Builds a decision tree manually using Gini impurity
- Handles categorical features via label encoding
- Includes prediction function
- Visualizes the decision tree using `matplotlib`

---

## 🧠 Core Functions

| Function           | Description |
|--------------------|-------------|
| `calculate_gini()` | Computes Gini index of a dataset |
| `split_data()`     | Splits dataset by a feature and value |
| `gini_gain()`      | Computes information gain from split |
| `build_tree()`     | Recursively builds the decision tree |
| `predict()`        | Predicts label for new samples |
| `plot_tree()`      | Recursively visualizes the decision tree |

---

## 🚀 How to Run

1. Upload the notebook to [Google Colab](https://colab.research.google.com/)
2. Mount your Google Drive and ensure the CSV file path is correct
3. Run all cells to train the decision tree and visualize it

---

## 📦 Dependencies

- Python 3.somehing
- pandas
- matplotlib
- scikit-learn

Install using:

```bash
pip install pandas matplotlib scikit-learn
