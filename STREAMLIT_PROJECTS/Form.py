import streamlit as st

st.title("📝 Contact Form")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thanks {name}, we received your message!")
