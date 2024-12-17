import streamlit as st
import numpy as np
import pandas as pd

# title of the application
st.title("Hello Streamlit")

# display a simple text
st.write("This is a simple Streamlit application.")

# create a pd dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df.to_csv("sampledata.csv")

# display the dataframe
st.write("Here is the dataframe")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)