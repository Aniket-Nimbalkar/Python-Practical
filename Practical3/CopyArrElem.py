#Copying the element of one array into other
n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
new_arr = []
for i in range(n):
    new_arr.append(arr[i])
print("Copied Elements in new_arr : " , end = " ")
for i in range(n):
    print(new_arr[i] , end= " ")