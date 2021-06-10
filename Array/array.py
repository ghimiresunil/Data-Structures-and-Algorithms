from array import *

arr =  array('i', [])

length = int(input('Enter the length of the array: '))

for i in range(length):
    values = int(input('Enter the next value: '))
    arr.append(values)

print(arr)

search_value = int(input('Enter the value for search: '))

count = 0
for a in arr:
    if a == values:
        print(count)
        break
    count += 1

