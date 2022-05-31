
# Take a number as input and return the Factorial of that number using "Recursion" method

def fact(n):
    if n==0 or n==1:
        return (1)
    else:
        return (n*fact(n-1))

n = int(input('\nEnter a number : '))
f = fact(n)
print(n, 'factorial is :', f, '\n')