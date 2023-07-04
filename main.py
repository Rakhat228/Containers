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
options = {'Mocha':'mocha', 'Kal':'Kal', 'Soskob':'soskob'}
if log_title == login and log_pass == password:
    st.multiselect('Выбрать контейнер', options)
    number = st.number_input('number', min_value=0, step=1)
    st.write(number)
    for i in range(1, number+1):
        lst.append(prev_num + i)
    st.write(lst)
    df = pd.DataFrame()
    df['Уникальный штрих кодконтейнера'] = lst

    def to_excel(df):
       output = BytesIO()
       writer = pd.ExcelWriter(output, engine='openpyxl')
       df.to_excel(writer, index=False, sheet_name='Sheet1') 
       writer.close()
       processed_data = output.getvalue()
       return processed_data
    df_xlsx = to_excel(df)
    st.download_button(label='📥 Скачать готовый файл',
                                   data = df_xlsx ,
                                   file_name= 'Output.xlsx')
        


