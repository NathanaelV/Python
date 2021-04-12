# Class Challenge 08

# Ler um determinado angulo e dar o valor do Sin, Cos e Tan
import math
d = float(input('Digite o ângulo em graus: '))
r = math.radians(d)
s = math.sin(math.radians(d)) # Posso colocar uma função dentro da outra
c = math.cos(r)
t = math.tan(r)
print('Seno: {:.4f}\nCosseno: {:.4f}\nTangente {:.4f}'.format(s, c, t))
