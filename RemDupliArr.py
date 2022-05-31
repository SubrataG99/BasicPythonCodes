
# Take a n-sized array and check and remove duplicate elements (if any) and also find sum and mean of all elements of the array

n = int(input('\nEnter the limit : '))
arr = []
for i in range(n):
    arr.append(int(input('Enter number {} :'.format(i+1))))

print('\nOriginal array :', arr)
print('Sum of all terms of the array :', sum(arr))
print('Mean of original array : {}'.format(format((sum(arr)/len(arr)), '.3f')))

Max = Min = arr[0]
for i in range(n):
    if arr[i]<Min:
        Min = arr[i]
    elif arr[i]>Max:
        Max = arr[i]
print('(Minimum, Maximum) --> ({}, {})'.format(Min, Max))

flag = 0
res = []
for i in arr:
    if i in res:
        flag = flag + 1
    else:
        res.append(i)

if flag==0:
    print('\nThere are no duplicates found in Original array...\n')
else:
    print('\nA total of {} duplicate(s) are removed'.format(flag))
    print('New array :', res)
    print('Sum of all terms of the array :', sum(res))
    print('Mean of original array : {}'.format(format((sum(res)/len(res)), '.3f')))
    
    Max = Min = res[0]
    for i in range(len(res)):
        if res[i]<Min:
            Min = res[i]
        elif res[i]>Max:
            Max = res[i]
    print('(Minimum, Maximum) --> ({}, {})\n'.format(Min, Max))