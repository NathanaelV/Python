# Challenge 107 - 112
# Criar modulos para dividir o meu programa, muito útil para programs muito grande
# Crio um outro arquivo Python e coloco as funções lá
# Quando precisar, só importar.

import uteis

# Quando eu crio módulos, não é recomendado usar a forma from uteis import fatorial
# O programa pode confundir com outras funções.
# Usar o uteis.dobro é mais seguro para o programa.
# Caso tenham duas funções com o mesmo nome, o Python execulta a última que foi importada


# Principal program
num = int(input('Enter a number: '))
fat = uteis.fatorial(num)
print(f'Factorial {num} is {fat}')
print(f'Double of {num} is {uteis.double(num)}')



# Pacotes

# Quando um módulo começa a ter muitas funções e novamente começa a ficar difícil
# a organização e manutenção nesses códigos
# Agora separo em pacotes (Bibliotecas em outras linguagens)
# O Pacote é uma pasta com vários módulos:
# Tratamento de números, Strings, datas, cores...

# Para importar um Pacote usa-se: import nomedopacote

from uteis import numeros

n = 98
t = numeros.triple(n)
print(f'Triple of {n} is {t}')

