n=int(input("Enter the last value : "))
sum=0

for x in range(2,n+1,2):
    print(x*x)
    sum= sum+x*x


print("//The total sumation is 1 to",n ,"is : ",sum)