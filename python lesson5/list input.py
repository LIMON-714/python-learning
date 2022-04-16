n= input("Enter your numbers:")
list= n.split()
print(list)
sum=0
for num in list:
    sum= sum+int(num)

print("\nThe all sumation is : ",sum)