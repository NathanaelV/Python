# Class Challenge 15

# read several integers and only stop when typing 999
# Show how many numbers were entered and what is the sum.
# Can't add output variable, 999.
# I need to use f string

c = s = n = 0
while True:
    n = int(input('Enter a number [type 999 to exit]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'{c} number(s) were entered and its(their) sum is {s}.')
