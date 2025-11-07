matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#creating matrix 3x3
for row in matrix:
    for num in row:
        #access the num first by access the matrix then access the rows on it
        if num>=0:
            #using >=0 beacause all elements or numbers in the listv >0 then it will be work
            print(num)
            total=0
            #define (total)
for row in matrix:
    #access the rows in the matrix
    total+=sum(row)
    #sum every num in the row with the other one
print(f"total is {total}")
#print total of sum


           
