
# Take a number as input and reverse the number (without using any Pre-defined Libraries)

n = int(input('\nEnter a number : '))

c = 0
s = 0
while n>0:
    s = (s*10) + (n%10)
    n = n//10
    c = c+1

print('\nIt is', c, 'digit number')
print('The reverse of the integer is : ', s)
print('Done...\n')