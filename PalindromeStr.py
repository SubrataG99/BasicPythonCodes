
# Take a string and check whether it is a Palindrome or not
# 'abcba' --> Palindrome
# 'abcde' --> Not-Palindrome

s = str(input('\nEnter a word (case sensitive) : '))
temp = ''
for i in range(len(s)):
    temp = temp + s[len(s) - 1 - i]
print('Reversed word is -->', temp)
if s==temp:
    print('Both are PALINDROME strings...\n')
else:
    print('Both are NOT PALINDROME string...\n')