import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter you name")

age = st.slider("Select you age", 0, 100, 25)
st.write(f"your age is {age}")

if name:
    st.write("Hello, " + name + "!")

options = ["Python", "Java", "C++", "JS"]
choice = st.selectbox("Choose your favorite language", options)
st.write(f"you selected " + choice)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)