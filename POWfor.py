
# Take the Base and Power as input and print the result (without using direct mathematical operator of python) using For-loop

b = int(input('\nEnter a number (base) : '))
p = int(input('Enter a number (power) : '))

prod = 1
for i in range(p):
    prod = prod * b

print(b, 'to the power of', p, 'is : ', prod, '\n')