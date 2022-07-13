# to find whether number is Happy number or not
def ishappy(n):
    sum = 0
    while (n > 0):
        rem = n % 10
        sum += pow(rem, 2)
        n = n // 10
    return sum

num = int(input("Enter a number:- "))
temp = ishappy(num)
if (temp == 1):
    print(num, "is an happy number")
elif (temp == 4):
    print(num, "is not an happy number")
else:
    while (temp>= 10):
        temp = ishappy(temp)
        if (temp == 1):
            print(num, "is an happy number")
        elif (temp == 4):
            print(num, "is not an happy number")