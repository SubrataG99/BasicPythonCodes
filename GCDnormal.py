
# Take two numbers from User as input and then find the GCD (Greatest Common Divisor) of the two

a = int(input('\nEnter the first number : '))
b = int(input('Enter the second number : '))

if a>=b:
    for i in range(1, b+1):
        if a%i==0 and b%i==0:
            g = i
else:
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            g = i

print('GCD or HCF of', a, 'and', b, 'is :', g, '\n')