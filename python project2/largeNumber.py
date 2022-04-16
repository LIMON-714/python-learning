
for x in range (3):

    num1 = int(input("Enter any number as you like :"))
    num2 = int(input("Enter any number as you like :"))
    num3 = int(input("Enter any number as you like :"))

    if num1 > num2 and num1 > num3:
        print("The large number is :", num1)
    elif num2 > num1 and num2 > num3:
        print("The large number is :", num2)
    else:
        print("The large number is : ", num3)

    print("____________BY LIMON____________")
