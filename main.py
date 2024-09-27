import os
import pandas as pd
import numpy as np
import time
import datetime
import streamlit as st
#import matplotlib.pyplot as plt
from pandas import read_csv
from commom import commomHeader
from pyDecision.algorithm import electre_tri_b

# Import local functions
from criterionCreation import   selectOptionsDefinitionCapacity, selectOptionsDefinitionMaturity, selectOptionsDefinitionPotencial , defineStartupNames, showResults, retrieveIntegerAnswersCompany

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações de sessão
def initConfig():
    
    Q = [1,1,1,1,1,1,1,1,1]
    P = [2,2,2,2,2,2,2,2,2]
    V = [3,3,3,3,3,3,3,3,3]
    W = [1,1,1,1,1,1,1,1,1]

    b1=[2,2,2,2,2,2,2,2,2]
    b2=[4,4,4,4,4,4,4,4,4]
    B = [b1,b2]
    
    st.session_state['config'] = {'init':'0', 'totalStartups':0, 'Q':Q,'P':P,'V':V,'W':W,'B':B}

if 'config' not in st.session_state:
    initConfig()

config = st.session_state['config']

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações da página
st.set_page_config(layout="wide",page_title="TCC MBA USP ESALQ",page_icon="chart_with_upwards_trend")

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# funções
def resetAll():
    initConfig()

def checkIntegerAnswersCompany(resultsFromCompanies):
    status = True
    try:
        for key in resultsFromCompanies.keys():
            companyNow =  resultsFromCompany[key]
            _ = retrieveIntegerAnswersCompany(companyNow)
    except:
        status = False
    return status

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# Desenha o header de todas as páginas
commomHeader(st)


if config['init'] == '0':
    totalNumberOfStartups = st.number_input("Defina a quantidade de startups:", min_value=2, max_value=30, value=2)
    buttonNumberOfStartups = st.button('Confirmar', key='buttonNumberStartup')

else:
    buttonNumberOfStartups = False

    
if buttonNumberOfStartups:
    config['init'] = '1'
    config['totalStartups'] = totalNumberOfStartups
    st.session_state['config'] = config
    #if st.session_state.get('buttonNumberStartup'):
    #    disabled
    st.experimental_rerun()

if config['init'] == '1':
    #config['init'] = '2'
    companyNames = defineStartupNames(st, config['totalStartups'])
    confirmStartupNamesBt = st.button('Confirmar',key='confirmStartupNames')
    #print("companies :", companyNames)
    if confirmStartupNamesBt:
        config['init'] = '2'
        config['companyNames'] = companyNames
        st.session_state['config'] = config
        st.experimental_rerun()


if config['init'] == '2':
    listOfCompanies = config['companyNames']
    resultsFromCompany = {}
    for idx, cmpy in enumerate(listOfCompanies):
        resultsFromCompany[cmpy] = []
        st.markdown("# Startup " + cmpy)
        keyValue = cmpy.replace(' ', '') + '_C'
        resultCapacity = selectOptionsDefinitionCapacity(st, keyValue, showAnswer=False)
        resultsFromCompany[cmpy].append(resultCapacity)
        st.markdown("### --------------------------------------------------------------------------------------------")
        keyValue = cmpy.replace(' ', '') + '_M'
        resultMaturity = selectOptionsDefinitionMaturity(st, keyValue, showAnswer=False)
        resultsFromCompany[cmpy].append(resultMaturity)
        st.markdown("### --------------------------------------------------------------------------------------------")
        keyValue = cmpy.replace(' ', '') +  '_P'
        resultPotencial = selectOptionsDefinitionPotencial(st, keyValue,  showAnswer=False)
        resultsFromCompany[cmpy].append(resultPotencial)
        st.markdown("## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    confirmStartupValuesBt = st.button('Confirmar', key='confirmStartupValues')
    if confirmStartupValuesBt:
        ok = checkIntegerAnswersCompany(resultsFromCompany)
        if ok:
            config['init'] = '3'
            config['resultsFromCompany'] = resultsFromCompany
            st.session_state['config'] = config
            st.experimental_rerun()
        else:
            st.warning("Atenção!!! Responder todos critérios")
            # time.sleep(1.0)

if config['init'] == '3':
    showResults(st,config)

if config['init'] != '0':
    st.button("Cancelar",  on_click=resetAll)
#print("St.__version__: ", st.__version__)