
# Take a number as input from user and print its Factorial using Iteration

n = int(input('\nEnter the number : '))

prod = 1
for i in range(1, n+1):
    prod = prod*i

print(n, end='! --> ')
print(prod, '\n')