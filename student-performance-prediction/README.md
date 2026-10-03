# 🎓 Student Performance Prediction using Machine Learning

A machine learning project that predicts a student's final score using academic and lifestyle-related features.

## 📌 Project Overview

This project demonstrates an end-to-end beginner-level machine learning workflow:

- Data inspection
- Exploratory Data Analysis (EDA)
- Correlation analysis
- Feature selection
- Train-test splitting
- Model training
- Model evaluation
- Cross-validation
- Feature importance analysis
- Model saving
- Streamlit deployment

## 📊 Dataset

The dataset contains 20 student records and the following features:

| Feature | Description |
|---|
| `Study_Hours` | Student's study hours |
| `Attendance` | Attendance percentage |
| `Previous_Marks` | Previous academic marks |
| `Assignments` | Assignment performance |
| `Sleep_Hours` | Sleep hours |
| `Final_Score` | Target variable |

## 🤖 Machine Learning Models

### Linear Regression

The model was trained to predict `Final_Score`.

Test-set results:

- MAE: 1.274
- RMSE: 1.541
- R²: 0.9918

### Random Forest Regressor

A Random Forest model was also trained for comparison.

Test-set results:

- MAE: 2.525
- RMSE: 2.685
- R²: 0.9752

## 🔄 Cross-Validation

5-fold cross-validation was performed.

**Linear Regression**

Mean CV R²: `0.9812`

**Random Forest**

Mean CV R²: `0.9425`

The results are specific to this dataset and should not be interpreted as real-world predictive performance.

## 🔍 Feature Importance

Random Forest feature importance was analyzed for:

- Previous Marks
- Attendance
- Assignments
- Study Hours
- Sleep Hours

## 🌐 Streamlit Application

The trained Linear Regression model was saved using Joblib and integrated into a Streamlit application.

The application accepts student information and returns a predicted final score.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Google Colab

## 📁 Project Structure

```text
student-performance-prediction/
│
├── README.md
├── Student_Performance_Prediction.ipynb
├── app.py
├── requirements.txt
├── student_performance.csv
└── student_score_model.pkl
```
