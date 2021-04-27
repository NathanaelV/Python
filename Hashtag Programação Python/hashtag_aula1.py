# Automação de Sistemas e Processos em Python

# Anotar os passos que eu faria. Depois pensar em como passar isso para o Python

# 1º Passo: Entrar no link (Google Drive)
# 2º Passo: Entrar na pasta Aula 1
# 3º Passo: Fazer o Download da base de Vendas (Excel)
# 4º Passo: Calcular os idicadores (Faturamento e quantidade de produtos
# 5º Passo: Entrar no meu email
# 6º Passo: Criar o email
# 7º Passo: Enviar o email

# Importar as bibliotecas: pyautogui: Automação do mouse e teclado
# pyperclip: Permite copiar e colar

import pyautogui
import pyperclip
import time

# Tempo que vai esperar para execultar um comando em segundos
# Caso seja digitado muito rápido, pode dar problema
pyautogui.PAUSE = 1

# Exibir um alerta de que o código vai rodar e o usuário vai ter que parar de usar o computador
pyautogui.alert('''ATENÇÃO!!!
Em quanto o código estiver rodando você NÃO poderá usar o Computador.
Deseja continuar?''')

# Mudar para a aba do google:
pyautogui.hotkey('alt', 'tab')

# 1º Passo: Entrar no link do Google Drive:
# Abrir uma aba no Google
pyautogui.hotkey('ctrl', 't')  # Usado para atalhos


# O Que fazer para abrir o navegador:
#    pyautogui.press('win')
#    pyautogui.write('google')
#    pyautogui.press('enter')


# Comando para escrever um texto
# Para links é melhor usar o comando Ctrl + c e Ctrl + v.
# Quando digitar um link ele vai sendo completado a medida que é digitado
link = 'https://drive.google.com/drive/folders/1uAPJrEMKDcGpxa9u48y9SJsRN0SXxO4C'

# Pedir para o Pc dar Ctrl + c e Ctrl + v no link
# Para copiar uma informação que está no meu código, uso o pyperclip

# Copia o link:
pyperclip.copy(link)

# Cola o link
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')  # Para apertar uma tecla

pyautogui.write('')  # Para escrever na tela

# Esperar um pouco para a pagina carregar
time.sleep(5)


# 2º Passo: Entrar na Pasta Aula 1:
# Para saber a posição do Mous na tela do computador:
# Fazer o programa esperar um tempo para dar tempo posicionar o mouse onde deseja

'''
time.sleep(5)
print(pyautogui.position())
'''


# Posições x e Y para o computador clicar.
# Importante checar a posição no computador que vai rodar o programa.
# Se a tela não tiver o mesmo tamanho e nem a mesma formação, pode dar problema
pyautogui.click(320, 283, clicks=2)
time.sleep(0.5)

# Para deixar a tela em tela cheia
# pyautogui.hotkey('winup')

# Fazer o download do arquivo
pyautogui.click(348, 431)
pyautogui.click(1157, 192)
pyautogui.click(950, 596)

# Abrir na pasta e deletar
time.sleep(2)
pyautogui.click(208, 698)  # Clicar na seta de download
time.sleep(1)
pyautogui.click(293, 637)  # Clicar: Mostra na pasta
time.sleep(2)
pyautogui.hotkey('del')

