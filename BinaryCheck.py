
# Take a number from user and determine if it is a Binary number (only 0 and 1) or not

n = int(input('\nEnter a number : '))
s = n
flag = 0
binli = [0, 1]
while s>0:
    if (s%10) not in binli:
        flag = flag + 1
        break
    s = s//10
if flag>0:
    print(n, 'is NOT a Binary number...\n')
else:
    print(n, 'is a Binary number\n')