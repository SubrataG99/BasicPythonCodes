
# Take 3 integers as input and find out the greatest of all and also sort the numbers in Descending order

a = int(input('\nEnter 1st number : '))
b = int(input('Enter 2nd number : '))
c = int(input('Enter 3rd number : '))

if a==b and a==c:
    print(a, '=', b, '=', c)
    print('All 3 numbers are equal...\n')
else: 
    if a>b and a>c:
        if b>c:
            print(a, '>', b, '>', c)
        else:
            print(a, '>', c, '>', b)
        print('Greatest of the three is : ', a, '\n')
    elif b>c:
        if a>c:
            print(b, '>', a, '>', c)
        else:
            print(b, '>', c, '>', a)
        print('Greatest of the three is : ', b, '\n')
    else:
        if a>b:
            print(c, '>', a, '>', b)
        else:
            print(c, '>', b, '>', a)
        print('Greatest of the three is : ', c, '\n')