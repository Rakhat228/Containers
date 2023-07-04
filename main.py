import pandas as pd
import numpy as np
import streamlit as st

login = 'a'
password = '12345678'

@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
st.write(df)

log_title = st.text_input('Login')
log_pass = st.text_input('password')   

number = st.number_input('number', min_value=0, step=1)

if log_title == login and log_pass == password:
    st.write(number)
