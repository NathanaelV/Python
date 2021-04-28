# Análise de Dados com Python

# DESAFIO:
# A empresa de telecom tem vários seviços diferente, entre os principais: Internet e Telefone
# O PROBLEMA:
# Analisar o histórico dos últimos anos, você percebeu que a empresa está com Chum de mais de 26%
# Chum: clientes não estão renovando o contrato
# Isso representa uma grande perda para empresa. Como resolver?


# Colocar a base de dados na mesma pasta do arquivo de Python


# PASSO 1: Importar a base de dados
# PASSO 2: Visualizar a base de dados para entender o que temos disponivel
# PASSO 3: Tratamento de Dados (A parte mais importante e que leva mais tempo)
# PASSO 4: Olhar como que estão distribuidos os Churns/Cancelamento
# PASSO 5: Fazer uma analise das causas dos cancelamentos


# PASSO 1: Importar a base de dados
# PASSO 2: Visualizar a base de dados para entender o que temos disponível

import pandas as pd
from IPython.display import display

# Por estar no mesmo arquivo, não preciso escrever todo o caminho 'C:\projects\...nome do arquivo
tabela_clientes = pd.read_csv('telecom_users.csv')
display(tabela_clientes)
# print(tabela_clientes.columns)  # Para mostrar todas as Colunas


# PASSO 3: Tratamento de Dados

# Remover uma coluna da Tabela. Comando drop pode excluir linhas ou colunas
# axis=0 exclui a linha e axis=1 exclui a coluna
tabela_clientes = tabela_clientes.drop('Unnamed: 0', axis=1)
display(tabela_clientes)

# Cria uma nova coluna e preenche tudo com o valor atribuido ou substitui o valor se já existir
tabela_clientes['NovaColuna'] = 1

# Quando aparece None no Python, é idicação de valor vazio
# Em analise de Dados, deve-se tratar todos os espaços vazios
print(tabela_clientes.info())

# non-null quantidade de valores não nulos
# object são as que não são números

# Total gasto está como object, preciso trartar esse problema
# Coma a info eu quero resolver dois problemas
# Problemas de tipos de informação:
#    Quando deveria ser número mas o Python está lendo como texto
# pd.to_numeric(A coluna que desejo tratar, jeito que vou tratar o erro)
#    coerce ele ignora o erro, preenche por um espaço vazio.
tabela_clientes['TotalGasto'] = pd.to_numeric(tabela_clientes['TotalGasto'], errors='coerce')
print('\n\nTratamento de uma Coluna: TotalGastos\n')
print(tabela_clientes.info())

# Perdi 10 valores na transformação, comparado com os 5.986, não é relevante

# Problemas de valores vazios:
#    Colunas completamente vazias.
# oque eu quero.dropna(condição para toda coluna vazia, defino se é coluna ou linha)
tabela_clientes = tabela_clientes.dropna(how='all', axis=1)  # axis usado a cima
print('\n\nExcluindo a coluna só com valores vazios\n')
print(tabela_clientes.info())

# Excluir uma linha com pelo menos 1 valor vazio:
# dropna(how='any' ou nada: por padrão é any, axis=0: Por ser linha, mas também não preciso definir)
tabela_clientes = tabela_clientes.dropna()
print('\n\nTabela com linhas vazias excluída\n')
print(tabela_clientes.info())

# Eu sei que todos os valores vazios foram excluido poir os nom-null são todos iguais


# PASSO 4: Olhar com que estão distribuidos os Churns/Cancelados

# Contar valores na coluna Churn
print('\nQuantas Pessoas deram Churn ou não. (Cancelaram):')
print(tabela_clientes['Churn'].value_counts())
print('\nPara Mostrar porcentagem: 100% = 1')
print(tabela_clientes['Churn'].value_counts(normalize=True))
print('\nParar Imprimir em percentual formatada:')
print(tabela_clientes['Churn'].value_counts(normalize=True).map("{:.2%}".format))


# PASSO 5: Fazer uma analise das causas

# Biblioteca permite criar graficos interativos
import plotly.express as px

# Escolher a tabela que vou usar e determinar x=coluna
# color= definir se vai ter cor ou não
grafico = px.histogram(tabela_clientes, x='Churn', color='Churn')
grafico.show()  # Usado para gráficos
# No caso do PyCharm o gráfico será exibido em uma nova aba

grafico2 = px.histogram(tabela_clientes, x='ServicoInternet', color='Churn')
grafico2.show()
# Cada grafico é aberto em uma aba diferente
# A definição de cores pode ser com outra coluna, como Churn no caso
# Google: plotly express histogram Change Color
#    Para ver outros modos de mexer no gráfico

# Como fazer para todos os gráficos

print('\n\nUsando o For:\n')
for coluna in tabela_clientes:
    print(coluna)
    grafico = px.histogram(tabela_clientes, x=coluna, color='Churn')
    grafico.show()

# Escrever as Conclusões: Achar os 20% que resolvem os 80% do cancelamento
# - Genero não tem muita diferença entre eles.
# - Aposentados Também não tem grande diferênça
# - Casados: Parece que solteros tendem a cancelar mais
# - Dependentes: Pessoas que tem dependentes tendem a cancelar menos
# - Meses Como Cliente: Clientes desistem no começo
# - Serviço de Telefone: Proporcional
# - Multiplas linhas: Proporcional
# - Fibra: Grande diferênça
# - Serviço de segurança online: Grande diferença

# Pessoas com dependentes tendem a cancelar menos:
# Temos um problema sério em reter os cliente nos primeiros meses
#   - 1º Palpite: Estamos trazendo muitos clientes desqualificado
#   - 2º Palpite: Problemas em reter os clientes, o serviço no inicio não parece bom
# Verificar os problemas em relação ao serviço de Fibra
# Clientes com MUITO mais serviço tende a cancelar menos
#   - Propor plano/promoção para incentivar o cliente a contrartar serviços
# Contrato mensal tende a cancelar menos
#   - Propor promoções para contratos anuais
# Boleto eletrônico cancela mais
#   - Incentivar as formas eletrônicas, evitar os boletos eltrônicos
