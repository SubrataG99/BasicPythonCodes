
# Take a string from User and print its ASCII value of each character

s = str(input('\nEnter a letter/word : '))

for i in s:
    print(i, ' --> ', ord(i))
print('\n')


# ord() --> Char to Ascii
# chr() --> Ascii to Char
