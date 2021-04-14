# Class Challenge 10

# Se ultrapassar os 80 km/h, gera uma multa de R$ 7 para cada km/h acima do limite

v = int(input('Qual a velocidade do car? '))

if v <= 80:
    print('Parabéns, você está dentro do limite de 80 km/h')
else:
    m = (v - 80) * 7
    print('Você excedeu o limite de 80 km/h!')
    print('Sua multa será de R$ {},00'.format(m))
