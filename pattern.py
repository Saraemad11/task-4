students=[40,58,79,90,99]
for score in students:
  if score >=90:
    if score>=85:
      print("Excellent")
    print("A")
  elif score >=75:
    print("B")
  elif score >=50:
    print("C")
  else:
    print("F")
passing_students=[]
#creating list called passing students to filter the scores
for i in  students:
  if i >=50:
     # if i >=50 then it will be added in passing students list
     passing_students.append(i)
     #if i >=50 then add i in passing students
heigh=len(passing_students)
#calc passing students len
for i in range (1,heigh+1):
 # loop from 1 to passing students num
 print("*"*i)
 #print (*) * passing students