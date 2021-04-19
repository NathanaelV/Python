# Class challenge 15

# The user will enter the amount he wants to withdraw in cash.
# The banknotes only has R$ 50 bills, R$ 20 bills, R$ 10 bills and R$ 1 bills

n = int(input('How much do you want withdraw? R$ '))
n50 = n20 = n10 = n1 = 0
while n // 50 > 0:
    n50 += 1
    n -= 50
while n // 20 > 0:
    n20 += 1
    n -= 20
while n // 10 > 0:
    n10 += 1
    n -= 10
print(f'You will receive {n50} bills of R$ 50.00')
print(f'You will receive {n20} bills of R$ 20.00')
print(f'You will receive {n10} bills of R$ 10.00')
print(f'You will receive {n} bills of R$ 1.00')
