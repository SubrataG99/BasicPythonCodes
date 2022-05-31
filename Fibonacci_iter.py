
# Take number of elements from user and print the Fibonacci series using Iteration 
# Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

n = int(input('\nEnter the limit of series : '))

a = 0
b = 1
sum = 0
print('The series upto',n,'terms are :', end=' ')
print(a, ',', end=' ')
for i in range(n-2):
    sum = a + b
    a = b
    b = sum
    print(a,',', end=' ')
print(sum, '\n')