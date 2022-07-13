#Count the number of tuples in a given list
list = [(1,2,3,4),"Python",("Aniket", "Kunal", "Yash"),('a','b','c','d'),15]

count = 0
for i in list:
    if(type(i) is tuple):
        print(i)
        count = count + 1
print("Total number of tuples:",count)