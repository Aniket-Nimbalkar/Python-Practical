#Ascending Merge Sort
def Ascending_merge(Arr,beg,mid,end):
    n1 = mid-beg+1
    n2 = end-mid
    left = [0] *n1
    right = [0] *n2
    for i in range(n1):
        left[i] = (Arr[i+beg])
    for i in range(n2):
        right[i] = (Arr[mid + 1 + i])
    
    a = 0
    b = 0
    k = beg
    while a<n1 and b<n2:
        if(left[a]<=right[b]):
            Arr[k] = left[a]
            a = a+1
        else:
            Arr[k] = right[b]
            b = b+1
        k= k+1
    while a<n1:
        Arr[k] = left[a]
        a = a+1
        k = k+1
    while b<n2:
        Arr[k] = right[b]
        b = b+1
        k = k+1
    


def Ascending_mergeSort(Arr,beg,end):
    if beg<end:
        mid = (beg+end)//2
        Ascending_mergeSort(Arr,beg,mid)
        Ascending_mergeSort(Arr,mid+1,end)
        Ascending_merge(Arr,beg,mid,end)

arr = [7,4,3,6,1,5,9]
print("Original array:",arr)
n = len(arr)
Ascending_mergeSort(arr,0,n-1)
print("Sorted array:",arr)
