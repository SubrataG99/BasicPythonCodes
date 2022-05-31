
# Take any form of a number and print its Equivalent number

print('\n1. Decimal')
print('2. Binary')
print('3. Octal')
print('4. Hexadecimal')
choice = int(input('What you want to convert to decimal : '))

#---------------------------------------------------------------------From Binary to Decimal
def bin2dec(n):
    b2d = 0
    cnt = 0
    for i in range(len(n)-1, -1, -1):
        b2d = (b2d) + (int(n[i]) *(2**cnt))
        cnt = cnt + 1
    return (b2d)

#---------------------------------------------------------------------From Octal to Decimal
def oct2dec(n):
    o2d = 0
    cnt = 0
    for i in range(len(n)-1, -1, -1):
        o2d = o2d + (int(n[i]) * (8**cnt))
        cnt = cnt + 1
    return (o2d)

#---------------------------------------------------------------------From Hexadecimal to Decimal
def hex2dec(n):
    h2d = 0
    cnt = 0
    hexvar = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(n)-1, -1, -1):
        if n[i] in hexvar:
            h2d = h2d + ((16**cnt) * (10 + hexvar.index(n[i])))
            cnt = cnt + 1
        else:
            h2d = h2d + ((16**cnt) * int(n[i]))
            cnt = cnt + 1
    return (h2d)

#---------------------------------------------------------------------Print as per choice provided
if choice==1:
    n = int(input('Enter a decimal number : '))
    print('The decimal equivalent of', n, 'is :', n, '\n')
elif choice==2:
    n = str(input('Enter a binary number : '))
    print('The decimal equivalent of', n, 'is :', bin2dec(n), '\n')
elif choice==3:
    n = str(input('Enter a octal number : '))
    print('The decimal equivalent of', n, 'is :', oct2dec(n), '\n')
elif choice==4:
    n = str(input('Enter a hexadecimal number : '))
    print('The decimal equivalent of', n, 'is :', hex2dec(n), '\n')
else:
    print('Option not available...')