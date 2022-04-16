from  random import randint

for x in range(1,6):
    gussNumber = int(input("Enter guss number as you like : "))
    randomNumber= randint(1,5)
    if gussNumber==randomNumber:
        print("congratulation ! you have won the game //")
    else:
        print("sorry! try again you lost the game //")
    print("The random number is ",randomNumber)

print("")
print("\t--------thank you ----------")