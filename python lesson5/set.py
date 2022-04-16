num1={1,2,3,4,5,5,6} #dublicat values is not print 2nd time
num2=set([4,5,6])
print(num1)
num2.add(9)
print(num2)
print(7 in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)