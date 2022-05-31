
# Take two numbers in 2 variables and swap their value using third variable

a = int(input('\nEnter first number : '))
b = int(input('Enter second number : '))

print('Before swapping : ', end='')
print('a =', a, 'b =', b)

temp = a
a = b
b = temp
print('After swapping : ', end='')
print('a =', a, 'b =', b, '\n')