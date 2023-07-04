import pandas as pd
import numpy as np
import streamlit as st

login = 'a'
password = '12345678'

log_title = st.text_input('Login')
log_pass = st.text_input('password')   

number = st.number_input('number', min_value=0, step=1)

if log_title == login and log_pass == password:
    st.write(number)
