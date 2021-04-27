# PARTE 1
# 1º Passo: Entrar no link (Google Drive)
# 2º Passo: Entrar na pasta Aula 1
# 3º Passo: Fazer o Download da base de Vendas (Excel)

# PARTE 2
# 4º Passo: Calcular os idicadores (Faturamento e quantidade de produtos
# 5º Passo: Entrar no meu email
# 6º Passo: Criar o email
# 7º Passo: Enviar o email

import pyautogui
import pyperclip
import time


pyautogui.PAUSE = 1


# 4º PASSO: Calcular os indicadores (Faturamento e Quantidade de Produtos)

# Muito bom para analise de dados. O as pb é apenas um atalho para chamar o comando
import pandas as pd

# Para poder usar o comando display
# Esse comando não é nescessário no Jupyter
from IPython.display import display

# Comando para ler a tabela.
# Colocar o r antes do texto, para ler literal o que está ali.
# Não vai interpretar os \n se aparecer.
tabela = pd.read_excel(r'C:\Users\tmnts\Downloads\Vendas - Dez.xlsx')

# para ler abas diferentes, (C:\Users...Dez.xlsx, sheet_name=n)
# n = Nº da aba que deseja ler

# Visualizar tabelas. Melhor que o print
# print(tabela)
display(tabela)  # No Pycharm fica igual ao print()

# Fazer os cálculos pelo Python
faturamento = tabela['Valor Final'].sum()
qtde_produtos = tabela['Quantidade'].sum()
print(f'Total do faturamento: {faturamento}')
print(f'Quantidade total de produtos: {qtde_produtos}')


# 5º PASSO: Entrar no meu email

# Copiando o Passo 1:
# Mudar do Pycharm para o Google
pyautogui.hotkey('alt', 'tab')

# Abrir uma nova aba
pyautogui.hotkey('ctrl', 't')

link = 'https://mail.google.com/'

# Copiar o link
pyperclip.copy(link)

# Colar o link
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Esperar o email carregar
time.sleep(6)


# PARTE 6: Criar o email

pyautogui.click(78, 205)
time.sleep(2)
pyautogui.write('tmntsplinter04@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
titulo = 'Aula de Python pela Hashtag Programação\n'
pyperclip.copy(titulo)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')


corpo = f'''Esse é o corpo do email.

Será que dá para escrever muita coisa aqui? 
Acento só funciona com comando Ctrl + c e Ctrl + v.
Caso contrário não funcionará.

Terei que colocar o faturamento nesse texto, então segue a baixo

Faturamento: R$ {faturamento:,.2f}
Quantidade de Produtos: {qtde_produtos:,}

Obrigado!
Tem um bom dia.'''


pyautogui.write('Primeira linha do corpo do email.\n')
pyperclip.copy(corpo)
pyautogui.hotkey('ctrl', 'v')


# 7º PASSO: Enviar o email

pyautogui.press('tab')
pyautogui.press('enter')

# Ou uso o atalho Ctrl + Enter: Ele manda o email

# Import os - para ver arquivos que vem com nome diferente
