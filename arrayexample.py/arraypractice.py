import array as ashu

arrayName = ashu.array('i' , [12,35,56,67])

sum=0
product=1
for val in arrayName:
    sum+=val
    product *= val

print(sum)
print(product)