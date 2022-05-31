
# Take the end limit of a range as input and find out all Prime numbers within that range

n = int(input('\nEnter the Highest limit of the range : '))

print('Prime numbers from 1 to', n, 'are : ', end='')
for i in range(1, n+1):
    flag = 0
    for j in range(1, i+1):
        if i%j==0:
            flag = flag + 1
    if flag==2:
        print(i, end=' ')
print('\n')