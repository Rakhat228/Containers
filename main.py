import pandas as pd
import streamlit as st
import requests
from io import BytesIO
st.set_page_config(page_title = 'Контейнеры')
st.header('Контейнеры')
st.subheader('Контейнеры')
lst = []
prev_num = 1001581234

sheet_url = "https://docs.google.com/spreadsheets/d/1I7cU0ZPlL5YatiAI5qMN7ZAe1qEmeRvwWz85go-bVTs/edit#gid=0"
csv_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
xd = pd.read_csv(csv_url)


log_title = st.text_input('Login')
log_pass = st.text_input('password') 
options = {'Mocha':'mocha', 'Kal':'Kal', 'Soskob':'soskob'}


for i in range(len(xd['Login'])):
    if log_title == xd['Login'][i] and log_pass == xd['Password'][i]:
        token = xd['Token'][i]
        st.write(token)
        st.selectbox('Выбрать контейнер', options)
        number = st.number_input('number', min_value=0, step=1)
        st.write(number)
        for i in range(1, number+1):
            lst.append(prev_num + i)
        df = pd.DataFrame()
        df['Уникальный штрих-код контейнера'] = lst
        st.write(df)
    
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
    else:
        st.write('Неправильный логин или пароль')
        
        


