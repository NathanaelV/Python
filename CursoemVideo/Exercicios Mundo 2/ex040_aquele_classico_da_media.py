# Class Challenge 12
# Calcular a média e exibir uma mensagem:
# Abaixo de 5.0 reprovado, entre 5 e 6.9 recuperação e acima de 7 aprovado
cores = {'limpo': '\033[m',
         'negrito': '\033[1m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}
n1 = float(input('Insira a 1ª nota do aluno: '))
n2 = float(input('Insira a 2ª nota do aluno: '))
m = n1 * 0.5 + n2 * 0.5
if m < 5:
    print('Voce foi {0}REPROVADO!{1} Sua nota foi {2}{3:.1f}{1}'
          .format(cores['vermelho'],cores['limpo'], cores['negrito'], m))
elif m < 6.9:
    print('Você está de {0}RECUPERAÇÃO!{1} Sua nota foi {2}{3:.1f}{1}'
          .format(cores['amarelo'], cores['limpo'], cores['negrito'], m))
else:
    print('{0}PARABÉNS{1} você foi {2}APROVADO!{1} Sua nota foi {0}{3:.1f}{1}'
          .format(cores['negrito'], cores['limpo'], cores['verde'], m))
