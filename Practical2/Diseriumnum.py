# To find given number is Diserium or not
num = int(input("Enter a number:- "))
sum = 0
l = len(str(num))
temp = num
while (temp != 0):
    rem = temp % 10
    sum += pow(rem, l)
    l = l - 1
    temp = temp // 10
if (sum == num ):
    print(num, "is an Disarium number")
else :
    print(num, "is not am Disarium number")