import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Carregando Modelo Teste
model = joblib.load('random_forest_model.pkl')

# Colunas a serem dropadas
drop_columns = ['ULTICONS', 'ULTIDIAG', 'ULTITRAT', 'obito_geral', 'vivo_ano1', 'vivo_ano3', 'ULTINFO', 'obito_cancer', 'ESCOLARI']

st.title('❤ Machine Learning Teste')

st.write('Hello world!')
df = pd.read_csv('https://raw.githubusercontent.com/acanellafilho/ia/refs/heads/main/Trabalho%20IA%20Parte%202/data_preProcess2.csv')
st.write(df)

with st.sidebar:
    st.header('Input features')
    
    # Inputs para todas as colunas relevantes
    escolari = st.selectbox('Escolaridade', ('1', '2', '3', '4', '5'))
    idade = st.slider('Idade(anos)', 0, 99, 46, step=1)
    ibge = st.text_input('IBGE')
    cateatend = st.text_input('Categoria de Atendimento')
    diagprev = st.text_input('Diagnóstico Prevalente')
    basediag = st.text_input('Base do Diagnóstico')
    ec = st.text_input('Estádio Clínico')
    g = st.text_input('G')
    psa = st.text_input('PSA')
    gleason = st.text_input('Gleason')
    trathosp = st.text_input('Tratamento Hospitalar')
    nenhum = st.checkbox('Nenhum Tratamento')
    cirurgia = st.checkbox('Cirurgia')
    radio = st.checkbox('Radioterapia')
    quimio = st.checkbox('Quimioterapia')
    hormonio = st.checkbox('Hormonioterapia')
    tmo = st.checkbox('Transplante de Medula Óssea')
    imuno = st.checkbox('Imunoterapia')
    outros = st.text_input('Outros Tratamentos')
    nenhumant = st.checkbox('Nenhum Tratamento Anterior')
    consdiag = st.text_input('Consulta Diagnóstico')
    tratcons = st.text_input('Tratamento de Consulta')
    diagtrat = st.text_input('Diagnóstico e Tratamento')
    anodig = st.number_input('Ano do Diagnóstico', min_value=1900, max_value=2025, value=2021)
    drs = st.text_input('DRS')
    rras = st.text_input('RRAS')
    recnenhum = st.checkbox('Nenhuma Recorrência')
    ibgeaten = st.text_input('IBGE Atendimento')

    # Criar um DataFrame com base nos dados de entrada
    data = {'ESCOLARI': [escolari],
            'IDADE': [idade],
            'IBGE': [ibge],
            'CATEATEND': [cateatend],
            'DIAGPREV': [diagprev],
            'BASEDIAG': [basediag],
            'EC': [ec],
            'G': [g],
            'PSA': [psa],
            'GLEASON': [gleason],
            'TRATHOSP': [trathosp],
            'NENHUM': [nenhum],
            'CIRURGIA': [cirurgia],
            'RADIO': [radio],
            'QUIMIO': [quimio],
            'HORMONIO': [hormonio],
            'TMO': [tmo],
            'IMUNO': [imuno],
            'OUTROS': [outros],
            'NENHUMANT': [nenhumant],
            'CONSDIAG': [consdiag],
            'TRATCONS': [tratcons],
            'DIAGTRAT': [diagtrat],
            'ANODIAG': [anodig],
            'DRS': [drs],
            'RRAS': [rras],
            'RECNENHUM': [recnenhum],
            'IBGEATEN': [ibgeaten]
           }

    input_df = pd.DataFrame(data)
    
    # Fazer a predição
    if st.button('Predict'):
        prediction = model.predict(input_df)
        st.write(f"Estimated `vivo_ano5`: {prediction[0]}")
