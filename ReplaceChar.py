
# Take a String and a character as input and replace the character in the string with any special character {i have used here underscore sign}

s = str(input('\nEnter a word : '))
c = str(input('Enter the specified character : '))
flag = 0
print('Final string is ==>', end=' ')
for i in s:
    if i==c:
        print('_', end='')                                         # To remove any character insert '' 
        flag = flag + 1
    else:
        print(i, end='')
if flag==0:
    print('\nThe specified character "', c, '\b" is absent in the string\n')