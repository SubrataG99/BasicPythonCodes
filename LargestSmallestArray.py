
# Take n-spaced integers as array and find out the smallest and largest of the array and also sort the array both in Ascending and Descending order

n = int(input('\nEnter the size of array : '))
arr = []
for i in range(n):
    temp = int(input('Enter number {} : '.format(i+1)))
    arr.append(temp)
print('\nOriginal Array :', arr)

Max = Min = arr[0]
for i in range(n):
    if arr[i]<Min:
        Min = arr[i]
    elif arr[i]>Max:
        Max = arr[i]
print('(Smallest, Largest) --> ({}, {})'.format(Min, Max))

#-------------------------------------------------------------------Ascending Order
for i in range(n):
    for j in range(n):
        if arr[i]<arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print('Array in Ascending order :', arr)

#-------------------------------------------------------------------Descending Order
for i in range(n):
    for j in range(n):
        if arr[i]>arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print('Array in Descending order :', arr, '\n')
