
# Take a string and find unique character in that string
# Unique character = Which occurs only once in the string

s = str(input('\nEnter : '))

charOrder = []
cnt = {}

for c in s:
    if c in cnt:
        cnt[c]+=1
    else:
        cnt[c] = 1
        charOrder.append(c)
print('The unique character(s) is/are :', end='')
for c in charOrder:
    if cnt[c]==1:
        print(c, end=', ')