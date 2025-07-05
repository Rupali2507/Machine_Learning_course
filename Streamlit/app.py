import streamlit as st
import pandas as pd
import numpy as np

#title of application
st.title("Happy Birthday")

# Display simple text
st.write("This is a simple application to wish you a happy birthday")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Birthday': ['1998-01-01', '1993-02-02', '1988-03-03']
})

st.write("Here is a sample DataFrame:")
st.write(df)

#create line chart

char_data = pd.DataFrame(
    np.random.randn(20,3),columns=['A', 'B', 'C']
)

st.line_chart(char_data)


