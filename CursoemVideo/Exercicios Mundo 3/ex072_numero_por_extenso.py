# Class Challenge 16

# Uma tupla com contagem até 20 por extenso.
# Usuario vai digita o valor e vai mostrar o valor por extendo.
# Só é valido números entre 0 e 20:
# um dois tres quatro

count = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
         'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
user = int(input('Enter a number between 0 and 20: '))
while not 0 <= user <= 20:
    user = int(input('Invalid! Please enter a number between 0 and 20: '))
print(f'The number {user} if full is: {count[user]}')
