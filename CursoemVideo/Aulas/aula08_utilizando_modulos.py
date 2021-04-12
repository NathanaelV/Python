# Challenge 16 - 21

# Da biblioteca math
# ceil: arredonda para cima, sem casas decimais
# floor: arredonda para baixo, sem casas decimais
# trunc: Elimida da virgula par frente, não arredonda
# pow: Esponencial
# sqrt: Raiz quadrada
# factorial: Fatorial
# import math: Importa todas as funções de matematica
# from math import sqrt: Só importa a raiz quadrada
    # Quando uso o comando from math import, não preciso mais colocar
    # math.expressão. Só escrever a espressão

# Usar a biblioteca importando tudo
# import math  # nesse caso tenho que usar o comando math.expressão
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada do nº {} é {:.2f}'.format(num, floor(raiz)))


