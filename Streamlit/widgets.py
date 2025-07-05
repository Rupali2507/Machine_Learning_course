import streamlit as st
import pandas as pd

st.title('Streamlit text input')

name = st.text_input('Enter your name')


age = st.slider('Select your age', 0, 100, 25)



options =["Pyhton", "Java", "C++", "JavaScript"]
choice = st.selectbox('Select your favorite programming language', options)

if name:
    st.write(f'Hello {name}!')
if age:
    st.write(f'You are {age} years old.')
if choice:
    st.write(f'You selected {choice} as your favorite programming language.')

if st.button('Submit'):
    st.write('Thank you for submitting your information!')



data ={
    "Name": name,
    "Age": age,
    "Favorite Language": choice
}
# Create a DataFrame
df = pd.DataFrame(data, index=[0])  
df.to_csv('user_data.csv', index=False)
st.write("Here is the data you entered:")
st.dataframe(df)


upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file is not None:
    df_uploaded = pd.read_csv(upload_file)
    st.write("Here is the uploaded CSV file:")
    st.dataframe(df_uploaded)