from array import *

arr = array('i', [])

length = int(input('Enter the length of the array: '))

for i in range(length):
    values = int(input('Enter the value you want: '))
    arr.append(values)

print(arr)

print('The size of an array is', len(arr))

search_values = int(input('Enter the value you want to search: '))

count = 0

for a in arr:
    if a == search_values:
        print('The index value of element {} is {}.'.format(search_values, count + 1 ))
        break
    count += 1 
    
    print('Sorry, Index value not found')
    break
    
   