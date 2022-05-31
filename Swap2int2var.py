
# Take two numbers in 2 variables and swap their value without any third variable

a = int(input('\nEnter first number : '))
b = int(input('Enter second number : '))

print('\nBefore swap : ', end=' ')
print('a =', a, 'b =', b)

sum = a+b
a = sum - a
b = sum - b

print('After swap : ', end=' ')
print('a =', a, 'b =', b, '\n')