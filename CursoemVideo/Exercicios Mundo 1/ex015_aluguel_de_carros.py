# Class Challenge

# Calcular o aluguel do carro, com entrada dos dia e Km rodados.
# Sendo R$60/dia e R$0,15/Km

d = int(input('\nQuantos dias você ficou com o Carro? '))
km = float(input('Quantos Km você rodou com o carro? '))

r = d * 60 + km * 0.15

print('O valor total a pagar pelo aluguel será: R${:.2f}'.format(r))
