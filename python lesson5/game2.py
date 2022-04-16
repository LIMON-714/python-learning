numOfWord=0
numOfDigit=0
numOfLettre=0
text= input("Enter your text as you like: ")
for x in text:
    if x>='a' and x<='z':
        numOfLettre=numOfLettre+1
    elif x>='0' and x<='9':
        numOfDigit=numOfDigit+1
    elif x==' ':
        numOfWord=numOfWord+1

print("the number of lettre of the text is : ",numOfLettre)
print("the number of digit of the text is : ",numOfDigit)
print("the number of word of the text is : ",numOfWord+1)
