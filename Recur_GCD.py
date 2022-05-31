
# Take two numbers as input and find GCD (Greatest Common Divisor) using "Recursion" method

a = int(input('\nEnter a number : '))
b = int(input('Enter another number : '))

def GCD(a, b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a==b:
        return a
    elif a>b:
        return GCD(a-b, b)
    return GCD(a, b-a)

print('GCD of', a, 'and', b, 'is : ', GCD(a, b), '\n')