n = 4
x = n-1
y = 1
for i in range(n):
    for j in range(x):
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end ="")
    x = x-1
    print()
y = n-1
k = 0
while y!=0:
    for i in range(k+1):
        print(" ",end = "")
    for i in range(y):
        print("*",end = "")
    for i in range(y-1):
        print("*",end="")
    k=k+1
    print()    
    y=y-1