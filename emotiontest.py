import streamlit as st

st.title("🧠 Test App")

user_input = st.text_input("Enter something:")

if st.button("Click"):
    st.write("You said:", user_input)
