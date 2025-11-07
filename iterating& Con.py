numbers=[10,20,30,40,50,60,70,80,90,100]
#Creating list
for num in numbers:
    if num % 3==0:
        #for the num inside numbers list if num div by 3 then print
        #(div_by_3_is:) and the num
        print(f"div_by_3_is:,{num}")
    
div_by_5= tuple  (num for num in numbers if num%5==0)
#take the numbers form the list that div by 5 and create a tuple  for this numbers
print("tuple=",num)

 
