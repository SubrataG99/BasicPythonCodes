
# Take an integer number as input and check if it is a prime number or not

n = int(input('\nEnter a number : '))

flag = 0
for i in range(2, n//2):
    if n%i==0:
        flag+= 1

if flag>1:
    print('It is not a Prime number...\n')
else:
    print('It is a Prime number...\n')