# Class Challenge 12

# Digitar um número e fazer a conversão para uma das opções:
# 1 - Binário; 2 - Octal; 3 - Hexadecimal
print('\033[1;32mEsse programa converte um número inteiro em uma das bases:\n'
      '\033[1;35m    1 - Binário\n\033[1;36m    2 - Octal\n\033[1;32m    3 - Hexadecimal\033[m')
base = int(input('Deseja converter um número para qual base?: '))
número = int(input('Digite o número que deseja converte: '))
if base == 1:
      print('O número {} convertido para Binário é:\n{}'.format(número, bin(número)[2:]))
elif base == 2:
      print('O número {} convertido para Octal é:\n{}'.format(número, oct(número)[2:]))
elif base == 3:
      print('O número {} convertido para Hexadecimal é:\n{}'.format(número, hex(número)[2:]))
else:
      print('Por favor, digite uma opção válida. 1, 2 ou 3.')
