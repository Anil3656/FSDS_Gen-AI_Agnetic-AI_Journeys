import streamlit as st

st.title("🔢 Counter App")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("➕ Increase"):
    st.session_state.count += 1

if st.button("➖ Decrease"):
    st.session_state.count -= 1

st.write(f"Current Count: {st.session_state.count}")
