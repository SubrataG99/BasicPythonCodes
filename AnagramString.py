
# Find if two strings are anagram to each other or not
# {String Anagram --> If two strings have same characters irrespective of their positioning}
# ['abcd', 'dbca' = Anagram] but ['abcd', 'abbcdd' = Not Anagram]

astr = str(input('\nEnter the first string : '))
bstr = str(input('Enter the second string : '))

ali = [char for char in astr]
bli = [char for char in bstr]
ali.sort()
bli.sort()

print('String 1 -->', str(ali))
print('String 2 -->', str(bli))

if ali==bli:
    print('Both are Anagram of each other\n')
else:
    print('The strings are NOT Anagram\n')