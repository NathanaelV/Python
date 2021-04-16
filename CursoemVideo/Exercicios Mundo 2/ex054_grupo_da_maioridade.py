# Class Challenge 13

# Ler o ano de nascimento de 7 pessoas e verificar quantos já atingiram os 18 anos.
# Mostrar quantos temm 18 ou 21, ou mais e quantos ainda não completaram.
from datetime import date

s = 0
for c in range(0, 7):
    nascimente = int(input('Digite a data de nascimento: '))
    idade = date.today().year - nascimente
    if idade >= 18:
        s += 1
print('No grupo têm {} pessoa(s) que chegaram na maioridade.'.format(s))
