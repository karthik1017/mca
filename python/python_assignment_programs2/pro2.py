# 2. Find the smallest of three numbers. 

num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
num3 = int(input('enter the third number: '))
if(num1 < num2):
    if(num1 < num3):
      print("the smallest number is num1: ",num1)
elif(num2 < num3):
      print("the smallest number is num2: ",num2)
else:
    print("the smallest number is num3: ",num3)

    
 
 