
# Find sum of 2 integer numbers given by User but "without using the + operator"

a = int(input('\nEnter a number : '))
b = int(input('Enter another number : '))

while b!=0:
    carry = a & b                                           # carry = common set bits of 'a' and 'b'
    a = a^b                                                 # sum of bits of 'a' and 'b' where at least one of the bits is not set
    b = carry<<1                                            # carry is shifted by one so that adding it to 'a' gives result

print('Sum of the above 2 numbers without any arithmetic operator is :', a)