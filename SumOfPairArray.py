
# Take no. of items and array of that size as input, now print the pairs of number (as set) from the array which when added gives the sum given by user as Input

n = int(input('\nEnter how many numbers : '))
li = []
for i in range(n):
    temp = int(input('Enter number {}: '.format(i+1)))
    li.append(temp)
print(li, '\n')
li.sort()
flag = 0
dig = int(input('Enter a sum : '))
print('Pairs whose sum is equal to', dig, 'are :')
for i in range(n//2):
    for j in range(i+1, n):
        if li[i] + li[j] == dig:
            print('({}, {})'.format(li[i], li[j]), end=' ')
            flag = flag + 1
if flag==0:
    print('OOPS ! No such pairs found\n')