matrix= [
    [1,2,3],
    [4,5,6],
]
''' 
matrix[0][2]=10
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][2]) #matrix index call

'''
for row in matrix:
    print(row) #row call
    for col in row:
        print(col) #col call