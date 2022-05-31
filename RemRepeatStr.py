
# Take a string as input and after removing the repeated characters (keeping the first occurence only of a repeated character) in the string (if any)

s = str(input('\nEnter a word : '))
res = ''
for i in s:
    if i not in res:
        res = res + i
print(res)