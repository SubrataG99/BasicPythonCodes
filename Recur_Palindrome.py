
# Take a number as input and check whether it is a Palindrome number using "Recursion" method

def rev(n, temp):
    if n==0:
        return temp
    temp = (10*temp) + (n%10)
    return rev(n//10, temp)

n = int(input('\nEnter a number : '))
temp = rev(n, 0)
if temp==n:
    print('Your input :', n)
    print('Reversed number :', temp)
    print('The number is PALINDROME\n')
else:
    print('Your input :', n)
    print('Reversed number :', temp)
    print('The number is NOT PALINDROME\n')