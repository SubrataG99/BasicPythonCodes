
# Take n-sized integer array and find out the integer with highest occuring frequency in array

import random

n = int(input('\nEnter the Upper limit : '))
li = []
for i in range(n+1):
    temp = random.randint(1, n+1)
    li.append(temp)
print('List -->\n', li)
li.sort()


res = {}
for i in li:
    res[i] = res.get(i, 0) + 1

print('\nDictionary -->\n', res)
# print(res.keys())                                                             # Gives the Keys of the Dictionary
# print(res.values())                                                           # Gives the Values of the Dictionary
# print(res.items())                                                            # Gives both (key, value) as set in Dictionary

print('\nAfter observation :')
for key, val in res.items():
    if val>1:
        print(key, end=' occurs ')
        print(val, 'times')
print('')