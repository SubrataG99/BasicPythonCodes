
# Take a string as input and change it to (i) Lower case all (ii) Upper case all (iii) Alternate case 

s = str(input('\nEnter a word : '))

#------------------------------------------------------------To Upper
print('The string all in Upper case : ', end='')
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        print(chr(ord(i)-32), end='')
    else:
        print(i, end='')

#-----------------------------------------------------------To Lower
print('\nThe string all in Lower case : ', end='')
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        print(chr(ord(i)+32), end='')
    else:
        print(i, end='')

#----------------------------------------------------------Alternate case
print('\nThe string in ALternate case : ', end='')
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        print(chr(ord(i)-32), end='')
    elif ord(i)>=65 and ord(i)<=90:
        print(chr(ord(i)+32), end='')

print('\n')


# Some important points to remember :
# [A - Z] = [65 - 90]
# [a - z] = [97 - 122]
# low --> high : -32
# high --> low : +32