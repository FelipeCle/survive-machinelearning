import streamlit as st
import pandas as pd

st.title('❤ Machine Learning teste')

st.write('Hello world!')
df =pd.read_csv('https://raw.githubusercontent.com/acanellafilho/ia/refs/heads/main/Trabalho%20IA%20Parte%202/data_preProcess2.csv')
df

with st.sidebar:
  st.header('Input features')
  # ESCOLARI,IDADE
  escolari = st.selectbox('Escolaridade',('1','2','3','4','5'))
  idade = st.slider('Idade(anos)', 0, 99, 46, step=1)
  #Criar df com base no input
  data = {'escolari': ESCOLARI,
          'idade': IDADE
          }
  input_df = pd.DataFrame(data, index=[0])
  input_df
