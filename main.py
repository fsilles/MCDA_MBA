import os
import pandas as pd
import numpy as np
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from pandas import read_csv
from commom import commomHeader

# Import local functions
from criterionCreation import   selectOptionsDefinitionCapacity, selectOptionsDefinitionMaturity, selectOptionsDefinitionPotencial

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações de sessão

if 'config' not in st.session_state:
    st.session_state['config'] = {'init':'0'}

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações da página
st.set_page_config(layout="wide",page_title="TCC MBA USP ESALQ",page_icon="chart_with_upwards_trend")

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# funções


# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# Desenha o header de todas as páginas
commomHeader(st)



# codificacao #
listOfCompanies = ['A', 'B', 'C']
resultsFromCompany = {}
for idx, cmpy in enumerate(listOfCompanies):
    resultsFromCompany[cmpy] = []
    st.markdown("# Company " + cmpy)
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

