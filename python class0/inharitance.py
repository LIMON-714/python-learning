class student():
    name=" "
    age=  " "
    gender= " "

class person(student):
    pass

name= input("Enter your name : ")
age= int(input("Enter your age : "))
gender=input("Enter your gender : ")
p1= person()
print(name,"your age is " ,age, " gender " ,gender)