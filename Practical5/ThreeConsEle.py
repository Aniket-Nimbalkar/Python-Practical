list = list(map(int, input("Enter the elements of the array : ").split()))
x = len(list)
i = 0
while i<(x-2):
    if(list[i]==list[i+1] and list[i]==list[i+2]):
        print("Consecutive element:",list[i])
        i = i+2
    i = i+1