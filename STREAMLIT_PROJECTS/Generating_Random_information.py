import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("This is a sample app to demonustarte the basic functionalities of Streamlit")

st.sidebar.header("User Input Features")

user_name = st.sidebar.text_input("What is your name?","Aneelkumar")
age = st.sidebar.slider(("select your age"),0,100,50)

favorite_color = st.sidebar.selectbox("What is your favorite color?",["Red","Green","Blue","Yellow","orange","purple"])

#------Main Page content------------
st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")


st.subheader("Here's some random data:")

#Create a sample dataframe
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)


#-----Check box to show/hide content or dataframe------
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

#----Button to trigger an action------ 
if st.button("Say hello!"):
    st.write("Hello, there!")
else:
    st.write("Goodbye!")