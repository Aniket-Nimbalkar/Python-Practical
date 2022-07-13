#Count occurrence of word in a given list
sentence = input("Enter the Sentence: ")
word = input("Enter the word: ")
count = 0
for i in sentence.split():
    if(i == word):
        count = count+1
print("The Given word occured",count,"times")