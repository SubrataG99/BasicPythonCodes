
# Take a String and a character as input and replace the character in the string with any special character {i have used here underscore sign} using the "replace()" command

s = str(input('\nEnter a word : '))
c = str(input('Enter the character to replace : '))

print('Final string -->', s.replace(c, '_'), '\n')