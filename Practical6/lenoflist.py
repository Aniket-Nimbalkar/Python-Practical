def findlen(arr):
    if arr:
        return 1+findlen(arr[1:])
    return 0

arr = list(map(int,input("Enter elements of list: ").split()))
print(findlen(arr))