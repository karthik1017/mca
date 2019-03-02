# 6. Display the multiplication table from 1 to n in the form 1*1 = 1 

n = int(input("enter the range:"))
initial = 1
while initial <= n:
    j = 1
    while j <= 10:
       print(initial,'*',j,'=',initial*j)
       j=j+1
    initial=initial+1