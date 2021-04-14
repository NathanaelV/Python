# Class Challenge 10

# Inserir um salário e calcular o aumento
# Aumento de 15% para quem ganha até R$ 1250,00
# Aumento de 10% para quem ganha acima de R$ 1250,00

s = float(input('Qual é o seu salário? '))

if s <= 1250:
    s1 = s * 1.15
    print('Seu salário com aumento de 15 % será R$ {:.2f}'.format(s1))
else:
    s2 = s * 1.1
    print('Seu salário com aumento de 10% será de R$ {:.2f}'.format(s2))
