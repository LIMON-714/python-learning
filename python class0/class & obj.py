'''
class myclass:
     x=5

p1= myclass()
print(p1.x)
'''

class parson:
     def __init__(self,name,age) :
          self.name= name
          self.age= age


name= input("Enter your name  :  ")
age= int(input("Enter your age :  "))
p1= parson(name,age)
print(p1.name, "your age is ",p1.age )