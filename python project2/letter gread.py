def letter_grd():
    while True:
        x = input("Type yes or not :  .. ").lower()

        def show_marks(mark):
            print(f"your grade is : {mark}")

        if x == "yes":
            mark = float(input("Enter the student mark :  ____ "))
            print(f"your grade is : {mark}")
            if mark > 100:
                print("not a viled mark/")
            elif mark >= 90:
                print("Congratulation! you get A+ ..")
            elif mark >= 80 and mark < 90:
                show_marks("A ")
            elif mark >= 70 and mark < 80:
                show_marks("A- ")
            elif mark >= 60 and mark < 70:
                show_marks("B ")
            elif mark >= 50 and mark < 60:
                show_marks("C ")
            elif mark >= 40 and mark < 50:
                show_marks("D")
            elif mark >= 0 and mark < 40:
                print("you faill the exm ...")
            else:
                print(' Sorry ..invalid mark ! ')

        else:
            break

        print(f"The student mark is : {mark}\n")
        print("_________________by limon _________________")

letter_grd()
