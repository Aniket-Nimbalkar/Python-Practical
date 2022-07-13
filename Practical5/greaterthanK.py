#Extract elements with frequency greater than k
list = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter Value of k: "))
extracted = []
freq ={}
for e in list:
    if e in freq:
        freq[e]+=1
    else:
        freq[e] =1
for key, value in freq.items():
   if value >= k:
    extracted.append(key)
print(extracted)