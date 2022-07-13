#printing the element of the array in reverse order
n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
i = len(arr)-1
while(i>=0):
    print(arr[i] , end = " ")
    i = i-1