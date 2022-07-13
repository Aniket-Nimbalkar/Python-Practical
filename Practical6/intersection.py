list1 = list(map(int,input("Enter elements of List1: ").split()))
list2 = list(map(int,input("Enter elements of list2: ").split()))
intersection = []
for i in list1:
    if(i in list2 and i not in intersection):
        intersection.append(i)
print(intersection)