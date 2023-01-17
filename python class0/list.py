
subject = [ 'C', 'C++','Java','Python','Go','R','Javascript','Swift','Sql']
print(f"\n{subject}")

subject.insert(2,"C#") # we can add value in any indexs
print(subject)

print(subject[2]) #use for showing this index value
print(subject[3:]) # use only show data index 3 to end
print (subject[-1]) # show reverse value

print("Python" in subject ) # its show boolean data
print('nodejs' not in subject)# it is in list or not

subject.append('NodeJs') # its add the subject name in the last index
print(subject)

print(f"the lenth of : {len(subject)}") # its count the lenth of the list

subject.pop() # its remove the last value of the list
print(subject)

subject.pop(2) # we can call the index number and remove the value
print(subject)

subject2 = subject.copy() # if need we can copy total list on the function
print(f"subject2 = {subject2}")

subject.remove('Go') # we can remove the needless value
print(subject)

subject.clear() # we can clear all the value on the list
print(f"{subject}\n")


number= [3,6,5,12,34,55,1,5]
print(f"{number} \n")

pos= number.index(12) # we can count the index number on the lists value
print(pos)

cou=number.count(5) # we can count how many time the values are on the list
print(cou)

number.sort() # we can sorting the list values
print(number)

number.reverse() # and we can reverse the values
print(number)





