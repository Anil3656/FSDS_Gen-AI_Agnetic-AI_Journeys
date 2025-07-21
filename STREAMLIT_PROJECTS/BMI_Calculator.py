import streamlit as st

st.title("🧮 BMI Calculator")

height = st.number_input("Enter height (in meters):", format="%.2f")
weight = st.number_input("Enter weight (in kg):")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.warning("Height must be greater than zero.")
