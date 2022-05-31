
# Take a number as input and return the Prime Factors of the number

n = int(input('\nEnter a number : '))

print('Prime factors of', n, 'are : ', end='')
for i in range(1,n):
    if n%i==0:
        print(i, end=', ')
print(n, '\n')