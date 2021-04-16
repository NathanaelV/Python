# Class Challenge 12

# Inserir peso e altura e calcular o IMC
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
print('Vamos calcular o seu IMC?')
h = float(input('Insira sua altura? (m): '))
m = float(input('Qual o seu peso? (Kg)): '))
IMC = m / h**2
if IMC < 18.49:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.\nProcure um médico.'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.1f}. Você está no Peso ideal.'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.1f}. Você está com Sobrepeso.\nProcure um médico.'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.1f}. Você está Obeso.\nProcure um médico rápido.'.format(IMC))
else:
    print('Seu IMC é {:.1f}. Você está com Obesidade Mórbida.\nProcure um médico Urgentemente!!!'.format(IMC))

# Exemplo do professor:

print('\nExemplo do professor:')
print('O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.49:
    print('Você está abaixo do peso.')
elif IMC < 25:
    print('Peso normal')
elif IMC < 30:
    print('Você está com Sobrepeso')
elif IMC < 40:
    print('Você está Obeso')
else:
    print('Você está com Obesidade Mórbida')