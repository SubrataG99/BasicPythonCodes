
# Take a number as input and return the Sum of the digits of the number using "Recursion" method

def DigSum(n):
    if n==0:
        return 0
    return ((n%10) + DigSum(n//10))

#--------------------------------------------Main program
n = int(input('\nEnter a number : '))
sum_digit = DigSum(n)
print('Sum of digits of', n, 'is :', sum_digit)