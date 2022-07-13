# to find given number is harshad number or not
num = int(input("Enter a number:- "))
sum = 0
temp = num
while (temp != 0):
    rem = temp % 10
    sum += rem
    temp = temp // 10
if (num%sum == 0 ):
    print(num, "is an Harshad number")
else :
    print(num, "is not am Harshad number")