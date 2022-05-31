
# Take 2 numbers as input and find out the LCM (Lowest Common Multiple) of them

a = int(input('\nEnter first number : '))
b = int(input('Enter second number : '))

temp = 1
if a<b:
    if a%b==0:
        lcm = b
    else:
        for i in range(2, a):
            if a%i==0 and b%i==0:
                temp = i
                break
        lcm = temp*(a//temp)*(b//temp)
else:
    if b%a==0:
        lcm = a
    else:
        for i in range(2, b):
            if b%i==0 and a%i==0:
                temp = i
                break
        lcm = temp*(a//temp)*(b//temp)

print('LCM of', a, 'and', b, 'is : ', lcm, '\n')
