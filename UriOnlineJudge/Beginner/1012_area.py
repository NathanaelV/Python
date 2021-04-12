import math
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
Triangle = (A * C) / 2
T = math.erf()
Circle = (3.14159 * C ** 2)
Trapezium = (A + B) * C / 2
Square = B ** 2
Rectangle = A * B
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}'.format(Triangle, Circle))
print('TRAPEZIO: {:.3f}\nQUADRADO: {:.3f}'.format(Trapezium, Square))
print('RETANGULO: {:.3f}'.format(Rectangle))
