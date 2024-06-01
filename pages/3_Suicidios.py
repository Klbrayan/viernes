import streamlit as st
import pandas as pd


st.title("Suicidios en Antioquia")
df = pd.read_csv('static/datasets/sivigila_intsuicidio.csv')

c
st.table(df)