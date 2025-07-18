import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load saved model
model = joblib.load('calorie_predictor.pkl')

# streamlit interface title
st.title('Calorie Burn Predictor')

# accept user input

# 'Gender', 'Age', 'Height', 'Weight', 'Duration',
#        'Heart_Rate', 'Body_Temp', 'Calories', 'BMI', 'BMI Category',
#        'Age Groups',

gender = st.selectbox( "Gender", ['male', 'female'])
age = st.slider("Age", 10, 100, 20)
height = st.number_input("Height (cm)", 100, 250, 160)
weight = st.number_input("Weight (kg)", 20, 200, 60)
duration = st.slider("Duration (mins)", 1, 180, 30)
heart_rate = st.slider("Heart Rate (bpm)", 40, 200, 80)
body_temp = st.slider("Body Temperature (°C)", 35.0, 42.0, 37.0)
bmi = weight / ((height / 100) ** 2)
bmi_category = 'Normal' if 18.5 <= bmi < 24.9 else 'Overweight' if bmi >= 25 else 'Underweight'
age_groups = 'Child' if age < 12 else 'Adolescence' if age < 19 else 'Adult' if age < 60 else 'Senior Adult'


# predict button
if st.button("Predict Calories Burned"):
    data = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp,
        "BMI": bmi,
        "BMI Category": bmi_category,
        "Age Groups": age_groups
    }
    # convert to dataframe
    df = pd.DataFrame(data)

    # predict model
    calorie = model.predict(df)
    prediction = np.sqrt(calorie)


    st.success(f'Estimated Calories Burned: {prediction[0]:.2f} kcal')
