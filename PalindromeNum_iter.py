
# Take a number and check whether it is a Palindrome number or not
# (12321) --> Palindrome
# (1234) --> Non-Palindrome

n = int(input('\nEnter a number : '))

s = n
sum = 0

while n>0:
    sum = (sum*10) + (n%10)
    n = n//10

if sum==s:
    print('The original number = ', s)
    print('The reversed number = ', sum)
    print("Palindrome number...\n")
else:
    print('The original number = ', s)
    print('The reversed number = ', sum)
    print('Non Palindrome number...\n')