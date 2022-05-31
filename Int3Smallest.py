
# Take 3 numbers and find out the smallest of them and sort them in Descending order

a = int(input('\nEnter 1st number : '))
b = int(input('Enter 2nd number : '))
c = int(input('Enter 3rd number : '))

if a==b and a==c:
    print(a, '=', b, '=', c)
    print('All are equal...\n')
elif a==b:
    if a<c:
        print(a, '=', b, '<', c)
        print('Smallest is : ', a, '\n')
    else:
        print(a, '=', b, '>', c)
        print('Smallest is : ', c, '\n')
elif b==c:
    if b>a:
        print(a, '<', b, '=', c)
        print('Smallest is : ', a, '\n')
    else:
        print(a, '>', b, '=', c)
        print('Smallest is : ', c, '\n')
elif a==c:
    if a<b:
        print(a, '<', b, '>', c)
        print('Smallest is : ', a, '\n')
    else:
        print(a, '>', b, '<', c)
        print('Smallest is : ', b)
elif a<b and a<c:
    if b<c:
        print(a, '<', b, '<', c)
    else:
        print(a, '<', c, '<', b)
    print('Smallest is : ', a, '\n')
elif b<a and b<c:
    if a<c:
        print(b, '<', a, '<', c)
    else:
        print(b, '<', c, '<', a)
    print('Smallest is : ', b, '\n')
else:
    if a<b:
        print(c, '<', a, '<', b)
    else:
        print(c, '<', b, '<', a)
    print('Smallest is : ', c, '\n')