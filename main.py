import pandas as pd
import numpy as np
import streamlit as st
df = []
prev_num = 1001581234
login = 'Kalykova'
password = '12345678'
log_title = st.text_input('Login')
log_pass = st.text_input('password') 

if log_title == login and log_pass == password:
    number = st.number_input('number', min_value=0, step=1)
    st.write(number)
    for i in range(1, number):
        df.append(prev_num + i)
    st.write(df)



