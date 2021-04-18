# Class Challenge 14

# Melhor o jogo do ex 28. Número entre 0 e 10.
# Tentar até acertar, e contabilizar o número de tentativas

from random import randint
from time import sleep
print('{:-^46}'.format(' JOGO DA ADIVINHAÇÃO 2.0 '))
print('Consegue adivinhar o número que eu pensei??\nDica: É um número entre 0 e 10!')
comp = randint(0, 10)
i = 0
n = 11
print(comp)
while n != comp:
    n = int(input('Digite seu palpite: '))
    i += 1
    sleep(0.5)
    if n != comp:
        if n < comp:
            print('Não. Muito baixo!')
            sleep(0.5)
        else:
            print('Não. Muito alto!')
            sleep(0.5)
print('Parabén você acertou!!!')
sleep(0.5)
print('Levou apenas {} tentativa(s).'.format(i))
