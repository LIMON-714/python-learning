try:
    x = int(input("Enter an integer numbar : "))
except ValueError:
    print("somthing want wrong ..... please try again")
else:
    print("nothing want weong")
finally:
    print("try to except finished")