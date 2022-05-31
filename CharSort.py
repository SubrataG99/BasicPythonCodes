
# Take a string as input and rearrange the characters in (i) Ascending order (ii) Descending order

s = str(input('\nEnter a string : '))
# asc = ''
# desc = ''
# #-------------------------------------------------------Ascending order
# for i in range(len(s)):
#     temp = s[i]
#     for j in range(i+1, len(s)):
#         if s[j]<temp:
#             temp = s[j]
#     asc = asc + temp
print('Ascending order -->', ''.join(sorted(s)))

# #-------------------------------------------------------Descending order
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         if s[j]>s[i]:
#             temp = s[j]
#             s[j] = s[i]
#             s[i] = temp
print('Descending order -->', ''.join(sorted(s, reverse=True )), '\n')

# The commented out codes work for C++ but not in python