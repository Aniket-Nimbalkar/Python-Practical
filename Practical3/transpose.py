# Transpose of a Input matrix
r = int(input("Enter number of rows: "))
c = int(input("Enter number of cols: "))
matrix = []
for i in range(r):
    temp = [] * c
    print("Enter row ",i+1,":")
    temp = list(map(int,input().split()))
    matrix.append(temp)
print("Original Matrix:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j] , end = " ")
    print()
transpose = [[0 for x in range(r)]for y in range(c)]
for i in range(c):
    for j in range(r):
        transpose[i][j] = matrix[j][i]

print("Transposed Matrix:")
for i in range(c):
    for j in range(r):
        print(transpose[i][j] , end = " ")
    print()