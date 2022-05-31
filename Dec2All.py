
# Take a decimal number from User and print its equivalent Binary, Octal & Hexadecimal

n = int(input('\nEnter the number in decimal : '))

#-----------------------------------------From Decimal to Binary
def dec2bin(n):
    t = 0
    while n>0:
        t = (10*t) + (n%2)
        n = n//2
    bin = 0
    while t>0:
        bin = (10*bin) + (t%10)
        t = t//10
    return (bin)

#----------------------------------------From Decimal to Octal
def dec2oct(n):
    t = 0 
    while n>0:
        t = (10*t) + (n%8)
        n = n//8
    oct = 0
    while t>0:
        oct = (10*oct) + (t%10)
        t = t//10
    return (oct)

#---------------------------------------From Decimal to Hexadecimal
def dec2hex(n):
    hexvar = ['A', 'B', 'C', 'D', 'E', 'F']
    temp = ''
    while n>0:
        if (n%16) >= 10:
            temp = temp + hexvar[10-(n%16)]
        else:
            temp = temp + str(n%16)
            n = n//16
    hexa = ''
    for i in range(len(temp)-1, 0, -1):
        hexa = hexa + temp[i]
    return (hexa)

#-------------------------------------Final print
print('The Binary equivalent of', n, 'is :', dec2bin(n))
print('The Octal equivalent of', n, 'is :', dec2oct(n))
print('The Hexadecimal equivalent of', n, 'is :', dec2hex(n), '\n')