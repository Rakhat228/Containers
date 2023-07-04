import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup as bs
import requests
from io import BytesIO
lst = []
prev_num = 1001581234
login = 'Kalykova'
password = '12345678'
log_title = st.text_input('Login')
log_pass = st.text_input('password') 

if log_title == login and log_pass == password:
    number = st.number_input('number', min_value=0, step=1)
    st.write(number)
    for i in range(1, number+1):
        lst.append(prev_num + i)
    df = pd.DataFrame()
    df['Code'] = lst
    st.write(df)
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='openpyxl')
        df.to_excel(writer, index=False, sheet_name='Sheet1') 
        writer.save()
        processed_data = output.getvalue()
        return processed_data
    df_xlsx = to_excel(df)
    st.download_button(label='📥 Скачать готовый файл',
                                    data = df_xlsx ,
                                    file_name=  'containers.xlsx')
    to_excel(df)


