

#operation

#1.add
# a)append()
#arrName.append(10)
#print(arrName)

#arrName.insert(0,-9)
#print(arrName)   

# import array as anshika

# arrayName = anshika.array('i',[12,35,56,67])

#1. add
#a). append (value) -> add the values in last , t/c - 0(1), 0(N)
#b). insert (index,value) -> insert the value at index,t/c - 0(1), 0(N)

#2. delete
#1. remove() or remove(values)
#2. pop() or pop(index)

# arrayName.remove(12)
# print(arrayName)

# arrayName.pop(1)

# print(arrayName)
# arrayName[0] = 40
# arrayName[1]= 50
# print(arrayName)


# arr = [4,2,7,9]

# min_val = arr[0]
# max_val = arr[0]

# for num in arr:
#     if num < min_val:
#      min_val = num

#     if num > max_val:
#      max_val = num

# print("minimum: ", min_val)
# print("maximum: ", max_val)

# arr = [2,4,3,8,9]

# left = 0
# right = len(arr)-1

# while left < right:
#     arr[left],arr[right] = arr[right],arr[left]

#     left += 1
#     right -= 1

# print(arr)

arr = [1, 2, 3, 6, 5]

is_sorted = False

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print(is_sorted)






