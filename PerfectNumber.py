
# Take a number and check whether the number is a perfect number or not
# Perfect number = Sum of the divisors of the number is same as the number

n = int(input('\nEnter a number : '))
s = 0
print('Factors of', n, 'are :', end='')
for i in range(1, n):
    if n%i==0:
        s = s + i
        print(i, end=' ')
if s==n:
    print('\n', n, 'is a perfect number\n')
else:
    print('\n', n, 'is NOT a perfect number\n')