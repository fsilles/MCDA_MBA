import numpy as np 
import pandas as pd
from pyDecision.algorithm import electre_tri_b

def createASelectionOption(st, labelName, options, keyValue):
    st.markdown('##### ' + labelName)
    #st.subheader(labelName)
    option = st.selectbox('' ,options, key=keyValue)
    return option

def selectOptionsDefinitionCapacity(st, keyValue, showAnswer = False):
    # §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
    st.subheader("Critério: Capacidade Equipe")
    st.markdown('##### ------------------------------------------------------------------------------------------')

    allResults = []

    allOptionsList = []
    #### primeira Lista
    listOfLabelMessage=["Q1 - Qualificação e experiência da equipe técnica de mentores no (problema de IA) apresentado:"
                         ,"Q2 - Qualificação e experiência da equipe técnica de mentores no (domínio específico) do problema"
                         ,"Q3 - A startup possui experiência no domínio específico do problema (saúde, educação, indústria, meio ambiente, etc):"
                         ,"Q4 -Capacidade da equipe de IA da startup em implementar as metodologias/algoritmos /ideias propostas durante o programa"
                         ]
    options01 = ["Selecione uma opção:"
                        ,"1. A equipe possui pouca ou nenhuma experiência relevante em IA no problema abordado."
                        ,"2. A equipe possui alguma experiência em IA no assunto, mas limitada e não diretamente relacionada ao problema apresentado."
                        ,"3. A equipe possui experiência moderada em IA no assunto e alguma experiência relevante no problema apresentado."
                        ,"4. A equipe possui vasta experiência em IA no assunto e experiência significativa no problema apresentado."
                        ,"5. A equipe possui extensa experiência em IA no assunto, incluindo vários projetos bem-sucedidos no problema apresentado."
                        ]
    allOptionsList.append(options01)

    options02 = ["Selecione uma opção:"
                 ,"1. Os mentores não possuem experiência no domínio específico, e há pouca viabilidade de buscar apoio em outras áreas do instituto ou externamente."
                 ,"2. Os mentores não possuem experiência no domínio específico, mas há alguma viabilidade de buscar apoio em outras áreas do instituto ou externamente."
                 ,"3. Os mentores possuem alguma experiência no domínio específico, e há viabilidade moderada de buscar apoio em outras áreas do instituto ou externamente."
                 ,"4. Os mentores possuem significativa experiência no domínio específico, sem necessidade de buscar apoio em outras áreas do instituto ou externamente."
                 ,"5. Os mentores possuem ampla experiência no domínio específico e oferecem todo o suporte necessário."
                ]
    allOptionsList.append(options02)
    options03 = ["Selecione uma opção:"
                 ,"1. A startup não possui experiência no domínio específico e há pouca viabilidade de buscar apoio externamente."
                 ,"2. A startup não possui experiência no domínio específico, mas há alguma viabilidade de buscar apoio externamente."
                 ,"3. A startup possui alguma experiência no domínio específico, e há viabilidade moderada de buscar apoio externamente."
                 ,"4. A startup possui significativa experiência no domínio específico, e não necessita buscar apoio externamente."
                 ,"5. A startup possui ampla experiência no domínio específico e opera de forma independente."

                ]
    allOptionsList.append(options03)
    options04 = ["Selecione uma opção:"
                 ,"1. A equipe possui baixa capacidade de implementação, com habilidades limitadas em IA."
                 ,"2. A equipe possui alguma capacidade de implementação, mas com lacunas significativas em habilidades e recursos humanos."
                 ,"3. A equipe possui capacidade moderada de implementação, com habilidades e recursos humanos suficientes para abordar os desafios comuns."
                 ,"4. A equipe possui alta capacidade de implementação, com habilidades avançadas em IA e recursos humanos."
                 ,"5. A equipe possui capacidade de implementação excepcional, com habilidades abrangentes e experiência comprovada em IA, aparenta não precisar da ajuda."
                ]
    allOptionsList.append(options04)
    for idx, selectMessage in enumerate(listOfLabelMessage):
        optionResult = createASelectionOption(st, selectMessage,allOptionsList[idx], keyValue + '_' + str(idx) )
        allResults.append(optionResult)
        if showAnswer:
            st.write("Opcao escolhida: ", optionResult)
        st.write("--------------------------------------------------------------------------")
    return allResults

def selectOptionsDefinitionMaturity(st, keyValue, showAnswer = False):
    # §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
    st.subheader("Critério: Detalhamento/maturidade tecnológica")
    st.markdown('##### ------------------------------------------------------------------------------------------')

    allResults = []

    allOptionsList = []
    #### primeira Lista
    listOfLabelMessage=["Q5 - Nível de desenvolvimento da tecnologia atual (ideia,protótipo,MVP,produto final)"
                        ,"Q6 - Maturidade para implementar IA (tem dados e clareza na definição do problema)"
                        ,"Q7 - Objetivo ao participar do programa compatível com o que é oferecido"
                         ]
    options01 = ["Selecione uma opção:"
                 ,"1. Ideia - A solução está no estágio inicial de concepção."
                 ,"2. Protótipo - A solução está em fase de prototipagem inicial."
                 ,"3. MVP - A solução tem um Produto Mínimo Viável funcional."
                 ,"4. Produto final - A solução está totalmente desenvolvida e pronta para lançamento."
                 ,"5. Comercializado - A solução está sendo comercializada com necessidade de melhorias."
                 ]
    allOptionsList.append(options01)

    options02 = ["Selecione uma opção:"
                 ,"1. A startup possui pouca ou nenhuma clareza na definição do problema e dados insuficientes."
                 ,"2. A startup tem alguma clareza na definição do problema, mas dados limitados."
                 ,"3. A startup tem definição moderada do problema e dados razoáveis."
                 ,"4. A startup possui boa clareza na definição do problema e dados suficientes para implementação."
                 ,"5. A startup tem definição clara e precisa do problema e dados abrangentes e prontos para a implementação de IA com recursos próprios."
                ]
    allOptionsList.append(options02)
    options03 = ["Selecione uma opção:"
                 ,"1. O objetivo da startup é pouco compatível com o que o programa oferece."
                 ,"2. O objetivo da startup é algo compatível com o que o programa oferece."
                 ,"3. O objetivo da startup é moderadamente compatível com o que o programa oferece."
                 ,"4. O objetivo da startup é altamente compatível com o que o programa oferece."
                 ,"5. O objetivo da startup é perfeitamente compatível com o que o programa oferece."
                ]
    allOptionsList.append(options03)
    for idx, selectMessage in enumerate(listOfLabelMessage):
        optionResult = createASelectionOption(st, selectMessage,allOptionsList[idx], keyValue + '_' + str(idx) )
        allResults.append(optionResult)
        if showAnswer:
            st.write("Opcao escolhida: ", optionResult)
        st.write("--------------------------------------------------------------------------")
    return allResults
  

def selectOptionsDefinitionPotencial(st, keyValue, showAnswer = False):
    # §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
    st.subheader("Critério: Potencial de negócio")
    st.markdown('##### ------------------------------------------------------------------------------------------')
    allResults = []

    allOptionsList = []
    #### primeira Lista
    listOfLabelMessage=["Q8 - Diferenciação e inovação da solução"
                       ,"Q9 - Modelo de negócio e estratégias de mercado" 
                       ,"Q10 - Capacidade de atração de investimentos e parcerias internas ou externas"
                       ]
    options01 = ["Selecione uma opção:"
                 ,"1. A solução possui pouca ou nenhuma diferenciação ou inovação."
                 ,"2. A solução tem alguma inovação, mas pouca diferenciação em relação ao mercado."
                 ,"3. A solução possui inovação moderada e alguma diferenciação."
                 ,"4. A solução é altamente inovadora e bem diferenciada."
                 ,"5. A solução é extremamente inovadora e única no mercado."
                ]
    allOptionsList.append(options01)

    options02 = ["Selecione uma opção:"
                 ,"1. O modelo de negócio é fraco e as estratégias de mercado são pouco definidas."
                 ,"2. O modelo de negócio é básico e as estratégias de mercado são limitadas."
                 ,"3. O modelo de negócio é razoável e as estratégias de mercado são moderadamente definidas."
                 ,"4. O modelo de negócio é forte e as estratégias de mercado são bem definidas."
                 ,"5. O modelo de negócio é robusto e inovador, com estratégias de mercado altamente definidas e eficazes."
                ]
    allOptionsList.append(options02)
    options03 = ["Selecione uma opção:"
                ,"1. A startup tem pouca ou nenhuma capacidade de atrair investimentos ou parcerias."
                ,"2. A startup tem alguma capacidade de atrair investimentos ou parcerias."
                ,"3. A startup tem capacidade moderada de atrair investimentos e parcerias."
                ,"4. A startup tem alta capacidade de atrair investimentos e parcerias significativas."
                ,"5. A startup tem excelente capacidade de atrair investimentos e parcerias estratégicas robustas."
                ]
    allOptionsList.append(options03)
    for idx, selectMessage in enumerate(listOfLabelMessage):
        optionResult = createASelectionOption(st, selectMessage,allOptionsList[idx], keyValue + '_' + str(idx) )
        allResults.append(optionResult)
        if showAnswer:
            st.write("Opcao escolhida: ", optionResult)
        st.write("--------------------------------------------------------------------------")
    return allResults

def defineStartupNames(st, totalStartups):
    companyNames = []
    for idx in range(totalStartups):
        zeroStr = ''
        if idx < 9:
            zeroStr = '0'
        strNumber = idx + 1

        strCompany = chr(ord('A') + idx)

        company = st.text_input(f"Startup {zeroStr}{strNumber}:", strCompany )
        companyNames.append(company)
    return companyNames

def retrieveIntegerAnswersCompany(companyResponse):
    companyAnswers = []
    for answer in companyResponse:
        for option in answer:
            optionInt = int(option[0])
            companyAnswers.append(optionInt)
    return companyAnswers

def createDatasetAnswer(config):
    datasetList = []
    companyNames = []
    resultsFromCompany = config['resultsFromCompany']
    for key in resultsFromCompany.keys():
            companyNames.append(key)
    if config['test']:
        datasetList = [
                       [1,1,1,1,1,1,1,1,1,1]
                       ,[4,4,4,5,3,4,4,4,4,4]
                       ,[4,4,3,2,3,4,3,3,3,3]
                       ,[2,1,2,1,2,3,2,2,1,1]
                       ,[3,3,2,2,2,3,2,3,2,2]
                       ,[5,5,5,5,5,5,5,5,5,5]
                      ]
    else:
        for key in resultsFromCompany.keys():
            companyNow =  resultsFromCompany[key]
            companyResults = retrieveIntegerAnswersCompany(companyNow)
            datasetList.append(companyResults)
    
    dataset = np.array(datasetList)
    return companyNames, dataset



def showResults(st,config):
    st.write('ResultFinal:')
    #st.write(config)

    companies , dataset = createDatasetAnswer(config)
    if config['test']:
        st.write(companies)
    columnNames = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9', 'Q10']
    datasetResults = pd.DataFrame(dataset, index=[companies],columns=columnNames)
    st.write(datasetResults)
    # Call Electre Tri-B Function
    W = config['W']
    Q = config['Q']
    P = config['P']
    V = config['V']
    B = config['B']
    classification = electre_tri_b(dataset, W , Q , P , V , B , cut_level = 0.8, verbose = True, rule = 'pc', graph = False)
    className = ['A=Acima da expectativa', 'B=Aprovada','C=Abaixo da expectativa']
    for i in range(0, len(classification)):
        if config['test']:
            print('Startup ' + companies[i] +': '+' Class: '+str(className[classification[i]]))
        classificationResult= 'Startup ' + companies[i] +': '+ str(className[classification[i]])
        st.write(classificationResult)
        

    
    

