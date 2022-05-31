
# Take the Base and Power as input and print the result (without using direct mathematical operator of python) using While-loop

b = int(input('\nEnter a number (base) : '))
p = int(input('Enter a number (power) : '))

prod = 1
t = p
while t>0:
    prod = prod * b
    t = t - 1

print(b, 'to the power of', p, 'is : ', prod, '\n')