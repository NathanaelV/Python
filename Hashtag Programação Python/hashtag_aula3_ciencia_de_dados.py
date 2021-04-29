# AULA 3: Passo a Passo de um Projeto de Ciência de Dados

# PASSO 1: Entendimento do Desafio
# PASSO 2: Entendimento da Área/Empresa
# PASSO 3: Extração/Obtenção de Dados
# PASSO 4: Ajuste de Dados (Tratamento/Limpeza)
# PASSO 5: Analise Exploratória
# PASSO 6: Modelagem + Algoritmos (Aqui que entra inteligência Artificial, se nescessário)
# PASSO 7: Interação de Resultados

import pandas as pd

tabela = pd.read_csv('advertising.csv')
# Caso as colunas venha separadas por ; ou , juntos em uma coisa só.
# pd.read_cvs('Nome_do_arquivo.csv, sep=; ou ,) Vai depender do que estiver separando as coulunas
# display(tabela)
print(tabela)


# PASSO 4: Ajuste de Dados (Tratamento/Limpeza)
print(tabela.info())
# Não há valores para serem tratados
# Analisar os valores Tv, Rádio e Jornal estão em milhares
# Vendas deve estar em milhão


# PASSO 5: Analise Exploratória

import seaborn as sns
import matplotlib.pyplot as plt


# fazer uma analise mais profunda
# Ver como cada informação está distribuida.
# Ver comos as informações estão ligadas entre sí

# Para analise de gráficos: 3 boas bibliotecas(seaborn, matplotlib, e o da aula 2)
print('\nMostrando Gráficos:\n')
sns.pairplot(tabela)
plt.show()

# Gráfico de barras: O Menor está na esquerda e o maior na direita
# Barra grande na esquerda: Muitos casos com pouco valor
# Barra pequena na direita: Poucos casos com muito valor

# Gráficos de pontinhos: Se o gráfico está muito espalhado não tem muito significado
# Caso o s pontilhados formem um desenho, começa ter uma ligação, proporcionalidade

# Criar um mapa de calor, para ver uma correlação
# corr(): Correlação
# cmpa='Wistia': Estilização de cores e escolha do padrão de cores
# annot=True:
# Para visualizar esse mapa, tenho que fechar a visualização do anterior
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)
plt.show()

# Correlação, varia de -1 a 1. Quando é proximo de 0 não há muita correlação
# Quanto mais próximo de 1 ou -1, maior a correlação + proporcional - inversamente proporcional
# Ver o que eu quero prever e como cada item influencia nisso, no caso VENDAS

# Quando analiso TV com os outros meios, o valor não pode ser muito grande.
# Significa que, se investir em um, investe a mesma coisa no outro

# Se tem dois itens como rádio e TV tem correlação MUITO próximo de 1 ou -1 tem que tirar um deles para prever as
# vendas. Caso contrário a I.A não reconhece bem


# Inteligência Artificial

# Usa uma base de dados tratada.
# Criar um modelo de IA. Toda IA deve ser treinada
# Não posso passar muitos informações de uma vez para a IA, caso contrário vai ficar abituada só com aquela base e não
# saberá fazer previsões
# PROBLEMA: Overfitting

# Passar 70% ou 80% da base de dados. Depois mostra os outros 20% para avaliar se está prevendo bem


import sklearn


# O CERTO DEVERIA SER: from sklearn.model_selection import train_test_split

# Train_test_split vai ajudar com o treino e validação de dados

# X são os valores que serão usados para fazer previsão
# Y é o que eu quero prever

x = tabela.drop('Vendas', axis=1)  # Excluir a coluna de Vendas
y = tabela('Vendas')

x_treino, x_teste, y_treino, y_teste = sklearn.cross_decomposition.train_test_split(x, y, test_size=0.3)

# TRANSFERIDO PARA O JUPYTER