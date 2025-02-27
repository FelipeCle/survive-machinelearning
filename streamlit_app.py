import streamlit as st
import pandas as pd
import joblib

# Carregando Modelo Teste
model = joblib.load('random_forest_model.pkl')

st.title('❤ Machine Learning teste')

st.write('Hello world!')
df = pd.read_csv('https://raw.githubusercontent.com/acanellafilho/ia/refs/heads/main/Trabalho%20IA%20Parte%202/data_preProcess2.csv')
st.write(df)

with st.sidebar:
  st.header('Input features')
  # Input features: ESCOLARI, IDADE
  escolari = st.selectbox('Escolaridade', ('1', '2', '3', '4', '5'))
  idade = st.slider('Idade(anos)', 0, 99, 46, step=1)
  
  # Create a dataframe based on user input
  data = {'ESCOLARI': [escolari],
          'IDADE': [idade]}
  input_df = pd.DataFrame(data)
  st.write("Input DataFrame", input_df)

  # Make prediction
  if st.button('Predict'):
      prediction = model.predict(input_df)
      st.write(f"Estimated `vivo_ano5`: {prediction[0]}")
