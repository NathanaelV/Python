# Class Challenge 12

# Digitar um número e fazer a conversão para uma das opções:
# 1 - tBinário; 2 - Octal; 3 - Hexadecimal

while True:
      print('\033[1;32mEsse programa converte um número inteiro em uma das bases:\n'
            '\033[1;35m    1 - Binário\n\033[1;36m    2 - Octal\n\033[1;32m    3 - Hexadecimal\033[m\n'
            '    4 - SAIR')
      base = int(input('Deseja converter um número para qual base?: '))
      if 1 <= base <= 4:
            if base == 4:
                  break
            número = int(input('Digite o número que deseja converte: '))
            if base == 1:
                  print(f'O número {número} convertido para Binário é: {bin(número)[2:]}')
            elif base == 2:
                  print('O número {} convertido para Octal é: {}'.format(número, oct(número)[2:]))
            elif base == 3:
                  print('O número {} convertido para Hexadecimal é: {}'.format(número, hex(número)[2:].upper()))
      else:
            print('Por favor, digite uma opção válida. 1, 2, 3 ou 4.')
