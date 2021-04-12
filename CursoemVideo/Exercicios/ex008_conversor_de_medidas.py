# Class Challenge 007
# Converter metros para centimetros e milimetros

a = float(input('Digite o valor em Metros: '))
c = a * 100
m = a * 1000
print('{} metros é igual a {} cm e {} mm'.format(a, c, m))

# Teacher example
m = float(input('Digite a distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O Valor {} m corresponde a:\n{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format(m, km, hm, dam, dm, cm, mm))
