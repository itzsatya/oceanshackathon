import streamlit as st
import pandas as pd

df = pd.read_csv(
  "./df.csv"
)

df = df.reindex(index=df.index[::-1])

st.title("Time vs Intensity data table")

st.write("Here is the dataset:") 

st.write(df)