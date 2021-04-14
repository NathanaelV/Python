# Class Challenge 10

# Inserir um salário e calcular o aumento
# Aumento de 15% para quem ganha até R$ 1250,00
# Aumento de 10% para quem ganha acima de R$ 1250,00

s = float(input('Qual é o seu salário? R$ '))
# Colocar o R$ evita que o usuário digite o R$ e de problema no código

if s <= 1250:
    s1 = s * 1.15
    print('Seu salário de R$ {:.2f} com aumento de 15 % será R$ {:.2f}'.format(s, s1))
else:
    s2 = s * 1.1
    print('Seu salário de R$ {:.2f} com aumento de 10% será de R$ {:.2f}'.format(s, s2))

# Exemplo do professor

print('\nExemplo do professor:')
if s <= 1250:
    novo = s * 1.15
    p = 15
else:
    novo = s * 1.1
    p = 10
print('Seu salário de {:.2f} será de {:.2f} com aumento de {}%.'.format(s, novo, p))
