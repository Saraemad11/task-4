students=[
    ["salma",49,80],
    ["ali",90,67],
    ["ahmed",78,97]
]
#craetung list

for student in students:
    name = student[0]
    score = student[1]
    attendance = student[2]
     #define score,name and attendence by index

    if score >= 50 and attendance >= 75:
        print("pass")
        if score >= 85:
            print("excellent")
            #nested if statement
    else:
        print("fail")

passing_students = 0
#define oassing students


for student in students:
    #accessing student in students
    score = student[1]
    #define the score =index num 1 in students
    if score >= 50:
        passing_students += 1
        #sum all passing students scores >=50  (filttering by if condition)
print(passing_students)
for  i in  range(1,len(students)+1):
    #access all numbers in  rows range from 1 and add 1 every turn to the end of the kist list
    for  j in  range(1,len(students)+1):
        #access all numbers in  column  range from 1 and add 1 every turn to the end of the kist list
        print(f"{i}*{j}")
        #muli i(rows)* j (column)

for i in range(1,passing_students+1):
    #i range from 1 to passing students count
    print("*"*i)
    # print i * passing student
