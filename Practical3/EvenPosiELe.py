#Printing the element of the array present on the even position
n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
print("Even positioned Elements are : ",end = " ")
for i in range(len(arr)):
    if(i%2==0):
        print(arr[i] , end=" ")