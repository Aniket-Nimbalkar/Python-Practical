#Python Program to print number pattern
n = 4
i = 1
while i<=n:
    for j in range(i):
        if(j!=0):
            print("*",end="")
        print(i,end="")
    i=i+1
    print()
j = n-1
while j!=0:
    for k in range(j):
        if(k!=0):
            print("*",end="")
        print(j,end="")
    j = j-1
    print()