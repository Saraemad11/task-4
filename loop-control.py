n=int(input("Enter a number"))
for i in range(1, n+1):
  #take num from loop 1
  for j in range(1, n+1):
   if i ==j:
    continue
    #if condition is true don't print it and continue the loop
  print(f"{i}x{j}={i*j}")
   #print all numbers result from 1 to the num user entered within i==j