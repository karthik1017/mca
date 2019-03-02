number = int(input("enter the value for number: "))
if(number % 3 == 0):
    if(number % 6 == 0):
        if(number % 9 == 0):
            print("the number is divided by 3,6 and 9")
        else: 
            print("the number is divided by only 3 and 6 but not by 9")
    else: 
        print("the number is only divided by 3 and not divided by 6 and 9:")
else:
    print("the number is not divided by any number:")