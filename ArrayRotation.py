
# Program to Rotate elements (in both directions) in Array where the array and the no. of shifting elements is given by User

import random

#--------------------------------------------------------------------------------------------Left shifting elements
def LeftRot(arr, d):
    temp = []
    n = len(arr)
    d = d%n
    i = d
    while (i != (d-1)%n):
        temp.append(arr[i])
        i = (i+1)%n
    temp.append(arr[i])
    return temp

#------------------------------------------------------------------------------------------Right shifting the elements
def RightRot(arr, d):
    temp = []
    n = len(arr)
    d = d%n
    for k in range((n-d), n):
        temp.append(arr[k])
    for k in range((n-d)):
        temp.append(arr[k])
    return temp

#-----------------------------------------------------------------------------------------Main Function (for user)
n = int(input('\nEnter the size of array : '))
a = []
for i in range(n):
    ran = random.randint(1, 30)
    a.append(ran)
print('The original array is :', a)

s = int(input('\nEnter the shift : '))
l = LeftRot(a, s)
r = RightRot(a, s)
print('After', s, 'place of Left shift, the array is :', l)
print('After', s, 'place of Right shift, the array is :', r)