# Class Challenge 12

# Entrar com o valor do produto e com a forma de pagamento
# À vista no dinheiro/cheque: 10% de desconto
# À vista no cartão débito: 5% de desconto
# Até 2x no cartão de crédito: preço normal
# 3x ou mais no cartão de crédito: 20% de juros no total
print('{:=^40}'.format(' LOJAS GUANABARAS '))
print('Hora de efetuar o pagamento')
print('-' * 48)
price = float(input('Qual o valor total da compra? '))
print('''Qual será a forma de pagamento?
    [ 1 ] - Dinheiro/cheque à vista. Desconto de 10%
    [ 2 ] - Cartão de débito à vista. Desconto de 5%
    [ 3 ] - Cartão de Crédito até 2x
    [ 4 ] - 3x ou mais no Cartão de Crédito. 20% de Juros''')
option = int(input('Digite uma opção de 1 a 4... '))

if option == 1:
    valor = price * 0.9
    print('O valor final com 10% de desconto será R$ {:.2f}'.format(valor))
elif option == 2:
    valor = price * 0.95
    print('O valor final com desconto de 5% será de R$ {:.2f}'.format(valor))
elif option == 3:
    print('O valor final será de R$ {:.2f}'.format(price))
elif option == 4:
    valor = price * 1.2
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = valor / parcela
    print('O valor com juros de 20% será de R$ {:.2f}.\nCada parcela será de R$ {:.2f}'.format(valor, valor_parcela))
else:
    print('Digite uma opão válida')
