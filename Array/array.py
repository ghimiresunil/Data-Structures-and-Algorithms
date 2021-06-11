from array import *

arr = array('i', [])

length = int(input('Enter the length of the array: '))

for i in range(length):
    values = int(input('Enter the value you want: '))
    arr.append(values)

print("The original array coming from user's input: {} ".format(arr))

print('The size of an array is {}. \n'.format(len(arr)))

## removing duplicates element from an array 
res = array('i', [])
for dup in arr:
    if dup not in res:
        res.append(dup)
print('Element after removing duplicate values(if exist) : {} \n'.format(res))

search_values = int(input('Enter the value you want to search: '))

count = 0

## Searching the index of an element
for a in res:
    if a == search_values:
        print('The index value of element {} is at {}.'.format(search_values, count + 1 ))
        break
    count += 1 
    
else:
    print('Sorry, Index value not found.')

    