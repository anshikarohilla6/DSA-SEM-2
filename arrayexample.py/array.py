

#operation

#1.add
# a)append()
#arrName.append(10)
#print(arrName)

#arrName.insert(0,-9)
#print(arrName)   

import array as anshika

arrayName = anshika.array('i',[12,35,56,67])

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


for i in range(0, len(arrayName)):
    print(arrayName[i], end=" ")