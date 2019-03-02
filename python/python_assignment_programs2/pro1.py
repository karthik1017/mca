# 1. Find the largest of three numbers.

num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
num3 = int(input('enter the third number: '))
if(num1 > num2):
    if(num1 > num3):
      print("the largest number is num1: ",num1)
elif(num2 > num3):
      print("the largest number is num2: ",num2)
else:
    print("the largest number is num3: ",num3)

    
 
 