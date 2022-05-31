
# Take a string as input from User and find out number of :
# Characters
# Vowels
# Consonants
# Digits (if any)
# Special Character

word = str(input('\nEnter a string : '))

v = 0
c = 0
n = 0
sc = 0
vow = ['a', 'e', 'i', 'o', 'u']
word = word.lower()

for ch in word:
    if ch.isalpha():
        if ch in vow:
            v = v + 1
        else:
            c = c + 1
    elif ch.isnumeric():
        n = n + 1
    else:
        sc = sc + 1

print('Your input has :', len(word), 'characters\n\t\t', v, 'vowels\n\t\t', c, 'consonant\n\t\t', n, 'digits\n\t\t', sc, 'special characters\n')