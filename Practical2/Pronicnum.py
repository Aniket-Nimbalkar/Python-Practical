# to find given number is pronic number or not
def isPronicNum(n):
    for i in range(n):
        if i * (i + 1) == n :
            break
    return 1
        
test = 0
num = int(input("Enter a number:- "))
test = isPronicNum(num)
if test==1:
    print(num, "is a pronic number")
else:
    print(num, "is not a pronic number")