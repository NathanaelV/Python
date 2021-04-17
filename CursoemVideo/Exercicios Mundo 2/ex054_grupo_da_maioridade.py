# Class Challenge 13

# Ler o ano de nascimento de 7 pessoas e verificar quantos já atingiram os 18 anos.
# Mostrar quantos temm 18 ou 21, ou mais e quantos ainda não completaram.
from datetime import date

s = 0
for c in range(1, 8):
    nascimente = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = date.today().year - nascimente
    if idade >= 18:
        s += 1
print('No grupo têm {} pessoa(s) que chegaram na maioridade.'.format(s))
print('No grupo têm {} pessoa(s) que não chegaram na maioridade.'.format(7 - s))
