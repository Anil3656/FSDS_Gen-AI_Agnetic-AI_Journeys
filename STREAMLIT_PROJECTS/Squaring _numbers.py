import streamlit as st
#Add title to your app
st.title("My first st app")

st.write("Welcome!, This app calculates the square of a number.")

st.header("Select a number")
number = st.slider("pick a num", 0, 100, 25) #min max default
st.subheader("result")
squared_num = number * number
st.write(f"The square of **{number}** is **{squared_num}**.")


#To run this file , you need to install streamlit. You can do this by running the following command in your terminal
#pip install streamlit

#Then you can run this file by running the following command in your terminal
#python -m streamlit run app.py