
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_score_model.pkl")

st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final score using a machine learning model.")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0.0,
    max_value=10.0,
    value=8.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

if st.button("Predict Score"):

    student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks],
        "Assignments": [assignments],
        "Sleep_Hours": [sleep_hours]
    })

    prediction = model.predict(student)[0]

    st.success(f"Predicted Final Score: {prediction:.2f}")
