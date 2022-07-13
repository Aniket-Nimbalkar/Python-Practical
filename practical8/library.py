from platform import libc_ver
from typing import Collection
# import pymongo
#Library Managment System
def DisplayBooks(books):
    print("\nAvailable Books are\n")
    for bookName in books:
        print(bookName.get("name"))
    print()
def Displaycodes(books):
    print("Codes of Books")
    for i in books:
       print(i.get("code"),i.get("name"))
    print()

def issueBook(code,books,issuedBookcode):
    i = 0
    b = True
    for ABooks in books:
        i = i+1
        if(ABooks.get("code")==code):
            b = False
            print(books[i-1].get("name"),"book Issued to You \n ")
            issuedBookCode.append(code)
            books.remove(books[i-1])
            DisplayBooks(books)
    if(b):
        print("\nSorry Book is not available\n")
def ReturnBook(bookcode,books,bookname,issuedBookcode):
    b = True
    for ABooks in books:
        if(bookcode not in issuedBookCode):
            b = False
    if(b==False):
        print("This book is not issued to you")
    if(b):   
        bookdetail = {"name":bookname,"code":bookcode}
        issuedBookCode.remove(bookcode);
        books.append(bookdetail)
        print("\nYour have return ",bookname ," book successfully \n")
 
books = [
{"name":"Digital Systems","code":"001"},
{"name":"Data Structures & Algorithms","code":"002"},
{"name":"Discrete Mathematics","code":"003"},
{"name":"Operating Systems","code":"004"},
{"name":"Compiler Design","code":"005"},
{"name":"Computer Networks","code":"006"},
{"name":"Machine Learning","code":"007"},
{"name":"Software Engineering","code":"008"},
{"name":"Theory of Computation","code":"009"}]
b = True
issuedBookCode = []
while(b):
    n = int(input("Enter \n 1 To Display Available Books \n 2 To Issue Book \n 3 To Return Book \n 4 To Exit \n : "))
    if n == 1:
        DisplayBooks(books)
    elif n ==2:
        Displaycodes(books)
        code = (input("Enter code of book : "))
        issueBook(code,books,issuedBookCode)
    elif n ==3:
        name = input("Enter Name of book")
        code = input("Enter code of book")
        ReturnBook(code,books,name,issuedBookCode)
    elif n ==4:
        b = False
    else:
        print("\nInvalid Input\n")