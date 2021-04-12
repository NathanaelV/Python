# Class Challenge 007

# Calcular a area da parede a quantidade de tinta necessária
# Cada litro de tinta pinta 2 m²

h = float(input('Digite a altura em metros: '))
l = float(input('Digite a largura em metros: '))

a = h * l
t = a / 2

print('\nA área da parede tem {:.2f} m².'.format(a))
print('Será necessário {:.3f} litros de tinta para pintá-la.\n'.format(t))
print('Sua parede de {:.2f} x {:.2f} e a área é {:.2f} m².'.format(h, l, a))
print('Para pintar a parede será necessário {:.3f}l de tinta'.format(t))

