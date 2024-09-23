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
resultCapacity = selectOptionsDefinitionCapacity(st, showAnswer=False)
st.markdown("### --------------------------------------------------------------------------------------------")
resultMaturity = selectOptionsDefinitionMaturity(st, showAnswer=False)
st.markdown("### --------------------------------------------------------------------------------------------")
resultPotencial = selectOptionsDefinitionPotencial(st, showAnswer=False)

