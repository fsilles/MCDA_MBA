import os
import pandas as pd
import numpy as np
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from pandas import read_csv
from commom import commomHeader

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações de sessão

if 'config' not in st.session_state:
    st.session_state['config'] = {'init':'0'}

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações da página
st.set_page_config(layout="wide",page_title="TCC MBA USP ESALQ",page_icon="chart_with_upwards_trend")

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# funções

def createASelectionOption(labelName, options):
    st.subheader(labelName)
    option = st.selectbox('' ,options)
    return option

def selectOptionsDefinition():
    # §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
    # Campos de dados CNHI
    allOptionsList = []
    #### primeira Lista
    listOfLabelMessage=["Qualificação e experiência da equipe técnica de mentores no problema de IA apresentador:"
                         ,"Qualificação e experiência da equipe de mentores/especialistas de outras áreas do instituto disponíveis para ajudar ou startup possui experiência no domínio específico do problema"
                         ,"Capacidade da equipe de IA da startup em implementar as metodologias/algoritmos /ideias propostas durante o programa"
                         ]
    options01 = ["Selecione uma Qualificação:"
                        ,"1. A equipe possui pouca ou nenhuma experiência relevante em IA no problema abordado."
                        ,"2. A equipe possui alguma experiência em IA no assunto, mas limitada e não diretamente relacionada ao problema apresentado"
                        ,"3. MVP - A solução tem um Produto Mínimo Viável funcional."
                        ,"4. Produto final - A solução está totalmente desenvolvida e pronta para lançamento."
                        ,"5. Comercializado - A solução está sendo comercializada com necessidade de melhorias"
                        ]
    allOptionsList.append(options01)

    options02 = ["Selecione uma opção:"
                 ,"1. Nem a startup nem os mentores possuem experiência no domínio específico, e há pouca viabilidade de buscar apoio em outras áreas ou externamente."
                 ,"2. Nem a startup nem os mentores possuem experiência no domínio específico, mas há alguma viabilidade de buscar apoio em outras áreas ou externamente."
                 ,"3. Os mentores ou a startup possuem alguma experiência no domínio específico, e há viabilidade moderada de buscar apoio em outras áreas ou externamente."
                 ,"4. A startup possui significativa experiência no domínio específico, e não necessita buscar apoio em outras áreas ou externamente."
                 ,"5. A startup possui ampla experiência no domínio específico, e os mentores possuem experiência no domínio específico."

                ]
    allOptionsList.append(options02)
    options03 = ["Selecione uma opção:"
                 ,"1. A equipe possui baixa capacidade de implementação, com habilidades limitadas em IA."
                 ,"2. A equipe possui alguma capacidade de implementação, mas com lacunas significativas em habilidades e recursos humanos."
                 ,"3. A equipe possui capacidade moderada de implementação, com habilidades e recursos humanos suficientes para abordar os desafios comuns."
                 ,"4. A equipe possui alta capacidade de implementação, com habilidades avançadas em IA e recursos humanos."
                 ,"5. A equipe possui capacidade de implementação excepcional, com habilidades abrangentes e experiência comprovada em IA, aparenta não precisar da ajuda."
                ]
    allOptionsList.append(options03)

    for idx, selectMessage in enumerate(listOfLabelMessage):
        optionResult = createASelectionOption(selectMessage,allOptionsList[idx] )
        st.write("Opcao escolhida: ", optionResult)
        st.write("-----------------------")
    #selectorOptions[optionsQualification]
                                   
    #for idxLabel, labelName in enumerate(listOfLabelSelector):
    #    selectorList.append(createASelectionOption(labelName))

    #st.write("Qualificacao escolhida: ", opQualificacao[])


# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# Desenha o header de todas as páginas
commomHeader(st)



# codificacao #
selectOptionsDefinition()

