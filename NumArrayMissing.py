
# Take length of an Array as input from User and generate random values for length-1 size of array and print the elements not present in the array

import random

def randlist(n):
    ele = random.sample(range(n+1), n)
    print('List :\n', ele, '\n')
    for i in range(n+1):
        if i not in ele:
            miss = i
            print(miss, 'is missing from the list\n')
    
n = int(input('\nEnter the last limit of array from 1 to : '))
randlist(n)