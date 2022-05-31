
# Take a String as input and print the sum of all the digits present in the string

s = str(input('\nEnter a word : '))
d = 0
cnt = 0
for i in s:
    if i.isdigit():
        d = d + int(i)
        cnt = cnt + 1
print('There are total', cnt, 'digits in the string which sum upto', d, '\n')