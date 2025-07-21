import streamlit as st

st.title("Welcome to Streamlit!")
st.write("This is your first Streamlit app 🎈")
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name} 👋")
