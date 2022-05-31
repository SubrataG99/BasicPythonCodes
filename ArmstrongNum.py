
# Take a number from integer and check if the number is Armstrong number (number = sum of (digits to power length of number))
#   Armstrong number example : 123 = 1**3 + 2**3 + 3**3

n = int(input('\nEnter a number : '))
n1 = n
digcnt = n
k = 0
s = 0

while digcnt>0:
    digcnt = digcnt//10
    k = k + 1

while n1>0:
    s = s + ((n1%10)**k)
    n1 = n1//10

if s==n:
    print(n, 'is an Armstrong number\n')
else:
    print(n, 'is not an Armstrong number\n')