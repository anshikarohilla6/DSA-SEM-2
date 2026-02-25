# two matrix addition,substraction,multiplication and division

# rows= int(input("enter the value of row: "))
# column= int(input("enter the value of column: "))
# a=[]
# for i in range(rows):
#     rowArr=[]
#     for j in range(column):
#         val=(int("enter your value: "))
#         rowArr.append(val)
#         a.append(rowArr)
#         print(a)

# rows=3
# cols=3
# matrix1=[]
# matrix2=[]
# sum=[]
# for i in range(rows):
#     rowArr = []
#     for j in range(cols):
#         val=int(input(f"enter your value at[{i}]+[{j}]: "))
#         rowArr.append(val)
#     matrix1.append(rowArr)
# for i in range(rows):
#     rowArr=[]
#     for j in range(cols):
#         val=int(input(f"enter the value of cols: "))

  
row = 3
col = 3
matrix = []
print ("original matrix : ")
for r in range(row):
    for c in range(col):
        print(matrix[r][c],ends=" ")
    print ()
for r in range(row-1):
    for c in range (r+1 , col):
        print(matrix[r][c],end=" ")
    print("upper triangle element")

for r in range (1,row):
    for c in range (r):
        print(matrix[r][c],end=" ")
    print("lower triangle element")

for r in  range(row):
    for c in range (col):
        matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
print("transpose matrix: ")

transpose = [[0 for c in range (col)] for r in range(rows)]
for r in range (row):
    for c in range(col):
        transpose[c][r]=matrix[r][c]

print(transpose)









