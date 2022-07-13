#Print unique elements from the list
list = list(map(int, input("Enter the elements of the array : ").split()))
unique_element = set(list)
print(unique_element)