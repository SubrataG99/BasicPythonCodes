
# Take String as input and a character to search from user and print the frequency of occurence of the character

s = str(input('\nEnter a Word : '))
c = str(input('Which character to count : '))
cnt = 0
for i in s:
    if i==c:
        cnt = cnt + 1
print('"', c, '"',  'occurs for', cnt, 'times\n')

    #   double quotes inside single quotes give quotation marks in print statement