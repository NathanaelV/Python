# Class Challenge 10

# Ler 3 segmentos de Reta e dizer se pode ser um triângulo

l1, l2, l3 = input('Digite o valor de 3 segmentos de reta para saber se forma um triângulo:\n').split()
l1, l2, l3 = int(l1), int(l2), int(l3)

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo com esses segmentos de reta.')
else:
    print('Não é possível formar um triângulo com esses segmentos de reta.')
