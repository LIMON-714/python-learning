
for x in range (5):
    mark = int(input("Enter the student mark = ____ "))

    if mark >= 100:
        print("The mark is not valid ")
    elif mark >= 80 and mark <= 99:
        print("Congratulation! you get A+ ")
    elif mark >= 70 and mark <= 79:
        print("You get A the emx")
    elif mark >= 60 and mark <= 69:
        print("you get A- the exm")
    elif mark >= 50 and mark <= 59:
        print("you get B the exm")
    elif mark >= 40 and mark <= 49:
        print("you get C the exm")
    elif mark >= 33 and mark <= 39:
        print("pass you get D the exm")
    else:
        print("sorry! you fail the exm plese try again")
    print("The student mark is : ", mark)
    print("_________________by limon _________________")



