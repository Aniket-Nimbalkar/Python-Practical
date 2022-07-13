list1 = list(map(int,input("Enter elements of list1: ").split()))
list2 = list(map(int,input("Enter elements of list2: ").split()))
union = []
for i in list1:
    if(i in union):
        continue
    else:
        union.append(i)
for  j in list2:
    if(j in union):
        continue
    else:
        union.append(j)
print(union)