matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print (matrix)

rows=len(matrix)
print(rows)

columns=len(matrix[0])
print(columns)

for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j],end=" ")
    print(" ")

print(matrix[1][0])
print(matrix[2][1])
print(matrix[1][1])
print(matrix[3][2])

m=[]
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

for i in range(0,r):
    temp=[]
    for j in range(0,c):
        x = int(input("Enter the element: "))
        temp.append(x)
    m.append(temp)

for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print(" ")