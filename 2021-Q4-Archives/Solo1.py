#wap to find the avg word length of a sentence
text = input().split() #turns input string into a list
a=len(text) #gives the no of words/elements in list
b=0
for i in text:
    count=len(i)
    b+=count #gives the no of characters in each word/element in list
print(b/a)