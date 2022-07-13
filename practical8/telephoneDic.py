def FindName(number,Tdirectory):
    b = True
    for num in Tdirectory:
        if(num.get("Mob") == number):
            print("\nYour Name is " ,num.get("name"),"\n")
            b = False
    if(b):
        print("\nYour number not found in our Directory\n")
def FindNumber(name,Tdirectory):
    b = True
    for Name in Tdirectory:
        if(Name.get("name") == name):
            print("\n",name , "Your Mobile number is ",Name.get("Mob"), "\n")
            b = False
    if(b):
        print("\nYour name not found in our Directory\n")
def ChangeNumber(oldNum,newNum,Tdirectory):
    b = True
    for num in Tdirectory:
        if(num.get("Mob")==oldNum):
            num["Mob"] = newNum
            print(num.get("name"), "Your mobile number changed from ",oldNum," to ",newNum," Successfully \n")
            b = False
    if(b):
        print("\n Yout number not present in our directory \n ")
       
Tdirectory = [
    {"name":"Anas","Mob":8756489856},
    {"name":"Arvind","Mob":9657256574},
    {"name":"Abhishek","Mob":7863789841},
    {"name":"Salman","Mob":7458969841},
    {"name":"Salman","Mob":7458969841},
    {"name":"John","Mob":7458969456},
    {"name":"Harry","Mob":7458969256},
    {"name":"Aadi","Mob":7458969213},
    {"name":"Nadav","Mob":7458969412},
    {"name":"Laadan","Mob":7458969235},
]
b = True
while (b):
    n = int(input("Enter 1 to FindNumber\nEnter 2 to FindName\nEnter 3 to change Number \nEnter any other number to exit\n"))
    if(n==1):
        name = (input("Enter Your name: "))
        FindNumber(name,Tdirectory)
    elif(n==2):
        num = int(input("Enter your Mobile No.:"))
        FindName(num,Tdirectory)
    elif(n==3):
        oldNumber = int(input("Enter old Number:"))
        newNumber = int(input("Enter new Number:"))
        ChangeNumber(oldNumber,newNumber,Tdirectory)
    else:
        b = False