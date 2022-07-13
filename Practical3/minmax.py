#Printing the largest and smalles element of array
n = int(input("Enter the size of the array: "))
arr = list(map(int,input("Enter elements of array: ").split()))
min = arr[0]
max = arr[0]
for i in range(n):
    if arr[i]<min:
        min = arr[i]
    if arr[i]>max:
        max = arr[i]

print('Min Value :',min)
print('Max Value :',max)