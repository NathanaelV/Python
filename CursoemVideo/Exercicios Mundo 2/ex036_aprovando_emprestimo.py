# Class Challenge 12

# Perguntar o valor da casa, salário e em quantos anos vai pagar
# O valor da prestação NÃO pode ser maior que 30% do salário

cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

print('{}Aprovando Emprestimo:{}'.format(cores['vermelho'], cores['limpa']))

casa = float(input('{}Qual o valor da casa que deseja comprar? R${} '.format(cores['negrito'], cores['limpa'])))
salário = float(input('{}Qual o seu salário? R${} '.format(cores['negrito'], cores['limpa'])))
tempo = int(input('{}Em quantos anos de seja pagar? {}'.format(cores['negrito'], cores['limpa'])))

prestação = casa / (tempo * 12)

if prestação >= 0.3 * salário:
    print('\nPedido de emrprestimo {}NEGADO!{}'.format(cores['vermelho'], cores['limpa']))
    print('A prestação foi de R$ {:.2f} e não deveria ser maior que 30% do seu saláro.'.format(prestação))
    aprovado = round(casa / (0.3 * salário) // 12 + 0.5)
    prestação = casa / (aprovado * 12)
    print('Você deve pagar a casa em {}{} anos{}, para o pedido de emprestimo ser aceito'
          .format(cores['negrito'], aprovado, cores['limpa']))
    print('E terão parcelas de {}R$ {:.2f}{}'.format(cores['negrito'], prestação, cores['limpa']))
else:
    print('\nPedido de emprestimo {}ACEITO!{}'.format(cores['verde'], cores['limpa']))
    print('Suas parcelas serão de {}R$ {:.2f}{} por mês'
          .format(cores['negrito'], prestação, cores['limpa']))

# Exemplo do professor:
# Exemplo semelhante
