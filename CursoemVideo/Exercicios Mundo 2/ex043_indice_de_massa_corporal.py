# Class Challenge 12

# Inserir peso e altura e calcular o IMC
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
print('Vamos calcular o seu IMC?')
h = float(input('Insira sua altura em metros: '))
m = float(input('Qual o seu peso? Não vale mentir: '))
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
