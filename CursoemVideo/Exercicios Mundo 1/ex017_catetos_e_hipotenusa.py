# Class Challenge 08

# Ler o comprimento dos 2 catetos e calcular a Hipotenusa
# from math import sqrt
from math import sqrt, hypot
c1 = float(input('Digite a medida de um dos catetos: '))
c2 = float(input('Digite a medida do outro cateto: '))

hi = (c1**2 + c2**2) ** (1/2)
h = sqrt(c1**2 + c2**2)  # Se tivesse a biblioteca math seria math.sqrt()
h2 = hypot(c1, c2)  #Se tivesse a biblioteca math seria math.hypot()

print('A hipotenusa do triangulo é = {:.2f}.'.format(h))
print('Hipotenusa: {:.2f}'.format(h2))
print('Hipotenusa: {:.2f}'.format(hi))
