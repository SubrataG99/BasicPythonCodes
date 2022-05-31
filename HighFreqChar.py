
# Take a string as input and print the character that has the highest frequency in the string

s = str(input('\nEnter a word : '))
freq = 0
freqChar = ''
for i in range(len(s)):
    temp = 0
    for j in range(i, len(s)):
        if s[j]==s[i]:
            temp = temp + 1
    if temp>freq:
        freq = temp
        freqChar = s[i]
if freq>1:
    print('"', freqChar, '" occurs for maximum', freq, 'times\n')
else:
    print('All the characters of "', s, '" occurs only once\n')