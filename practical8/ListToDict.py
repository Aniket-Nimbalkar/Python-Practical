list1 = [1,2,3,4]
list2 = ["A","B","C","D"]
dict = {}
for i in range(len(list1)) :
    dict[list1[i]] = list2[i]
print(dict)